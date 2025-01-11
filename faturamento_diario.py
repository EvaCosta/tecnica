import json

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

valores = [d["valor"] for d in faturamento if d["valor"] > 0]
media_mensal = sum(valores) / len(valores)
menor_valor = min(valores)
maior_valor = max(valores)
dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
