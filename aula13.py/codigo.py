import os

def salvar_variaveis(**kwargs):
    with open("dados.txt",'w') as f:

        for chave, valor in kwargs.items():
            f.write(f"{chave}: {valor}\n")

if not os.path.exists("dados.txt") :

    with open("dados.txt","w") as w :
        nome_v = input("digite seu nome: ")
        telefone_v = input("\ndigite seu numero: ")
        email_v = input("\ndigite seu email: ")
        salvar_variaveis(nome = nome_v, telefone = telefone_v, email = email_v)

elif os.path.exists("dados.txt") :

    with open("dados.txt","r") as r :
        for line in r :
            chave,valor = line.strip().split(": ")
            print(chave,":",valor)