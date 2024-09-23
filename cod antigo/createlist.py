list1 = []
info = ""
condicao = True

while condicao:
  
    resultado = input("Se quiser adicionar itens nessa lista, aperte '1', para ver sua lista, aperte '2', para sair, aperte '3': ")
    if resultado == '2':
            print(list1)
    elif resultado == '3':
            condicao = False
            print("Programa finalizado, sua lista ficou assim: ",list1)
    elif resultado == '1':
           info = input("Adicione informações nessa lista: ")
           list1.append(info)
    else:
        print(list1)

    

        

