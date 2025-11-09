from app.services.servico_tmb import calcular_tmb
from app.services.servico_meta import estimar_tempo_para_meta
from app.services.servico_relatorio import gerar_relatorio_semanal

class ServicoGerenciamentoPeso:
    def __init__(self, repo_usuario, repo_registro):
        self.repo_usuario = repo_usuario
        self.repo_registro = repo_registro

    def calcular_tmb(self, usuario, peso_kg):
        return calcular_tmb(usuario, peso_kg)

    def estimar_tempo_para_meta(self, usuario_id):
        return estimar_tempo_para_meta(self.repo_usuario, self.repo_registro, usuario_id)

    def relatorio_semanal_progresso(self, usuario_id, data_fim_semana):
        return gerar_relatorio_semanal(self.repo_usuario, self.repo_registro, usuario_id, data_fim_semana)
