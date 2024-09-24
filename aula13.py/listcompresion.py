string = " chave1 : valor1  ,  chave2: valor2  ,  chave3: valor3  "

# Divide a string em pares de chave-valor
pares = [item.strip() for item in string.split(",")]

# Divide cada par pelo dois pontos e remove espaços em branco
lista = [tuple(par.strip().split(": ")) for par in pares]

print(lista)
