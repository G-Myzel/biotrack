import math


def ler_numero(valor, nome):
    try:
        numero = float(str(valor).strip().replace(",", "."))
    except ValueError as erro:
        raise ValueError(f"{nome} precisa ser um número.") from erro
    if not math.isfinite(numero):
        raise ValueError(f"{nome} precisa ser um número finito.")
    return numero


def validar_carga(carga):
    placa = str(carga.get("placa", "")).strip().upper()
    if not placa:
        raise ValueError("Informe a placa do veículo.")
    carga["placa"] = placa

    for campo, rotulo in (
        ("peso_bruto", "Peso bruto"),
        ("peso_tara", "Peso da tara"),
        ("umidade", "Umidade"),
    ):
        carga[campo] = ler_numero(carga.get(campo), rotulo)

    if carga["peso_bruto"] <= 0 or carga["peso_tara"] < 0:
        raise ValueError("O peso bruto deve ser positivo e a tara não pode ser negativa.")
    if carga["peso_bruto"] < carga["peso_tara"]:
        raise ValueError("O peso bruto não pode ser menor que a tara.")
    if not 0 <= carga["umidade"] <= 100:
        raise ValueError("A umidade deve estar entre 0% e 100%.")
