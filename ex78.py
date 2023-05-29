lista = [input("Digite um número: "),
         ("Digite um número: "),
         input("Digite um número: "),
         input("Digite um número: "),
         input("Digite um número: ")]
maior = max(lista)
menor = min(lista)
posicao = lista.index(maior)
posicaoMin = lista.index(menor)

print(f'O maior ', maior, " posicao ", posicao)
print(f'O maior ', menor, " posicao ", posicaoMin)