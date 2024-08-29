senha ='123456'
condicao = True
numtentativa = 3

while condicao:
    entrada = input("Digite a sua senha: ")
    if entrada == senha:
        print("Você acertou sua senha.")
        condicao = False
    elif entrada != senha and numtentativa > 0:
        numtentativa -= 1
        print("senha errada, tentativas restantes:", numtentativa)
    elif numtentativa <= 0:
        print("Suas chances acabaram, bloqueamos seu cartão")
        condicao = False
        
  
    
        


