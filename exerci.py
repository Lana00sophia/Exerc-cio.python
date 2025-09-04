livros = ["Crepusculo","Lua nova","Eclipse"]
print(livros)
print(livros[1:3])
livros.append("Amanhecer.1")
livros.append("Amanhecer.2")
print(livros)
livros.insert(1,"Duna")
print(livros)
print("Livro não encontrado")
numeros = [1,2,3,2,4,2,5]
repetidos = numeros.count(2)
print(repetidos)
for livro in livros:
    print(f"O livro {livro} é interessante")
idades = [12,14,18,30]
for idad in idades :
    if idad >= 18:
        print(idad)
valores = [10,20,30,40]
somaval = sum(valores)
print(somaval)


nota_1 = print(input("Nota 1: "))
nota_2 = print(input("Nota 2: "))
nota_3 = print(input("Nota 3: "))

#explicação do 11
#list comprehecion 
tabuleiro = [["[ ]"for casa in range(8)] for linha in range ]
print(tabuleiro)
