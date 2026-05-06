# Mural Inteligente UNICAP
### Mini-curso Full-Stack com IA — Centro de IA FASA/UNICAP

Aplicação que recebe uma foto de um aviso físico, processa a imagem com visão computacional (BLIP) e raciocínio via LLM (Groq), e exibe o informativo estruturado em um painel Angular.

---

## Stack

**Backend**
- Python · FastAPI · Uvicorn
- LangGraph · LangChain-Groq
- Transformers (BLIP) · PyTorch CPU · Pillow
- Pydantic Settings

**Frontend**
- Angular 21 (standalone components) · TypeScript 5.9
- RxJS · Signals · HttpClient

---

## Configuração e execução

### Pré-requisitos
- Python 3.11+
- Node.js 20+ e npm 11+
- Chave de API gratuita em [console.groq.com](https://console.groq.com)

### Backend
```bash
# Na raiz do projeto
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/macOS

pip install -r backend/requirement.txt

# Crie o arquivo de variáveis de ambiente
copy backend\.env.example backend\.env
# Edite backend\.env e preencha GROQ_API_KEY

uvicorn backend.main:app --reload
# API disponível em http://localhost:8000
```

### Frontend
```bash
cd frontend
npm install
npm start
# App disponível em http://localhost:4200
```

---

## Como o pipeline de IA funciona

```
[Foto do aviso]
      │
      ▼
  VisionNode          ← BLIP gera descrição textual da imagem
      │
      ▼
 ReasoningNode        ← Groq (LLM) classifica relevância e estrutura os dados
      │
      ▼
 data/data.json       ← Informativo salvo
      │
      ▼
 Dashboard Angular    ← Exibição em tempo real via Signals
```

O estado compartilhado entre os nós (`AgentState`) carrega: `image_path`, `raw_description`, `is_relevant`, `structured_data` e `history`.

API Key = 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
  