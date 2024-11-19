class Animal:
    def __init__(self, qnt_patas, som_emitido, especie):
        self.qnt_patas = qnt_patas
        self.som_emitido = som_emitido
        self.especie = especie

class Cachorro(Animal):
    def __init__(self, qnt_patas, som_emitido, especie, cor_pelo, raca, nome):
        super().__init__(qnt_patas, som_emitido, especie)
        self.cor_pelo = cor_pelo
        self.raca = raca
        self.nome = nome
    def __str__(self):
        return (f'Quantidade de patas: {self.qnt_patas}\nSom: {self.som_emitido}\nEspécie: {self.especie}\nCor: {self.cor_pelo}\nRaça: {self.raca}\nNome: {self.nome}') 
        

cachorro1 = Cachorro('4', 'Latido', 'Canis lupus familiaris', 'Dourado', 'Golden Retriever', 'Rex')
print(cachorro1)
    