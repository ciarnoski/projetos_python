print("Esse é um programa que converte graus Celsius em Fahrenheit")

celsius = float(input("Quantos graus está? "))

def temp(a):
    f = (9*celsius+160)/5
    print("A temperatura em Fahrenheit é: ", f)

temp(celsius)