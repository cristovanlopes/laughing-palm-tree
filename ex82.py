principalList = []
lista_par = []
lista_impar = []


while True:
    n = int(input('Digite um numero: '))
    principalList.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)

    cont =  str(input('Quer continuar? ')).upper()[0]
    if 'N' in cont:
        break
print('=-'*30)
print(f'A lista total: {principalList}')
print(f'par: {lista_par}')
print(f'impar: {lista_impar}')