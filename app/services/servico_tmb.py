from datetime import date

def calcular_tmb(usuario, peso_kg):
    """Calcula a Taxa Metabólica Basal (TMB) usando a fórmula de Mifflin-St Jeor."""
    idade = date.today().year - usuario.data_nascimento.year

    if usuario.sexo == 'M':
        return (10 * peso_kg) + (6.25 * usuario.altura_cm) - (5 * idade) + 5
    elif usuario.sexo == 'F':
        return (10 * peso_kg) + (6.25 * usuario.altura_cm) - (5 * idade) - 161
    else:
        raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
