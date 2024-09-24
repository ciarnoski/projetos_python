# Abrindo um arquivo para escrita
with open('exemplo.txt', 'w' , encoding='utf-8') as arquivo: #o enconding = 'utf-8' é usado para os acentos não bugarem, pois o utf-8 é do Brasil
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo do uso de with.')

# O arquivo é automaticamente fechado após o bloco with

with open('exemplo.txt','r', encoding='utf-8') as f:
    print(f.read())

