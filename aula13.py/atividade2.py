import os

# Salvar variáveis em um arquivo separado por nomes
def salvar_variaveis(path_file, **kwargs):
    with open(path_file, 'w') as f:
        for chave, valor in kwargs.items():
            f.write(f"{chave}: {valor}\n")

# Carregar variáveis de um arquivo
def carregar_variaveis(path_file):
    variaveis = {}
    with open(path_file, 'r') as f:
        for line in f:
            chave, valor = line.strip().split(': ')
            variaveis[chave] = valor
        return variaveis

def verifica_primeira_vez():
    match os.path.exists("texto.txt"):

        case True:
            variaveis_carregadas = carregar_variaveis('texto.txt')

            if len(variaveis_carregadas) > 0:
                print(f"seja bem vindo novamente {variaveis_carregadas["nome"]}, seu email é {variaveis_carregadas["email"]} e seu telefone é {variaveis_carregadas["telefone"]}")
            else:
                nome_v = input("por favor digite seu nome")
                email_v = input("digite seu email")
                telefone_v = input("digite seu telefone")

                salvar_variaveis('texto.txt',nome = nome_v, email = email_v, telefone = telefone_v )
        case False:
            nome_v = input("por favor digite seu nome")
            email_v = input("digite seu email")
            telefone_v = input("digite seu telefone")

            salvar_variaveis('texto.txt',nome = nome_v, email = email_v, telefone = telefone_v )

verifica_primeira_vez()