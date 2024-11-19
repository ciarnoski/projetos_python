class Super():
    def coisar(self):
        print('o super está coisando')


class Sub(Super):
    def __init__(self) -> None:
        super().__init__()
    def coisar(self):
        print('o sub está coisando')

coisas = Sub()
coisas.coisar()