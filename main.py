from calculations import calcular_peso_liquido
from report import exibir_relatorio
from ui import ler_carga, mostrar_carga
from validation import validar_carga

cargas = []


def registrar_carga():
    try:
        carga = ler_carga()
        validar_carga(carga)
    except ValueError as erro:
        print(f"Não foi possível registrar: {erro}")
        return

    carga["peso_liquido"] = calcular_peso_liquido(
        carga["peso_bruto"], carga["peso_tara"]
    )
    cargas.append(carga)
    print("Carga registrada.")
    mostrar_carga(carga)


def main():
    while True:
        print("\nBIOTRACK — Recebimento de biomassa")
        print("1. Registrar carga")
        print("2. Ver relatório")
        print("3. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            registrar_carga()
        elif opcao == "2":
            exibir_relatorio(cargas)
        elif opcao == "3":
            print("Até logo!")
            break
        else:
            print("Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
