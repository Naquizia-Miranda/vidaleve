import firebase_admin
from firebase_admin import credentials, firestore

# 🔹 Caminho fixo direto para o arquivo JSON
cred_path = r"C:\Users\NAQUI\vidaleve\firebase_credentials.json"

try:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    print("✅ Firebase inicializado com sucesso!")
except Exception as e:
    print("❌ Erro ao inicializar o Firebase:", e)

import firebase_admin
from firebase_admin import credentials, firestore

# 🔹 Caminho fixo direto para o arquivo JSON
cred_path = r"C:\Users\NAQUI\vidaleve\firebase_credentials.json"

# Inicializa o app Firebase (se ainda não estiver inicializado)
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    print("✅ Firebase inicializado com sucesso!")

# 🔹 Cria a conexão com o Firestore
db = firestore.client()
