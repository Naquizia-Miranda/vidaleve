def estimar_tempo_para_meta(repo_usuario, repo_registro, usuario_id):
    usuario = repo_usuario.obter_usuario_por_id(usuario_id)
    meta = repo_usuario.obter_meta_por_usuario_id(usuario_id)
    ultimo_peso = repo_registro.obter_ultimo_registro_peso(usuario_id)

    if not all([usuario, meta, ultimo_peso]):
        return None

    peso_atual = ultimo_peso.peso_kg
    peso_alvo = meta.peso_alvo_kg

    if peso_atual == peso_alvo:
        return {"mensagem": "Peso atual já é o peso alvo!", "dias_restantes": 0, "semanas_restantes": 0}

    from app.services.servico_tmb import calcular_tmb
    calorias_diarias_estimadas = meta.calorias_alvo_diarias or calcular_tmb(usuario, peso_atual)

    balanco_calorico_diario = calcular_tmb(usuario, peso_atual) - calorias_diarias_estimadas
    if balanco_calorico_diario == 0:
        return {"mensagem": "Balanço calórico diário zero. Não há mudança esperada.", "dias_restantes": None}

    calorias_para_meta = (peso_atual - peso_alvo) * 7700

    if (calorias_para_meta > 0 and balanco_calorico_diario > 0) or (calorias_para_meta < 0 and balanco_calorico_diario < 0):
        return {"mensagem": "A meta calórica não favorece o objetivo.", "dias_restantes": None}

    dias_restantes = abs(calorias_para_meta / balanco_calorico_diario)
    return {
        "mensagem": "Estimativa calculada com sucesso.",
        "dias_restantes": round(dias_restantes),
        "semanas_restantes": round(dias_restantes / 7, 2)
    }
