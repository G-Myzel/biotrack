def exibir_relatorio(cargas):
    if not cargas:
        print("Ainda não há cargas registradas.")
        return

    peso_total = sum(carga["peso_liquido"] for carga in cargas)
    umidade_media = sum(carga["umidade"] for carga in cargas) / len(cargas)
    print(f"\nCargas registradas: {len(cargas)}")
    print(f"Peso líquido total: {peso_total:.3f} t")
    print(f"Umidade média: {umidade_media:.1f}%")
    print("\nDetalhes:")
    for carga in cargas:
        print(
            f"- {carga['data']} | {carga['placa']} | "
            f"{carga['peso_liquido']:.3f} t | {carga['umidade']:.1f}%"
        )
