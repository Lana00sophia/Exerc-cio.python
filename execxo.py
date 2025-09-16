try :
    numero = int(input("Coloque um número: "))
except ValueError:
    print("Número inválido!")
else :
    print(f"número",numero)

try :
    num_1 = int(input("Primeiro número: ")) 
    num_2 = int(input("Segundo número: "))
except Exception:
    print("Algo de errado :(")
else : 
    print(num_1 * num_2)

try:
    arquivo = open("dados.txt") 
    print("Abrindo arquivo")
except FileNotFoundError:
    print("Arquivo ainda não existe.")
finally:
    print("Encerrando programa.")


def divisao(a,b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b
print(divisao(9,3))

class IdadeInvalidaError(Exception):
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("Idade não pode ser negativa.")
    print("Idade cadastrada")

try:
    n1 = int(input("Dividendo: "))
    n2 = int(input("Divisor: "))
    resultado = n1 / n2
except ValueError:
    print("Valor inválido. Digite apenas números.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print("Resultado da divisão:", resultado)

try:
    numero_ = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: valor inválido.")
else:
    if numero_ % 2 == 0:
        print(f"O número {numero_} é par.")
    else:
        print(f"O número {numero_} é ímpar.")
finally:
    print("Fim do programa.")
class saldoinsuficiente.erro
