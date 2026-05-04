from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    """Configurações da aplicação carregadas de forma automática.

    O `Pydantic Settings` é uma ferramenta do Pydantic feita para guardar e
    carregar configurações da aplicação de maneira simples e segura. Ele pega
    valores que podem vir de variáveis de ambiente, de um arquivo `.env` ou de
    valores padrão definidos no código.

    Isso resolve um problema comum em projetos: evitar espalhar senhas, chaves
    de API e caminhos importantes pelo código-fonte. Em vez disso, essas
    informações ficam organizadas em um único lugar, com validação automática e
    tipos corretos.

    Para quem está começando, pense nele como uma "caixa de configurações" da
    aplicação. Se uma variável estiver faltando ou vier no formato errado, o
    Pydantic ajuda a detectar isso mais cedo, antes de o programa quebrar em
    tempo de execução.
    """
    APP_NAME: str = "Mural Inteligente UNICAP"
    GROQ_API_KEY: str = ""
    DATA_PATH: Path = Path(__file__).parent.parent.parent / "data" / "data.json"
    MODEL_NAME: str = "Salesforce/blip-image-captioning-base"
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
