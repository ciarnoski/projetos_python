nomes = []

for x in range (0,4):
    nome = input ("Adicione um nome: ")

    nomes.append(nome)

print (nomes)

nome = input ("Digite um nome para pesquisar dentro da lista: ")

if nome in nomes:
    print(f'{nome} está em na lista')

elif nome not in nomes:
    print(f'{nome} não está na lista')
    