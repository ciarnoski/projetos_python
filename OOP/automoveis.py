class Automovel:
    def __init__(self, marca, modelo, ano, cor, motor, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.preco = preco
    def info(self):
        return (f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nMotor: {self.motor}\nPreço: {self.preco}')

carro = Automovel('Peugeot', '208 Active', '2023', 'Preto', '1.6', '79.990,00')
print(carro.info())