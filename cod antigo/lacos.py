entrada = ""
condicao = True
count = 0

while condicao:
    count+=1
    print("Digite uma das opções: 1- para exibir oi 2- para sair")
    print(" ")
    entrada = input("digite: ")
    print("vezes que repetiu o while: ", count)
    if entrada == "1":
        print ("oi")
    elif entrada == "2":
        print ("tu saiu")
        condicao = False
    else:
        print("digite algo válido.")
    print(" ")
    count += 1    
