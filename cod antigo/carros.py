carros = [
    {"marca": "Toyota","modelo":"Corolla", "ano":2022,'cor': "prata", "preco": 25000},
    {"marca": "Honda","modelo":"Civic", "ano":2021,'cor': "preto", "preco": 28000},
    {"marca": "Ford","modelo":"Mustang", "ano":2020,'cor': "vermelho", "preco": 45000},
    {"marca": "Chevrolet","modelo":"Camaro", "ano":2021,'cor': "azul", "preco": 50000},
    {"marca": "Tesla","modelo":"Model S", "ano":2023,'cor': "branco", "preco": 60000},   
]
for carro in carros:
    if carro['marca'] == 'ford':
        print(f"Marca: {carro['marca']}, Modelo: {carro['modelo']}, Ano: {carro['ano']}, Cor: {carro['cor']}, Preço: {carro['preco']}")