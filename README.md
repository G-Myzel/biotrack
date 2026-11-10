# BioTrack

Exercício de Python para registrar o recebimento de cargas de biomassa e praticar validação, cálculos e separação do programa em módulos.

## O que o programa faz

- Registra placa, peso bruto, tara e umidade da carga.
- Valida os pesos e a umidade informados.
- Calcula o peso líquido como peso bruto menos tara.
- Mostra um resumo das cargas registradas durante a execução.

O peso é informado em toneladas. O sistema apenas registra a umidade; não aplica desconto ou correção sobre o peso, pois isso dependeria de uma regra definida pelo projeto.

## Como executar

Requer Python 3.10 ou mais recente:

```bash
python main.py
```

Os dados ficam em memória e são perdidos ao fechar o programa.
