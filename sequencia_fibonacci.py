import math

def is_fibonacci(num):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    cond1 = is_perfect_square(5 * num**2 + 4)
    cond2 = is_perfect_square(5 * num**2 - 4)

    if cond1 or cond2:
        return f"{num} pertence à sequência de Fibonacci."
    return f"{num} NÃO pertence à sequência de Fibonacci."

# Entrada do usuário
numero = int(input("Digite um número: "))
print(is_fibonacci(numero))
