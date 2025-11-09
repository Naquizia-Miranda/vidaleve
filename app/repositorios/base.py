from typing import List, Optional, Type, TypeVar, Dict, Any
from datetime import date, datetime
from google.cloud.firestore_v1.collection import CollectionReference
from app.firebase_config import db
from app.modelos import FirebaseModel

T = TypeVar("T", bound=FirebaseModel)

class RepositorioBase:
    def __init__(self, collection_name: str, model_class: Type[T]):
        self.collection: CollectionReference = db.collection(collection_name)
        self.model_class = model_class

    def criar(self, modelo: T) -> Optional[T]:
        data = modelo.to_dict() if hasattr(modelo, "to_dict") else modelo.__dict__
        for key, value in data.items():
            if isinstance(value, date) and not isinstance(value, datetime):
                data[key] = datetime.combine(value, datetime.min.time())
        _, doc_ref = self.collection.add(data)
        modelo.id = doc_ref.id
        return modelo

    def obter_por_id(self, doc_id: str) -> Optional[T]:
        doc = self.collection.document(doc_id).get()
        if doc.exists:
            return self.model_class.from_dict(doc.id, doc.to_dict())
        return None

    def atualizar(self, doc_id: str, dados: Dict[str, Any]) -> Optional[T]:
        doc_ref = self.collection.document(doc_id)
        doc_ref.update(dados)
        return self.obter_por_id(doc_id)

    def deletar(self, doc_id: str) -> bool:
        self.collection.document(doc_id).delete()
        return True

    def obter_todos(self) -> List[T]:
        docs = self.collection.stream()
        return [self.model_class.from_dict(doc.id, doc.to_dict()) for doc in docs]
