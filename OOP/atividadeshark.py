class Shark():
    def nadar(self):
        print('o tubarão esta nadando')
    def nadar_para_tras(self):
        print('o tubarão nao consegue nadar para tras, mas pode afundar para tras')
    def esqueleto(self):
        print('o esqueleto do tubarao é feito de cartilagem')

class Clowfish(Shark):
    def __init__(self) -> None:
        super().__init__()
    def nadar(self):
        print('o peixe palhaço esta nadando')
    def nadar_para_tras(self):
        print('o peixe palhaço pode nadar pra tras')
    def esquelo(self):
        print('o esqueleto do peixe palhaço é feito de osso')

peixe_palhaco = Clowfish()

peixe_palhaco.nadar()