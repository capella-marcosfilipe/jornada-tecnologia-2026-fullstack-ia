import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File
from backend.schemas.informativo import InformativoSchema
from backend.config.settings import settings
from backend.services.storage_service import StorageService
from backend.graph.builder import build_graph

app_graph = build_graph()
router = APIRouter()

@router.get("/informativos")
async def listar_informativos():
    return StorageService.load_data()["informativos"]

@router.post("/analisar", response_model=InformativoSchema)
async def analisar_mural(file: UploadFile = File(...)):
    # 1. Salvar a imagem temporariamente
    upload_dir = settings.UPLOAD_DIR
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = upload_dir / f"{uuid.uuid4()}_{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Executa o Grafo Agêntico
    inputs = {"image_path": file_path, "history": []}
    
    # .invoke é síncrono, mas pode ser adaptado para async se necessário,
    # daí usaríamos await app_graph.ainvoke(inputs)
    result = app_graph.invoke(inputs)
    
    # Extrai o dado estruturado gerado pela LLM
    novo_info = result["structured_data"]
    novo_info["id"] = str(uuid.uuid4())

    # 3. Persistir no JSON
    StorageService.save_data(novo_info)
    
    return novo_info