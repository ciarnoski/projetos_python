class Shark:
    animal_type = 'fish'
    location = 'ocean'
    flowers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_followers(self,followers):
        self.flowers = followers
        print('This user has ' + str(followers) + ' followers')
nome = Shark('nemo', 15)
nome.set_followers(5)
print(nome.flowers)