nome = input("Qual seu nome? ")
salario = int(input("Qual seu salário? "))
vendas = int(input("Quantas vendas tu realizou? "))


def vendedor(a, b, c):
    print("Seu nome é: ",nome)
    print("Seu salário é: ",salario, "R$")
    liquido = salario + (salario * 0.15)
    print("Seu salário total é ",liquido, "R$")

vendedor(nome, salario, vendas)