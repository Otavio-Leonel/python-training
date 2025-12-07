# Duas condições necessárias
ativo = True
logado = True

if ativo and logado:
    print("Bem vindo usuario")
else:
    print('Favor logar')

# Ou uma ou outra condição
ativo = True

if ativo or logado:
    print("Bem vindo usuario")
else:
    print('Favor logar')

# Nega uma das condições 
ativo = True

if not ativo:
    print("Bem vindo usuario")
else:
    print('Favor logar')

# compara para ver se é aquela condição
ativo = True

if ativo is True:
    print("Bem vindo usuario")
else:
    print('Favor logar')