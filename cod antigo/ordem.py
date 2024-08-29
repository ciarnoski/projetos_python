print("Vamos descobrir a ordem descrescente de 3 números")
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite mais um valor: "))

if n1 >= n2 >= n3:
    print(n1,",",n2,",", n3)
elif n1 >= n3 >= n2:
    print(n1,",",n3,",", n2)
elif n2 >= n1 >= n3:
    print(n2,",",n1,",", n3)
elif n2 >= n3 >= n1:
    print(n2,",",n3,",", n1)
elif n3 >= n1 >= n2:
    print(n3,",",n1,",", n2)
elif n3 >= n2 >= n1:
    print(n3,",",n2,",", n1)
