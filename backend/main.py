from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.analise_router import router as analise_router
from backend.config.settings import settings
import uvicorn

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Verificar se o diretório de uploads existe, caso contrário, criar
upload_dir = settings.UPLOAD_DIR
if not upload_dir.exists():
    upload_dir.mkdir(parents=True, exist_ok=True)

# Servir arquivos de imagem para o frontend
app.mount("/uploads", StaticFiles(directory=str(upload_dir)), name="uploads")

app.include_router(analise_router)

@app.get("/")
def read_root():
    return {"status": "Centro de IA FASA/UNICAP - API Online"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)