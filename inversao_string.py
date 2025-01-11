def inverter_string(s):
    caracteres = list(s)
    invertida = []
    for i in range(len(caracteres) - 1, -1, -1):
        invertida.append(caracteres[i])
    return ''.join(invertida)

# String a ser invertida
string = input("Digite uma string: ")
print(f"String invertida: {inverter_string(string)}")
