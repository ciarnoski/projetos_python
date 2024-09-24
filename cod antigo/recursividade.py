lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def remocao():
    if lista != []:
        lista.pop()
        print(lista)
        remocao()
    else:
        print('a lista foi totalmente removida')

remocao()
        
     

    

