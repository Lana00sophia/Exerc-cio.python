#tuplas não são tão dinâmicas e não pode ser modificada
#além dos parênteses se coloca a vírgula
tupla = ("joão",)
#print(type(tupla2))

#pode somar 
tupla1 = ("joão","maria",)
tupla2 = ("larissa","paulo",)

#conjuntos
#"sets"
#os dados n são ordenados 
conjuntos = {"Lana","Lótus","Luna"}
#ñ adimite repetição
print(conjuntos)

#Dicionários 
#São coleções que recebem valores definidos por chaves tmb mas precisa 
dicionário_vazio = {"pedro":13}
# as adiçoes são sempre sucessivas



num = input("informe um numuero de 1 a 3")
match num:
    case "1":
        print("você digitou 1")
    case "2":
        print("você digitou 2")
    case "3":
        print("você digitou 3")
    case _:
        print("Número não encontrado")

frutas = input("frutas boas")
match frutas:
    case "banana"|"Abacaxi"|"Maracujá":
        print("Fruta boa")
    case "mamão"|"laranja"|"pera":
        print("fruta ruim")
        
#funções evita repetição e moduliza o código 
def nome_função():
    print("Ola mundo")
nome_função
def ola(msg):

#msg é uma variável