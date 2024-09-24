with open('exemplo.txt', 'r+', encoding='utf-8') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.write('Este é um exemplo do uso de with.')
   
    #Mover o cursor de volta ao início do arquivo
    arquivo.seek(0)
   
    #Ler e imprimir o conteúdo do arquivo
    conteudo = arquivo.read()
    print(conteudo)