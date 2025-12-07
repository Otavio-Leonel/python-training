# listas em Python estão sempre entre []

lista1 = [1, 8, 3, 545, 6, 10, 8]
lista2 = ['a', 'd', 'f', 'g', 'e', 'dv']
lista3 = []
lista4 = list(range(11))
lista5 = list('Terraria Calamity')

''' Verificar se um valor está dentro de uma lista

if 8 in lista4:
    print('Achei o numero')
else:
    print('Não achei o numero')

'''

''' Outro Tipo de verificação

num = 10
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')
'''

''' Ordenar listas

lista1.sort()
print(lista1)
'''

''' Contar numero de ocorrencias de um valor em uma lista

print(lista1.count(8))
print(lista5.count('a'))
'''

''' Adicionar elementos em uma lista, um elemento por vez usando o "append"

print(lista1)
lista1.append(36)
print(lista1)
'''

''' Adicionar mais de um elemento a uma lista 

print(lista1)
lista1.extend([6, 8, 10, 506])
print(lista1)

'''

''' Adicionar um valor e informar a posição no indice

lista1.insert(2, 'Novo Valor')
print(lista1)
'''

''' Mesclar listas

lista6 = lista1 + lista2
print(lista6)

# Ou

lista1.extend(lista2)
print(lista1)

'''

''' Inverter exibição da lista
lista1.reverse()
print(lista1)

# Ou

print(lista1[::-1])
'''

''' Copiar uma lista para outra

lista6 = lista2.copy()
print(lista6)
'''

''' Exibi o tamanho de uma lista, vulgo quantidade de itens presentes 

print(len(lista1))
'''

''' Remove o ultimo elemento de uma lista

print(lista5)
lista5.pop()
print(lista5)
'''

''' Remove elementos pelo indice deles

print(lista5)
lista5.pop(2)
print(lista5)
'''

''' Remover todos elementos de uma lista

print(lista5)
lista5.clear()
print(lista5)
'''

''' Repetir elementos de uma lista

print(lista1)
lista1 = lista1 * 3
print(lista1)
'''

''' Converter String em lista, faz a lista de acordo com os espaços da string

game = "terraria calamity"
print(game)
game = game.split()
print(game)

# Define o separador da string caso não seja espaço

game = "terraria,calamity"
print(game)
game = game.split(',')
print(game)

'''

''' Converter Lista em String

lista6 = ["Terraria", "Calamity", "Top1"]
print(lista6)

game = ' '.join(lista6)
print(game)

'''

''' Lista em Python aceita qualquer tipo de dado

lista6 = [1, 25, "f", "otavio", True, [1,2], 16846846846]
print(lista6)
'''

''' Iterar itens de uma lista (for)

for elemento in lista1:
    print(elemento)
'''

''' Iterar itens de uma lista (While) e listar com (for)

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto em seu carrinho ou digite (sair) para finalizar compra: ")
    produto = input()
    if produto != ' sair':
        carrinho.append(produto)

print(carrinho)


for produto in carrinho:
    print(produto)
'''

''' Lista com variaveis

numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
'''

''' Verificar elemento guardado em determinada posição de uma lista
frutas = ['uva', 'maça', 'banana', 'Morango']
print(frutas[0])

#  ou em ordem inversa
frutas = ['uva', 'maça', 'banana', 'Morango']
print(frutas[-1])
'''

''' Exibir elementos da lista com while ou for

frutas = ['uva', 'maça', 'banana', 'Morango']

for fruta in frutas:
    print(fruta)

indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice = indice + 1

'''

''' Gerar um indice em um for

frutas = ['uva', 'maça', 'banana', 'Morango']

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

'''

''' Encontrar o indice de um elemento em minha lista e caso tenha repetido vai mostrar a posição apenas do primeiro da lista

frutas = ['uva', 'maça', 'banana', 'Morango', 'abacaxi', 'manga', 'carambola', 'melão', 'melancia', 'manga', 'nespera', 'lichia', 'cereja']
print(frutas.index('maça'))
print(frutas.index('manga'))
print(frutas.index('manga', 6)) # busca a partir do indice de numero colocado
print(frutas.index('manga', 6, 12)) # busca a entre o indice de numero colocado
'''

''' Exibir a partir de um determinado indice 

frutas = ['uva', 'maça', 'banana', 'Morango', 'abacaxi', 'manga', 'carambola', 'melão', 'melancia', 'manga', 'nespera', 'lichia', 'cereja']

print(frutas[5:])
print(frutas[:5])
print(frutas[0::2]) # Mostra alternando de acordo com a quantidade colocado a partir do segundo ':'
'''

''' Verificação numerica de uma lista de valores inteiros ou reais

lista6 = [1, 2, 3, 4, 5, 6, 7]
print(sum(lista6))
print(max(lista6))
print(min(lista6))
print(len(lista6))
'''

''' Transformar lista em tupla

lista6 = [1, 2, 3, 4, 5, 6, 7]
print(lista6)
print(type(lista6))

tupla = tuple(lista6)
print(tupla)
print(type(tupla))

'''

''' Desempacotar uma lista, quantidade de numeros da lista e das variaveis devem ser os mesmos
lista6 = [1, 2, 3]

num1, num2, num3 = lista6
print(num1)
print(num2)
print(num3)

'''

''' Copiar lista de uma para outra (Shallow Copy and Deep Copy)

# Deep
lista6 = [1, 2, 3]
print(lista6)

nova = lista6.copy()
print(nova)
nova.append(4)

print(lista6)
print(nova)

# Shallow
lista6 = [1, 2, 3]
print(lista6)

nova = lista6
print(nova)

nova.append(4)

print(lista6)
print(nova)

'''

