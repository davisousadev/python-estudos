class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        return f"{self.nome} está latindo!"
        
anamaria = Cachorro("Anamaria", "Labrador")

print(anamaria.latir())