from datetime import datetime
from pydantic import Field
from .base import FirebaseModel

class RegistroAtividade(FirebaseModel):
    usuario_id: str
    data_registro: datetime = Field(default_factory=datetime.now)
    atividade: str
    duracao_minutos: int = Field(..., gt=0)
    calorias_queimadas: int = Field(..., gt=0)
