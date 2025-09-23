def saudacao():
    print("Olá,bem vindo ao Python!")
saudacao()

def dobro(a):
    return a * 2
print(dobro(2))
print(dobro(3))
print(dobro(5))
def soma(a,b):
    return a + b 
print(soma(10,20))
def mensagem(nome = "visitante"):
    print("Olá "+ nome + "!")
mensagem("Sophia")
mensagem()

def operações(a,b):
    soma = a + b 
    subtra = a - b
    multi = a * b
    return soma ,subtra ,multi

def media(*nums):
    soma = sum(numeros)
    quantidade = len(numeros)      
    return soma / quantidade 

    
    






