#Exercício 1
def saudar_visitante():
    print("Bem vindo(a) à TechSolutions! Como posso ajudar?")

saudar_visitante()
saudar_visitante()
saudar_visitante()

print("\n")

#Exercício 2
def emitir_som_alarme():
    print("BEEP! BEEP! BEEP! O bolo está pronto!")

emitir_som_alarme()

print("\n")

#Exercício 3
def cartao_boas_festas():
    print("Feliz Natal e um próspero Ano Novo! Que todos os seus desejos se realizem!")

cartao_boas_festas()

print("\n")

#Exercício 4

def executar_danca_robo():
    print("Passo para frente! Giro para a esquerda! Balança os braços!")

executar_danca_robo()
executar_danca_robo()

print("\n")

#Exercício 5
def iniciar_nova_rodada():
    print("--- INÍCIO DA NOVA RODADA ---")
    print("Preparem-se!")

iniciar_nova_rodada()

print("\n")

#Exercício 6
bebida = input("Digite uma bebida de sua escolha: ")

def preparar_bebida():
    print(f"Seu {bebida} está pronto!")

preparar_bebida()

print("\n")

#Exercício 7
nome = input("Digite seu nome: ")

def saudar_visitante_personalizado():
    print(f"Bem-vindo(a), {nome}! Estamos felizes em vê-lo(a)!")

saudar_visitante_personalizado()

print("\n")

#Exercício 8
numero_destino = input("Digite o número destino: ")
mensagem = input("Mensagem: ")

def enviar_sms():
    print(f"Enviando mensagem para: {numero_destino}")
    print(f"{mensagem}")

enviar_sms()

print("\n")

#Exercício 9
def dobrar_ingrediente(ingrediente, quantidade_original):
    print(f"Para {ingrediente}, use {quantidade_original * 2} unidades")

dobrar_ingrediente(ingrediente = "Farinha", quantidade_original = 2)
dobrar_ingrediente(ingrediente = "Açúcar", quantidade_original = 0.5)

print("\n")

#Exercício 11
fruta = input("Digite uma fruta: ")

def fazer_suco(fruta):
  return f"Suco de {fruta} fresco!"

meu_suco = fazer_suco(fruta)

print(meu_suco)

print("\n")

#Exercício 12

def verificar_idade(idade_pessoa, idade_minima):
    if idade_pessoa >= idade_minima:
        return True
    else:
        return False
    
idade_pessoa = int(input("Digite a sua idade: "))
idade_minima = 12

pode_entrar = verificar_idade(idade_pessoa, idade_minima)
if pode_entrar:
  print("Pode entrar!")
else:
  print("Entrada negada.")

print("\n")

#Exercício 13

def calcular_media(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3) / 3
  return media

resultado_media = calcular_media(nota1 = float(input("Nota 1 = ")), nota2 = float(input("Nota 2 = ")), nota3 = float(input("Nota 3 = ")))
print("O resultado da média é:", resultado_media)

print("\n")

#Exercício 14

def reais_para_dolar(valor_reais, cotacao):
  resultado = valor_reais * cotacao
  print(f"O valor de R${valor_reais:.2f} em dólar é de: U${resultado:.2f}")

reais_para_dolar(valor_reais= float(input("Digite o valor: ")), cotacao= float(5.47))

print("\n")

#Exercício 15
def classificar_numero(numero):
    if(numero > 0):
        return f"{numero} é um número positivo"
    elif(numero < 0):
        return f"{numero} é um número negativo"
    else:
        return "Número zero."

print(classificar_numero(numero= int(input("Digite um número: "))))
print(classificar_numero(numero= int(input("Digite um número: "))))
print(classificar_numero(numero= int(input("Digite um número: "))))

print("\n")

#Exercício 16
def pedir_e_somar():
   x = int(input("Digite o 1º número: "))
   y = int(input("Digite o 2º número: "))
   return x + y

resultado = pedir_e_somar()
print(f"Resultado: {resultado}")

print("\n")

#Exercício 17
def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    return [nome, idade]

lista = cadastrar_usuario()
print(lista)

print("\n")

#Exercício 18
def calcular_imc():
    peso = float(input("Digite seu peso(em kg): "))
    altura = float(input("Digite sua altura(em m): "))

    return peso / (altura * altura)

valorIMC = calcular_imc()
print(f"O calculo do IMC é de: {valorIMC:.2f}")

print("\n")

#Exercicio 19
def verificar_login(usuario_correto, senha_correta):
    usuario = input("Usuário: ")
    senha = int(input("Senha: "))

    if usuario == usuario_correto and senha == senha_correta:
        return True
    else:
        return False

login = verificar_login(usuario_correto = "joao", senha_correta = 101025)
if login == True:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos!")

print("\n")

#Exercício 21
def gerar_mensagens_diarias(lista_nomes):
    for nome in lista_nomes:
        print(f"Bom dia, {nome}! tenha um ótimo dia!")

gerar_mensagens_diarias(lista_nomes= ['João', 'Nicole', 'Daniel'])