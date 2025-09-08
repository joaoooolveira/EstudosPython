#Exercício 1
while True:
    try:
       idade = int(input("Digite sua idade: "))
       print(f"Sua idade é {idade}")
       break
    except ValueError:
       print("Idade invalida, por favor digite um número!")
    
print("\n")

#Exercício 2
while True:
    try:
      num1 = int(input("Digite o 1º número: "))
      num2 = int(input("Digite o 2º número: "))
      soma = num1 + num2
      print(f"Resultado: {soma}")
      break
    except ValueError:
      print("Entrada inválida! Digite apenas números")

print("\n")

#Exercício 3
while True:
    try:
        celsius = float(input("Digite a temperatura em celsius: "))
    except ValueError:
        print("Temperatura inválida")

    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C fica {fahrenheit:.1f}°F em Fahrenheit")
    break
    
print("\n")

#Exercício 4
while True:
    try:
        numero = int(input("Digite um número de 0 a 10: "))
        if numero <= 10 and numero >= 0:
            print("Número valido!")
            break
        else:
            print("Nota fora do intervalo valido!")
    except ValueError:
        print("Digite apenas números.")
        
print("\n")

#Exercício 5
while True:
    try:
        preco = float(input("Digite o preço do produto: R$"))
        print(f"Preço registrado: R${preco:.2f}")
        break
    except:
        print("Preço inválido.")
        
print("\n")
        
#Exercício 6
while True:
    try:
        numerador = int(input("Digite um numerador: "))
        denominador = int(input("Digite um denominador: "))
        
        resultado = numerador / denominador
        print(f"O resultado é: {resultado}")
        break
    except ZeroDivisionError:
        print("Erro: Não é possivel dividir por zero!")
    except ValueError:
        print("Digite um número.")

print("\n")

#Exercício 7
frutas = ["Maçã", "Banana", "Uva"]
while True:
    try:   
        indice = int(input("Digite um índice: "))
        
        print(f"{frutas[indice]}")
        break
    except IndexError:
        print("Índice inválido! Essa posição não existe")
        
print("\n")

#Exercício 8
aluno = {"nome": "Léo", "idade": 17}
while True:
    try:
        chave = input("Digite uma chave que deseja acessar: ")
        
        print(f"Chave acessada: {aluno[chave]}")
        break
    except KeyError:
        print("Chave não encontrada!")
        
print("\n")

#Exercício 9
notas = []
nota = 1
soma = 0

while True:
    try:
        if nota != 0:
            for _ in range(3):
                nota = float(input("Digite suas notas: "))
                soma += nota
                notas.append(nota)
        
        media = soma / 3
        print(f"{notas}")
        print(f"A média dessas notas é: {media:.1f}")
        break
        
    except ValueError:
        print("Digite apenas números.")
        
    except ZeroDivisionError:
        print("Não existem notas na lista")
        
print("\n")

#Exercício 10
while True:
    try:
        palavra = input("Digite uma palavra: ")
        
        indice = int(input("Digite o índice: "))
        
        print(f"{palavra[indice]}")
        break
    
    except IndexError:
        print("Fora do comprimento da palavra")
        
    except ValueError:
        print("Digite um número.")
        
print("\n")

#Exercício 11

while True:
    try:
        usuario = input("Usuario: ")
        senha = int(input("Senha: "))
        
    except ValueError:
        print("Login ou senha incorreto!")
        
    else:
        print("Login bem-sucedido")
        break
    
print("\n")

#Exercício 12
try:
    int("abc")

except:
    print("Entrada inválida")
    
finally:
    print("Processo de relatório finalizado, com ousem erros.")
    
print("\n")

#Exercício 13
try:
    print("Baixando arquivo...")
    
except FileNotFoundError:
    print("Falha no download!")
    
else:
    print("Download concluído com sucesso!")
    
finally:
    print("Limpando recursos")
    
print("\n")

#Exercício 14
numero = int(input("Digite um número: "))
try:
    divisao = 100 / numero
    
except ZeroDivisionError:
    print("LOG: Tentativa de divisão por zero!")

else:
    print(f"O resultado é: {divisao}")
    
finally:
    print("Processamento de dados encerrado.")

print("\n")

#Exercício 15
try:
    num = input("Digite uma string: ")
    numInt = int(num)
    numFloat = float(numInt)
    
except ValueError:
    print("Não foi possível converter para número")

else:
    print(f"Resultado: {numFloat}")
    
print("\n")

#Exercício 16
def obter_numero_inteiro_seguro():
    while True:
        try:
            num = int(input("Digite um número: "))
            print("Número inteiro válido.")
            break
        
        except ValueError:
            print("Digite um número inteiro.")
            
obter_numero_inteiro_seguro()

#Exercício 17
def buscar_info_aluno(dicionarioAluno, chaveInfo):
    try:
        return f"Valor encontrado: {dicionarioAluno[chaveInfo]}"
    except KeyError:
        return f"Informação '{chaveInfo}' não encontrada."

aluno = {"nome": "Léo", "idade": 17, "curso": "Python"}      
print(buscar_info_aluno(aluno, "nome"))
print(buscar_info_aluno(aluno, "email"))

print("\n")

#Exercício 18
def fazerOperacao(num1 = None, num2 = None, operacao = ""):
    try:
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))
    
        operacao = input("Digite a operação: (+ ou /)")
    
        if operacao == '+':
            soma = num1 + num2
            return f"O resultado é: {soma}"
        elif operacao == '/':
            divisao = num1 / num2
            return f"O resultado é: {divisao}"
        else:
            print("Digite uma operação válida.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero!")
    
print(fazerOperacao())

#Exercício 19
usuarioCorreto = "senaialunos"
senhaCorreta = "senai2025"
i = 0

while i < 3:
    try:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuario == usuarioCorreto and senha == senhaCorreta:
            print("Login bem-sucedido")
            break
        else:
            print("Tente novamente.")

    except Exception:
        print("Erro na entrada de dados.")
    i += 1

if i == 3:
    print("Login bloqueado")
    
print("\n")

#Exercício 20
def ler_nomes_do_arquivo(nome_arquivo):
    nomes = []
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                if nome:
                    nomes.append(nome)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return nomes

# Programa principal
lista_nomes = ler_nomes_do_arquivo("nomes.txt")
print("Lista de nomes:", lista_nomes)