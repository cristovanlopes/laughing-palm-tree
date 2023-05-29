import random

minimo = 1
maximo = 10
quantidade_numeros = 5
tupla=(1,3)
tupla_numeros_aleatorios = tuple(random.randint(minimo, maximo) for _ in range(quantidade_numeros))

print("Tupla de números aleatórios:", tupla_numeros_aleatorios)

menor_numero = min(tupla_numeros_aleatorios)
maior_numero = max(tupla_numeros_aleatorios)

print("Menor número:", menor_numero)
print("Maior número:", maior_numero)
