numero = 1
max = int(input("Digite um inteiro maior que 1: "))

print("Numeros pares entre 1 e", max,":")

while numero <= max:
    if numero%2==1: #é usado para mostrar os números pares!
        print(numero, end=" ")
    numero+=1