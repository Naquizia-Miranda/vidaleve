from typing import Optional, Dict, Any
from pydantic import BaseModel

class FirebaseModel(BaseModel):
    id: Optional[str] = None  # Firebase document ID

    def to_dict(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        if "id" in data:
            del data["id"]
        return data

    @classmethod
    def from_dict(cls, doc_id, source):
        """Cria um objeto da classe a partir de um dicionário do Firestore."""
        data = dict(source)
        data.pop("id", None)
        return cls(id=doc_id, **data)
