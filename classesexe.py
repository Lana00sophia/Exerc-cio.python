class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    def apresentar(self):
        return print(f"Olá meu nome é {self.nome},eu tenho{self.idade}anos!")
pess1 = Pessoa("Sophia",19)
pess2 = Pessoa("João",25)





