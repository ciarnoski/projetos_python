texto = ''

def ola():
    if texto == '':
        print('ola')
    continuar = input('digite qualquer coisa para continuar ou 2 para sair: ')
    if continuar != '' and continuar != '2':
        ola()
    elif continuar == '2':
        print('finalizando')

ola()