from datetime import datetime
from typing import Optional
from pydantic import Field
from .base import FirebaseModel

class RegistroAlimentacao(FirebaseModel):
    usuario_id: str
    data_registro: datetime = Field(default_factory=datetime.now)
    alimento: str
    calorias: int = Field(..., gt=0)
    proteinas_g: Optional[float] = Field(None, ge=0)
    carboidratos_g: Optional[float] = Field(None, ge=0)
    gorduras_g: Optional[float] = Field(None, ge=0)
