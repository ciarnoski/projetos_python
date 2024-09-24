produto = float(input("Quanto foi o valor do produto que você comprou parcelado em 5 vezes? "))

def valor(a):
    prestacao = produto / 5
    print("O valor de cada prestação foi: ", prestacao,"R$")

valor(produto)
