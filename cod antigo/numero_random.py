import random

valor = random.randint(1,100)
tentativa = None
num_tentativa = 0

while tentativa != valor:
    tentativa = int(input("Adivinhe um número de 1 a 100: "))
    num_tentativa += 1
    if tentativa < valor:
        print("Esse número é menor que o valor sorteado, numero de tentativas:", num_tentativa)
    elif tentativa > valor:
        print("Esse número é maior que o valor sorteado, numero de tentativas:", num_tentativa)
    else:
        print("Você acertou, numero de tentativas:", num_tentativa)    