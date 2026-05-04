from pydantic import BaseModel
from typing import Optional


class InformativoSchema(BaseModel):
    """O BaseModel do Pydantic é a classe base usada para criar modelos de dados.

    Ele faz validação automática e conversão de tipos, ajudando a garantir que os
    dados recebidos ou enviados pela API estejam no formato correto.

    Na prática, essa classe funciona de forma parecida com um DTO
    (Data Transfer Object) em outras linguagens, porque define a estrutura dos
    dados que a aplicação vai manipular.
    """
    id: Optional[str] = None
    titulo: str
    categoria: str
    resumo: str
    relevancia: str
    