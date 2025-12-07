# Existem dois metodos de calcular a raiz em python: usando a biblioteca Math ou utilizando o simbolo de pontenciação que é (**)

import math

print('Vamos calcular a raiz de numeros positivos')

numero = int(input('Digite um numero: '))

if numero > 0:
    # raiz = numero ** 0.5 jeito sem a biblioteca
    raiz = math.sqrt(numero)
    print('A raiz de seu numero é', raiz)
else:
    print('favor digitar um numero valido')