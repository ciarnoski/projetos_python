def calculo(a,b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao

n1 = float(input ("Digite um número: "))
n2 = float(input("Digite outro número: "))

print(calculo(n1,n2))
