numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = 30

while numero <0 or numero > 20:
     print("Escolha um numero entre 0 e 20 burrao")
     numero = int(input())
     if numero >= 0 and numero <= 20:
          print(f'Voce escolheu o numero: {numeros_por_extenso[numero]}')
          break

     print('Entre 0 e 20 burrão!!!!!')