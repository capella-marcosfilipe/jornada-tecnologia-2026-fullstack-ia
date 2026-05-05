import json

from langchain_groq import ChatGroq
from pydantic import SecretStr

from backend.config.settings import settings
from backend.graph.state import AgentState

class ReasoningNode:
    def __init__(self):
        self.llm = ChatGroq(api_key=SecretStr(settings.GROQ_API_KEY), model="llama-3.1-8b-instant")

    def _parse_response_content(self, content: str | list[str | dict]) -> dict:
        if isinstance(content, list):
            content = "".join(
                part if isinstance(part, str) else json.dumps(part)
                for part in content
            )

        cleaned_content = content.strip()

        if cleaned_content.startswith("```"):
            cleaned_content = cleaned_content.removeprefix("```json").removeprefix("```").strip()
            if cleaned_content.endswith("```"):
                cleaned_content = cleaned_content[:-3].strip()

        return json.loads(cleaned_content)

    def execute(self, state: AgentState) -> dict:
        print("--- EXECUTANDO RACIOCÍNIO (LLAMA 3) ---")
        
        prompt = f"""
        Você é um auditor de murais da UNICAP. 
        Com base na descrição da imagem: "{state['raw_description']}", 
        gere um informativo estruturado em JSON com:
        - titulo: (curto e direto)
        - categoria: (Financeiro, Eventos, Acadêmico ou Administrativo)
        - resumo: (máximo 20 palavras)
        - relevancia: (Alta, Media ou Baixa)
        
        Responda APENAS o JSON.
        """
        
        response = self.llm.invoke(prompt)
        structured_data = self._parse_response_content(response.content)
        
        return {
            "structured_data": structured_data,
            "is_relevant": True
        }