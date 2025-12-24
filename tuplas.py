# diferente das listas as tuplas são imutaveis

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2) 

print(type(tupla2))

# não existem tuplas de apenas um item

tupla3 = (4)
print(tupla3) 

print(type(tupla3))

tupla4 = (4,)
print(tupla4) 

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# tuplas são definidas pelas virgulas e não somente pelo uso de ()

tupla6 = tuple(range(11))
print(tupla6) 

print(type(tupla6))

# desenpacotamento de tupla

tupla7 = ('universo', 'astronomico')

local, materia = tupla7

print(local)
print(materia)

# remoção, adição e outras alterações não existem nas tuplas por serem imutaveis

tupla8 = (1, 2, 3, 4, 5, 6)

print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

# apenas com numeros reais ou inteiros acima

# Concatenação de tuplas

tupla9 = (1, 2, 3)
print(tupla9)

tupla10 = (4, 5, 6)
print(tupla10)

print(tupla9 + tupla10)

tupla11 = tupla9 + tupla10

print(tupla9)
print(tupla10)
print(tupla11)

tupla9 = tupla9 + tupla10
print(tupla9)

# Tuplas são imutaveis, mas podem ser sobrescrevidas

tupla12 = (1, 2, 3)
print(3 in tupla12)

# Iterando uma tupla

tupla13 = (1, 2, 3)

for n in tupla13:
    print(n)

for indice, valor in enumerate(tupla13):
    print(indice, valor)
    
# Contagem de elementos

tupla14 = ('a', 'b', 'c', 'a')
print(tupla14.count('a'))

estrela = tuple('Bellatrix')
print(estrela)

print(estrela.count('l'))

# Utilizar tupla quando os dados forem realmente imutaveis e não devem ser alterados

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses[5])

# Iterar while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

print(meses.index('Junho'))
print(meses[5:9])

# Copiando uma tupla para outra

tupla15 = (1, 2, 3)
print(tupla15)

nova = tupla15

print(nova)
print(tupla15)

tupla16 = (4, 5, 6)

nova = nova + tupla16
print(nova)
print(tupla16)
