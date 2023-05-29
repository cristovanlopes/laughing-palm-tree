lista = []
verificar = 10

while verificar != 20:
    n = int(input('DIGITE UM VALOR: '))
    if n not in lista:
        lista.append(n)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor repetido')

    cont = int(input('QUER CONTINUAR? [0/20]'))
    if cont == 20:
        break
print(lista)