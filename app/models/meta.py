from datetime import date
from typing import Optional
from pydantic import Field
from .base import FirebaseModel

class Meta(FirebaseModel):
    usuario_id: str
    peso_alvo_kg: float = Field(..., gt=0)
    data_inicio: date
    data_alvo: date
    calorias_alvo_diarias: Optional[int] = None
    agua_alvo_ml: Optional[int] = None
