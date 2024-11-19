class Calculadora:
    def __init__(self) -> None:
        pass
    def soma(self, a, b):
        return a+b
    def diz_oi(self):
        print('oi')
obj_calculdadora = Calculadora()
print(obj_calculdadora.soma(5,5))
obj_calculdadora.diz_oi()