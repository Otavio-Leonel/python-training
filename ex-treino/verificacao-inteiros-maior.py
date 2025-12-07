print('Digite dois valores e vamos ver qual o maior')

numero1 = int(input('Digite o Primeiro numero: '))
numero2 = int(input('Digite o Segundo numero: '))

if numero1 > numero2:
    print('o primeiro numero é maior')
elif numero1 == numero2:
    print('os numeros são iguais')
else:
    print('o segundo numero é maior')