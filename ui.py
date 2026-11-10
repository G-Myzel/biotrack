from datetime import datetime

from validation import ler_numero


def pedir_numero(pergunta, nome):
    while True:
        valor = input(pergunta).strip()
        try:
            return ler_numero(valor, nome)
        except ValueError as erro:
            print(erro)


def ler_carga():
    placa = input("Placa do veículo: ").strip()
    peso_bruto = pedir_numero("Peso bruto (t): ", "Peso bruto")
    peso_tara = pedir_numero("Peso da tara (t): ", "Peso da tara")
    umidade = pedir_numero("Umidade da biomassa (%): ", "Umidade")
    return {
        "placa": placa,
        "peso_bruto": peso_bruto,
        "peso_tara": peso_tara,
        "umidade": umidade,
        "data": datetime.now().date().isoformat(),
    }


def mostrar_carga(carga):
    print(
        f"{carga['data']} | {carga['placa']} | "
        f"Líquido: {carga['peso_liquido']:.3f} t | "
        f"Umidade: {carga['umidade']:.1f}%"
    )
