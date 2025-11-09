from datetime import date, datetime
from typing import List
from app.firebase_config import db
from app.models import RegistroPeso, RegistroAlimentacao, RegistroAtividade, RegistroAgua
from app.repositorios.base import RepositorioBase

class RepositorioRegistro(RepositorioBase):
    def __init__(self):
        super().__init__("registros_peso", RegistroPeso)

    def obter_registros_por_usuario(self, id_usuario: str) -> List[RegistroPeso]:
        query = self.collection.where("id_usuario", "==", id_usuario).stream()
        return [RegistroPeso.from_dict(doc.id, doc.to_dict()) for doc in query]

    # ==============================
    # Métodos de criação
    # ==============================
    def criar_registro_peso(self, registro: RegistroPeso):
        return self._criar_registro_generico("registros_peso", registro)

    def criar_registro_alimentacao(self, registro: RegistroAlimentacao):
        return self._criar_registro_generico("registros_alimentacao", registro)

    def criar_registro_atividade(self, registro: RegistroAtividade):
        return self._criar_registro_generico("registros_atividade", registro)

    def criar_registro_agua(self, registro: RegistroAgua):
        return self._criar_registro_generico("registros_agua", registro)

    # ==============================
    # Auxiliar genérico
    # ==============================
    def _criar_registro_generico(self, nome_colecao: str, registro):
        registro_data = registro.to_dict() if hasattr(registro, "to_dict") else registro.__dict__
        for key, value in registro_data.items():
            if isinstance(value, date) and not isinstance(value, datetime):
                registro_data[key] = datetime.combine(value, datetime.min.time())
        _, doc_ref = db.collection(nome_colecao).add(registro_data)
        registro.id = doc_ref.id
        return registro
