def is_fibonacci(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} NÃO pertence à sequência de Fibonacci."

# Número a ser testado
numero = int(input("Digite um número: "))
print(is_fibonacci(numero))
