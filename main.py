from datetime import date, datetime, timedelta
from app.services.servico_gerenciamento_peso import ServicoGerenciamentoPeso

from app.Repositorios.repositorio_registro import RepositorioRegistro
from app.firebase_config import db # Importar db para garantir a inicialização
from app.models import Usuario, Meta, RegistroPeso, RegistroAlimentacao, RegistroAtividade, RegistroAgua
from app.repositorios import RepositorioUsuario, RepositorioRegistro
from app.repositorios import (
    RepositorioUsuario,
    RepositorioMeta,
    RepositorioRegistroPeso
)
def main():
    print("Iniciando a aplicação de Gerenciamento de Peso com Firebase...")

    # 1. Inicializar repositórios e serviços
    if db is None:
        print("Erro: Firebase não inicializado. Verifique as credenciais.")
        return

    repositorio_usuario = RepositorioUsuario()
    repositorio_registro = RepositorioRegistro()
    servico_gerenciamento = ServicoGerenciamentoPeso(repositorio_usuario, repositorio_registro)

    # 2. Criar um usuário
    print("\n--- Criando Usuário ---")
    novo_usuario_data = Usuario(
        nome="Ana Silva Firebase",
        email="ana.silva.firebase@example.com",
        data_nascimento=date(1990, 5, 15),
        sexo="F",
        altura_cm=165.0
    )
    
    usuario_criado = repositorio_usuario.obter_usuario_por_email(novo_usuario_data.email)
    if not usuario_criado:
        usuario_criado = repositorio_usuario.criar_usuario(novo_usuario_data)
        print(f"Usuário criado: {usuario_criado.model_dump_json(indent=2)}")
    else:
        print(f"Usuário existente recuperado: {usuario_criado.model_dump_json(indent=2)}")

    if not usuario_criado or not usuario_criado.id:
        print("Não foi possível obter o ID do usuário. Encerrando.")
        return
    user_id = usuario_criado.id

    # 3. Criar uma meta para o usuário
    print("\n--- Criando Meta ---")
    meta_existente = repositorio_usuario.obter_meta_por_usuario_id(user_id)
    if not meta_existente:
        nova_meta_data = Meta(
            usuario_id=user_id,
            peso_alvo_kg=60.0,
            data_inicio=date(2023, 10, 1),
            data_alvo=date(2024, 3, 1),
            calorias_alvo_diarias=1500,
            agua_alvo_ml=2500
        )
        meta_criada = repositorio_usuario.criar_meta(nova_meta_data)
        if meta_criada:
            print(f"Meta criada: {meta_criada.model_dump_json(indent=2)}")
    else:
        print(f"Meta existente recuperada: {meta_existente.model_dump_json(indent=2)}")

    # 4. Adicionar registros de peso
    print("\n--- Adicionando Registros de Peso ---")
    peso1 = RegistroPeso(usuario_id=user_id, data_registro=datetime(2023, 10, 1, 8, 0, 0), peso_kg=70.0)
    peso2 = RegistroPeso(usuario_id=user_id, data_registro=datetime(2023, 10, 8, 8, 0, 0), peso_kg=69.5)
    peso3 = RegistroPeso(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 8, 0, 0), peso_kg=69.0)

    repositorio_registro.criar_registro_peso(peso1)
    repositorio_registro.criar_registro_peso(peso2)
    repositorio_registro.criar_registro_peso(peso3)
    print("Registros de peso adicionados.")

    # 5. Adicionar registros de alimentação
    print("\n--- Adicionando Registros de Alimentação ---")
    alim1 = RegistroAlimentacao(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 9, 0, 0), alimento="Pão integral", calorias=200)
    alim2 = RegistroAlimentacao(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 13, 0, 0), alimento="Salada com frango", calorias=400)
    alim3 = RegistroAlimentacao(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 20, 0, 0), alimento="Sopa de legumes", calorias=300)

    repositorio_registro.criar_registro_alimentacao(alim1)
    repositorio_registro.criar_registro_alimentacao(alim2)
    repositorio_registro.criar_registro_alimentacao(alim3)
    print("Registros de alimentação adicionados.")

    # 6. Adicionar registros de atividade
    print("\n--- Adicionando Registros de Atividade ---")
    ativ1 = RegistroAtividade(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 18, 0, 0), atividade="Caminhada", duracao_minutos=60, calorias_queimadas=300)
    repositorio_registro.criar_registro_atividade(ativ1)
    print("Registros de atividade adicionados.")

    # 7. Adicionar registros de água
    print("\n--- Adicionando Registros de Água ---")
    agua1 = RegistroAgua(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 10, 0, 0), quantidade_ml=500)
    agua2 = RegistroAgua(usuario_id=user_id, data_registro=datetime(2023, 10, 15, 14, 0, 0), quantidade_ml=750)
    repositorio_registro.criar_registro_agua(agua1)
    repositorio_registro.criar_registro_agua(agua2)
    print("Registros de água adicionados.")

    # 8. Calcular TMB
    print("\n--- Calculando TMB ---")
    if usuario_criado and peso3:
        tmb = servico_gerenciamento.calcular_tmb(usuario_criado, peso3.peso_kg)
        print(f"TMB para {usuario_criado.nome} com peso de {peso3.peso_kg}kg: {tmb:.2f} kcal/dia")
    else:
        print("Não foi possível calcular TMB. Usuário ou peso não encontrados.")

    # 9. Estimar tempo para alcançar a meta
    print("\n--- Estimando Tempo para Meta ---")
    estimativa = servico_gerenciamento.estimar_tempo_para_meta(user_id)
    if estimativa:
        print(f"Estimativa para a meta: {estimativa}")
    else:
        print("Não foi possível estimar o tempo para a meta. Dados insuficientes.")

    # 10. Gerar Relatório Semanal de Progresso
    print("\n--- Gerando Relatório Semanal de Progresso ---")
    data_fim_relatorio = date(2023, 10, 15) # Exemplo: fim da semana de 9 a 15 de Out
    relatorio = servico_gerenciamento.relatorio_semanal_progresso(user_id, data_fim_relatorio)
    if relatorio:
        print(f"Relatório Semanal ({data_fim_relatorio - timedelta(days=6)} a {data_fim_relatorio}): {relatorio}")
    else:
        print("Não foi possível gerar o relatório semanal. Dados insuficientes.")

    print("\nDemonstração concluída.")

if __name__ == "__main__":
    main()

