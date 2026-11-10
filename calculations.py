def calcular_peso_liquido(peso_bruto, peso_tara):
    """Calcula o peso líquido em toneladas a partir do bruto e da tara."""
    if peso_bruto < 0 or peso_tara < 0:
        raise ValueError("Os pesos não podem ser negativos.")
    if peso_bruto < peso_tara:
        raise ValueError("O peso bruto não pode ser menor que a tara.")
    return round(peso_bruto - peso_tara, 3)
