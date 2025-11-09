from datetime import timedelta

def gerar_relatorio_semanal(repo_usuario, repo_registro, usuario_id, data_fim_semana):
    usuario = repo_usuario.obter_usuario_por_id(usuario_id)
    if not usuario:
        return None

    data_inicio_semana = data_fim_semana - timedelta(days=6)
    registros_peso = repo_registro.obter_registros_peso_periodo(usuario_id, data_inicio_semana, data_fim_semana)

    perda_peso = 0.0
    if len(registros_peso) >= 2:
        registros_peso.sort(key=lambda x: x.data_registro)
        perda_peso = registros_peso[0].peso_kg - registros_peso[-1].peso_kg

    total_calorias_consumidas = 0
    total_calorias_queimadas = 0
    dias_com_registros = set()

    for i in range(7):
        data_atual = data_inicio_semana + timedelta(days=i)
        alimentos = repo_registro.obter_registros_alimentacao_por_usuario_e_data(usuario_id, data_atual)
        atividades = repo_registro.obter_registros_atividade_por_usuario_e_data(usuario_id, data_atual)

        if alimentos or atividades:
            dias_com_registros.add(data_atual)

        total_calorias_consumidas += sum(r.calorias for r in alimentos)
        total_calorias_queimadas += sum(r.calorias_queimadas for r in atividades)

    num_dias = len(dias_com_registros)
    balanco_medio = 0.0
    if num_dias > 0:
        from app.services.servico_tmb import calcular_tmb
        peso_para_tmb = registros_peso[-1].peso_kg if registros_peso else usuario.altura_cm
        tmb = calcular_tmb(usuario, peso_para_tmb)
        balanco_medio = (total_calorias_consumidas - total_calorias_queimadas - (tmb * num_dias)) / num_dias

    meta_agua = repo_usuario.obter_meta_por_usuario_id(usuario_id)
    porcentagem_agua = 0.0
    if meta_agua and meta_agua.agua_alvo_ml:
        total_agua = 0
        for i in range(7):
            data_atual = data_inicio_semana + timedelta(days=i)
            registros = repo_registro.obter_registros_agua_por_usuario_e_data(usuario_id, data_atual)
            total_agua += sum(r.quantidade_ml for r in registros)

        porcentagem_agua = (total_agua / (meta_agua.agua_alvo_ml * 7)) * 100

    return {
        "data_inicio_semana": data_inicio_semana.isoformat(),
        "data_fim_semana": data_fim_semana.isoformat(),
        "perda_peso_semanal_kg": round(perda_peso, 2),
        "balanco_calorico_medio_diario": round(balanco_medio, 2),
        "porcentagem_meta_agua_atingida": round(porcentagem_agua, 2),
    }
