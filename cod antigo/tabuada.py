condicao = True
count = 0
while condicao:
    count = 0
    entrada = int(input("Informe um número para saber sua tabuada: "))

    while count<=10:
        print(f"{entrada} x {count} = {entrada * count}")
        count += 1

        opcao = input ("1 - para informar  ")
