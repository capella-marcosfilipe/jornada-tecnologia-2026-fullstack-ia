import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File
from backend.schemas.informativo import InformativoSchema
from backend.config.settings import settings
from backend.services.storage_service import StorageService

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

    # 2. Mock de resposta (Aqui o T1 entrega o bastão para o T2)
    # No próximo passo (T2), este dicionário virá do LangGraph
    novo_informativo = {
        "id": str(uuid.uuid4()),
        "titulo": f"Análise Pendente: {file.filename}",
        "categoria": "Processando",
        "resumo": "A inteligência artificial processará esta imagem na Parte 2.",
        "relevancia": "Media"
    }

    # 3. Persistir no JSON
    StorageService.save_data(novo_informativo)
    
    return novo_informativo