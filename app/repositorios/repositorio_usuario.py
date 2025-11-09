from google.cloud import firestore

class RepositorioUsuario:
    """Repositório responsável por gerenciar os dados dos usuários no Firestore."""

    def __init__(self):
        self.db = firestore.Client()
        self.colecao = self.db.collection("usuarios")

    # ------------------------------------------------------------
    # 🔹 Criar ou atualizar usuário
    # ------------------------------------------------------------
    def criar_ou_atualizar_usuario(self, usuario_dados):
        """Cria ou atualiza um usuário com base no email."""
        try:
            email = usuario_dados.get("email")

            # Procura usuário existente com esse e-mail
            query = self.colecao.where("email", "==", email).limit(1).stream()
            doc_existente = next(query, None)

            if doc_existente:
                # Atualiza usuário existente
                doc_ref = self.colecao.document(doc_existente.id)
                doc_ref.update(usuario_dados)
                usuario_dados["id"] = doc_existente.id
                print(f"Usuário existente atualizado: {usuario_dados}")
                return usuario_dados
            else:
                # Cria novo usuário
                doc_ref = self.colecao.add(usuario_dados)[1]
                usuario_dados["id"] = doc_ref.id
                print(f"Usuário criado com sucesso: {usuario_dados}")
                return usuario_dados
        except Exception as e:
            print(f"❌ Erro ao criar ou atualizar usuário: {e}")
            return None

    # ------------------------------------------------------------
    # 🔹 Obter usuário por e-mail
    # ------------------------------------------------------------
    def obter_usuario_por_email(self, email):
        """Obtém um usuário pelo e-mail."""
        try:
            query = self.colecao.where("email", "==", email).limit(1).stream()
            for doc in query:
                dados = doc.to_dict()
                dados["id"] = doc.id
                return dados
            print(f"⚠️ Nenhum usuário encontrado com o e-mail {email}.")
            return None
        except Exception as e:
            print(f"❌ Erro ao obter usuário por e-mail: {e}")
            return None

    # ------------------------------------------------------------
    # 🔹 Obter usuário por ID (novo método)
    # ------------------------------------------------------------
    def obter_usuario_por_id(self, usuario_id):
        """Obtém um usuário pelo ID do documento."""
        try:
            doc_ref = self.colecao.document(usuario_id)
            doc = doc_ref.get()
            if doc.exists:
                dados = doc.to_dict()
                dados["id"] = doc.id
                return dados
            else:
                print(f"⚠️ Usuário com ID {usuario_id} não encontrado.")
                return None
        except Exception as e:
            print(f"❌ Erro ao obter usuário por ID: {e}")
            return None

    # ------------------------------------------------------------
    # 🔹 Listar todos os usuários
    # ------------------------------------------------------------
    def listar_usuarios(self):
        """Retorna uma lista com todos os usuários cadastrados."""
        try:
            usuarios = []
            for doc in self.colecao.stream():
                dados = doc.to_dict()
                dados["id"] = doc.id
                usuarios.append(dados)
            return usuarios
        except Exception as e:
            print(f"❌ Erro ao listar usuários: {e}")
            return []

    # ------------------------------------------------------------
    # 🔹 Excluir usuário
    # ------------------------------------------------------------
    def excluir_usuario(self, usuario_id):
        """Exclui um usuário do Firestore pelo ID."""
        try:
            self.colecao.document(usuario_id).delete()
            print(f"✅ Usuário {usuario_id} excluído com sucesso.")
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir usuário: {e}")
            return False
