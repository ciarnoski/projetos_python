class Pessoa:
    nome = ''
    idade = ''
    def set_nome(self, n):
        self.nome = n
    def set_idade(self, i):
        self.idade = i
    
    def get_nome(self):
        return (f'o seu nome é {self.nome}')
    def get_idade(self):
        return(f'a sua idade é {self.idade}')

individuo = Pessoa()
individuo.set_nome('Angelo')
individuo.set_idade('17')

print(individuo.get_nome())
print(individuo.get_idade())