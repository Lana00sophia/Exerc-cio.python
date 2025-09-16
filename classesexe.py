class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def apresentar(self):
        return print(f"Olá meu nome é {self.nome},eu tenho{self.idade}anos!")
pess1 = Pessoa("Sophia",19)
pess2 = Pessoa("João",25)
pess1.apresentar()

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)
carro3 = Carro("Ford", "Focus", 2018)
print(f"{carro1.marca} {carro1.modelo}, Ano: {carro1.ano}")
print(f"{carro2.marca} {carro2.modelo}, Ano: {carro2.ano}")
print(f"{carro3.marca} {carro3.modelo}, Ano: {carro3.ano}")
print("Antes:", carro1.ano)

# Alterando o ano
carro1.ano = 2022
print("Depois:", carro1.ano)

