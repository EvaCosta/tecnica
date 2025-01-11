def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    if total == 0:
        return {}
    
    return {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

def exibir_percentuais(percentuais):
    print("Percentual de faturamento por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

# Faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamento)
exibir_percentuais(percentuais)
