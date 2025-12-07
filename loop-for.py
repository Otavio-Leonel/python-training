# O "FOR" no Python não funciona do mesmo jeito que em outras lingguagens tipo Java e C

# range(valor inicial, valor final)


# nome = 'Otavio Leonel'
# lista = [1, 3, 5, 7, 9]
# numeros = range(1, 10)

# for letra in nome:
#     print(letra)

# for numero in nome:
#     print(numero)

# for numero in range(1, 10):
#     print(numero)

# frutas = ["maçã", "banana", "uva"]

# for fruta in frutas:
#     print(fruta)

quantidade = int(input("Quantas vezes o loop vai rodar?"))
soma = 0

# for n in range(1, quantidade):
#     print('Imprimir', n)

for n in range(1, quantidade+1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma = soma + num
print(f'A soma é {soma}')