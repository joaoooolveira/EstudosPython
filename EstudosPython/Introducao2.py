#EX1
nome = input("Digite seu nome: ")
animal_favorito = input("Qual é o seu animal favorito? ")

print("Olá,", nome + "! Bem-vindo")
print("Seu animal favorito é:", animal_favorito)

print("\n")

#EX2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma dos números é:", soma)

print("\n")

#EX3
numero_decimal = float(input("Digite um número decimal: "))
dobro = numero_decimal * 2

print("O dobro do número é:", dobro)

print("\n")

#EX4
idade = int(input("Qual a sua idade em anos? "))
idade_meses = idade * 12

print("Sua idade em meses é aproximadamente:", idade_meses)

print("\n")

#EX5
largura = float(input("Digite a largura do retângulo (em metros): "))
altura = float(input("Digite a altura do retângulo (em metros): "))

area = largura * altura
print(f"A área do retângulo é: {area} metros quadrados.")

print("\n")

#EX6
rua = input("Digite o nome da sua rua: ")
numero = input("Digite o número da sua casa: ")
bairro = input("Digite o nome do seu bairro: ")

print(f"Seu endereço completo é: {rua}, {numero}, {bairro}.")

print("\n")

#EX7
preco_original = float(input("Digite o preço original do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"O preço final com desconto é: R$ {preco_final:.2f}")

print("\n")

#EX8
cores = ["vermelho", "preto", "rubro-negro"]

print(cores)

print("\n")

#EX9
amigos = ["João", "Lucas", "Pedro", "Nicole"]

print("O segundo nome na lista é:", amigos[1])

#EX10
filmes = ["Como treinar seu dragão", "Pokemon", "Carros 2"]
novo_filme = input("Digite um novo filme para adicionar: ")
filmes.append(novo_filme)

print(f"Sua lista de filmes atualizada é:", filmes)

print("\n")

#EX11
ingredientes = ["farinha", "açúcar", "ovos", "leite"]
ingrediente_removido = ingredientes.pop()

print(f"Ingrediente removido: {ingrediente_removido}")

print(f"Lista de ingredientes agora: {ingredientes}")

print("\n")

#EX12
hobbies = ["leitura", "caminhada", "cozinhar", "jogar videogame"]
quantidade_hobbies = len(hobbies)

print(f"Você tem {quantidade_hobbies} hobbies.")

print("\n")

#EX13
lista_compras = []
print("Vamos criar sua lista de compras. Digite 3 itens.")

for i in range(3):
    item = input(f"Digite o item {i + 1}: ")
    lista_compras.append(item)
    
print("Sua lista de compras completa é:", lista_compras)

print("\n")

#EX14
pessoas = ["Ana", "Pedro", "Carla", "João", "Juliana"]
primeira_pessoa = pessoas[0]
ultima_pessoa = pessoas[len(pessoas) - 1]

print(f"A primeira pessoa na fila é: {primeira_pessoa}")
print(f"A última pessoa na fila é: {ultima_pessoa}")

print("\n")

#EX15
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
    
print("\n")

#EX16
senha_correta = "abracadabra"
senha_digitada = "" # Valor inicial para o loop começar

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada != senha_correta:
        print("Senha incorreta. Tente novamente.")

print("Senha correta! Bem-vindo!")

print("\n")

#EX17
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
    
print("\n")

#EX18
soma = 0
numero = -1 # Valor inicial diferente de zero

while numero != 0:
    numero = float(input("Digite um número (0 para parar): "))
    soma += numero

print(f"A soma total dos números é: {soma}")

print("\n")

#EX19
opcao = 0
while opcao != 3:
    print("\n--- MENU ---")
    print("1 - Ver saldo")
    print("2 - Fazer depósito")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    
print("Obrigado por usar o nosso serviço!")

print("\n")