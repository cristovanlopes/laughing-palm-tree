lista = []

for i in range(5):
    num = int(input("Digite um número: "))

    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print("Os números digitados em ordem são: ", lista)