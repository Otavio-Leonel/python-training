# Para verificar se o numero é par ou impar podemos utilizar o operador módulo (%) que me retorna o valor do resto de uma divisão

print('Vamos ver se esse numero é par ou impar')

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print('seu numero é par')
else:
    print('seu numero é impar')