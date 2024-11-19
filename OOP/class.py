class Aluno:
    def __init__(self,nome_p):
        self.nome = nome_p
    def correr(self):
        print(f'correndo{self.nome}')
    def descansar(self):
        print('estou cansado chefe!')
aluno1 = Aluno('joao')
aluno2 = Aluno('maria')

aluno1.correr