import json

def calcular_faturamento(faturamento):
    valores = [d["valor"] for d in faturamento if d["valor"] > 0]
    if not valores:
        return "Nenhum faturamento válido encontrado."
    
    media_mensal = sum(valores) / len(valores)
    menor_valor = min(valores)
    maior_valor = max(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    return {
        "menor_valor": menor_valor,
        "maior_valor": maior_valor,
        "dias_acima_media": dias_acima_media,
    }

# Simulação do JSON de faturamento
faturamento_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0}
]
'''

faturamento = json.loads(faturamento_json)
resultado = calcular_faturamento(faturamento)

print(f"Menor valor de faturamento: {resultado['menor_valor']:.2f}")
print(f"Maior valor de faturamento: {resultado['maior_valor']:.2f}")
print(f"Dias com faturamento acima da média: {resultado['dias_acima_media']}")
