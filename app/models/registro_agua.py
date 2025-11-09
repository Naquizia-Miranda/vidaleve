from datetime import datetime
from pydantic import Field
from .base import FirebaseModel

class RegistroAgua(FirebaseModel):
    usuario_id: str
    data_registro: datetime = Field(default_factory=datetime.now)
    quantidade_ml: int = Field(..., gt=0)
