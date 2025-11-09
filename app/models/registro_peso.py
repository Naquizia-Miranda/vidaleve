from datetime import datetime
from pydantic import Field
from .base import FirebaseModel

class RegistroPeso(FirebaseModel):
    usuario_id: str
    data_registro: datetime = Field(default_factory=datetime.now)
    peso_kg: float = Field(..., gt=0)
