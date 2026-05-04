from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config.settings import settings
# from backend.routers import analise_router  # Comentado para o Tutor 1

app = FastAPI(title=settings.APP_NAME)

# Configuração de CORS para o Angular (Tutor 3)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção usaríamos a URL do Angular
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Centro de IA FASA/UNICAP - API Online"}

# app.include_router(analise_router.router)