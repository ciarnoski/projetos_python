bebida = int(input("Você planeja beber? "))
comida = int(input("Você planeja comer? "))
transporte = int(input("Você contratará transporte? "))
pessoas = int(input("Você irá sozinho? "))
def media(a,b,c):
    if bebida == 1 and comida == 1 and transporte == 1 and pessoas == 1:
        bebida = 80
        comida = 60
        transporte = 15
        pessoas = input("Quantas pessoas irá com você? ")
        media = (bebida + comida + transporte) * (pessoas+1)
        print(media)
    elif bebida == 2 and comida == 1 and transporte == 1 and pessoas == 1:
        bebida = 0
        comida = 60
        transporte = 15
        pessoas = input("Quantas pessoas irá com você? ")
        media = (bebida + comida + transporte) * (pessoas+1)
        print(media)
    elif bebida == = 's' or pessoas == 'S':
        bebida = 80
        comida = 0
        transporte = 15
        pessoas = input("Quantas pessoas irá com você? ")
        media = (bebida + comida + transporte) * (pessoas+1)
        print(media)
    elif bebida == 'sim' or bebida == 'Sim' or bebida == 's' or bebida == 'S' and comida == 'sim' or comida == 'Sim' or bebida == 'S' or bebida == 's' and transporte == 'nao' or transporte == 'Nao' or transporte == 'n' or transporte == 'N' and pessoas == 'Sim' or pessoas == 'sim' or pessoas == 's' or pessoas == 'S':
        bebida = 80
        comida = 60
        transporte = 0
        pessoas = input("Quantas pessoas irá com você? ")
        media = (bebida + comida + transporte) * (pessoas+1)
        print(media)
    elif bebida == 'sim' or bebida == 'Sim' or bebida == 's' or bebida == 'S' and comida == 'sim' or comida == 'Sim' or bebida == 'S' or bebida == 's' and transporte == 'sim' or transporte == 'Sim' or transporte == 's' or transporte == 'S' and pessoas == 'Nao' or pessoas == 'nao' or pessoas == 'N' or pessoas == 'n':
        bebida = 80
        comida = 60
        transporte = 0
        pessoas = 0
        media = (bebida + comida + transporte) * (pessoas+1)
        print(media)
    media(bebida, comida, transporte)   
    
