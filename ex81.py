num = []
while True:
    num.append((int(input('Digite um valor'))))
    cont = str(input('Quer continuar? ')).upper()[0]
    if cont in 'N':
        break
print(f'Foram digitados {len(num)} vezes')
num.sort(reverse=True)
print(f'A lista de forma decrescente: {num} ')
if 5 in num:
    print('sim está na lista caralho')
else:
    print('Seu burro nao ta na lista o 5')