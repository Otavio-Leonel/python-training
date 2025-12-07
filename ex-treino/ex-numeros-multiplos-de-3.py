print("Vamos verificar os numero multiplos de 3!")

max = int(input("Digite quantos numeros multiplos de 3 quer visualizar: "))
contagem = 0
num = 1

while contagem != max:
    multiplo = 3 * num
    print(f"{multiplo} é um multiplo de 3")
    num = num + 1
    contagem = contagem + 1
