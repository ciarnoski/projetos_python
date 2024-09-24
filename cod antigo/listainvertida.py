rodada = 0
lista = []

for x in range(0,10):
    entrada = input(f'(rodada {rodada})) - digite um número: ')
    lista.append(entrada)
    rodada += 1

print(f'a ordem original de números foi: {lista}')



lista.reverse()(print(f'a ordem inversa de números foi: {lista}'))