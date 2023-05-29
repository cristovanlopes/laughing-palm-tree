n = (int(input(f'informe numero ')), int(input(f'Informe numero ')), int(input(f'Informe numero ')), int(input(f'Informe numero ')))
if 3 in n:
    print(f'O valor 3 foi digitado na posição {n.index(3)}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
for cont in n:
    if cont % 2 == 0:
        print(cont, end=' ')