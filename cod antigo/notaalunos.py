print ("Veremos qual letra que tu tirou no teste, escreva um número de 0 a 10, por gentileza.")
nota = float(input("Digite a nota que você tirou no teste: "))


if nota < 6.0 and nota >= 0:
    print("Sua nota é F")
elif nota >= 6.0 and nota < 7.0:
    print("Sua nota é D")
elif nota >= 7.0 and nota < 8.0:
    print("Sua nota é C")
elif nota >= 8.0 and nota < 9.0:
    print("Sua nota é B")
elif nota >= 9.0 and nota <= 10.0:
    print("PARABÉNS! Sua nota é um A")
else:
    print("Tu não digitou um valor adequado")
    


