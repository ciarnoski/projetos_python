info = []


while True:
    opcao = int(input("1 para add, 2 para mostrar e 3 para sair:"))
    if opcao == 1:
        nome = input("nome:")
        numero = input("numero: ")
        email = input("email: ")
        
        infos = nome, numero, email
        if infos not in (info):
            info.append(infos)
            print("Contato adicionado")

    elif opcao == 2:
            
            print (info)
    elif opcao == 3:
        print("saindo")
        break
