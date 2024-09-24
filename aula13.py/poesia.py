import os

print('frases poeticas')

while True:
    poeta = input('escreva uma frase poetica: ')
    if poeta == "":
        print('vc nao escreveu nada se4u idiota nada POETICO')
        arquivos = open("aula13.py/frases.txt",'r')
        print(arquivos.read())
        arquivos.close()
        break

    if os.path.exists('aula13.py/frases.txt'):
        arquivos = open('aula13.py/frases.txt','a')
    else:
        arquivos = open('aula13.py/frases.txt','w')
    arquivos.write(f'{poeta}\n')
    arquivos.close()