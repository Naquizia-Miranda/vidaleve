from datetime import date, datetime
from pydantic import Field
from .base import FirebaseModel

class Usuario(FirebaseModel):
    nome: str
    email: str
    data_nascimento: date
    sexo: str  # 'M' ou 'F'
    altura_cm: float = Field(..., gt=0)

    def to_dict(self):
        data = self.model_dump()
        for key, value in data.items():
            if isinstance(value, date) and not isinstance(value, datetime):
                data[key] = datetime.combine(value, datetime.min.time())
        return data
