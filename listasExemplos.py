# parte 1
valor = input("Digite um número: ")

if valor == "1":
    num = [2, 5, 9, 1]
    num[2] = 3
    num.append(7)
    num.sort(reverse=True)
    num.insert(2, 2)
    if 4 in num:
        num.remove(4)
    else:
        print('Não achei o número 4')
    print(num)
    print(f'Essa lista tem {len(num)} elementos.')
    breakpoint();



elif valor == "2":
    valores = []
    valores.append(5)
    valores.append(9)
    valores.append(4)
    for c, v in enumerate(valores):
        print(f'Na posição {c} encontrei p valor {v}!')
        print('Cheguei ao final da lista.')




else:
    print("Você não digitou nem o número 1 nem o número 2.")
    # parte 3
    valores = list()
    for cont in range(0, 5):
        valores.append(int(input('Digite um valor: ')))
    for c, v in enumerate(valores):
        print(f'Na posição  {c} encontrei o valor {v}!')
    print('Cheguei ao final da lista.')





