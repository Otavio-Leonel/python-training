# print("Qual seu Nome?")
# nome = input()

nome = input('Qual seu nome? ')

# print('Bem vindo %s' % nome) Old
# print('Bem vindo {0}' .format(nome))
print(f'Seja bem vindo {nome}')

# print("Qual sua idade?")
# idade = input()

idade = int(input('Qual sua idade? '))

# print('%s tem %s anos' % (nome, idade)) old
# print('{0} tem {1} anos' .format(nome, idade))
print(f'{nome} possui {idade} anos')
print(f'{nome} nasceu em {2025 - idade}')

