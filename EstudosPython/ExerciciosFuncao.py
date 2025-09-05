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
#def cartao_boas_festas():
#    print("Feliz Natal e um próspero Ano Novo! Que todos os seus desejos se realizem!")

#cartao_boas_festas()

#print("\n")

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

print("\n")

#Exercício 22
def adicionar_lembrete(lista_lembretes = []):
    novolembrete = input("Digite um novo lembrete: ")
    lista_lembretes.append(novolembrete)
    print(lista_lembretes)

listarLembretes = ["Comprar leite", "Ligar para o médico"]
adicionar_lembrete(listarLembretes)
adicionar_lembrete(listarLembretes)

print("\n")

#Exercício 23
print("Jogo de adivinhação")
def jogar_adivinhacao(numero_secreto, max_tentativas):
    tentativas = 0
    while tentativas < max_tentativas:
        numero = int(input("Digite um número: "))
        tentativas += 1
        if numero == numero_secreto:
            return True
        else:
            print("Tente novamente!")
    return False

jogo = jogar_adivinhacao(numero_secreto = 7, max_tentativas= 3)
if jogo == True:
    print("Você acertou!")
else:
    print("Que pena, você não acertou!")

print("\n")

#Exercício 26
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_lowercase + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
senhaAtual = gerar_senha(tamanho)
print(senhaAtual)
print("\n")

#Exercício 27
lista = []
def mostrar_tarefas(lista = []):
    print(lista)

def adicionar_tarefa(lista = []):
    tarefa = input("Insira uma nova tarefa: ")
    lista.append(tarefa)

def remover_tarefa(lista = []):
    if not lista:
        print("Lista vazia!")
        return
    try:
        indice = int(input(f"Digite o índice que deseja remover: (0 a {len(lista)-1}): "))
        removido = lista.pop(indice)
        print(f"Item removido: {removido}")
    except (ValueError, IndexError):
        print("Índice inválido.")

while True:
    escolha = int(input("Escolha entre: \n1) Mostrar lista\n2) Adicionar item\n3) Remover item\n0) Sair\n"))
    if escolha == 1:
        mostrar_tarefas(lista)   
    elif escolha == 2:
        adicionar_tarefa(lista)      
    elif escolha == 3:
        remover_tarefa(lista)
    elif escolha == 0:
        break
    else:
        print("Opção inválida!")
    
print("\n")

#Exercício 28
saldo = 0

def ver_saldo(saldo_atual):
    print(f"Saldo atual: R${saldo_atual}\n")
    return saldo_atual

def depositar(saldo_atual, valor):
    deposito = int(input("Digite o valor do deposito: "))
    valor = deposito
    saldo_atual += valor
    print(f"Deposito concluído!\nSaldo atual: R${saldo_atual}\n")

    return saldo_atual

def sacar(saldo_atual, valor):
    saque = int(input("Digite o valor que deseja sacar: "))
    valor = saque
    if saque <= saldo_atual:
        saldo_atual -= valor
        print(f"Saque concluído! \nValor atual: R${saldo_atual}\n")
    else:
        print("Saldo insuficiente.\n")

    return saldo_atual

while True:
    escolha = int(input("Escolha entre: \n1) Ver saldo\n2) Depositar\n3) Sacar\n"))
    if escolha == 1:
        ver_saldo(saldo)
    elif escolha == 2:
        saldo = depositar(saldo, 0)
    elif escolha == 3:
        saldo = sacar(saldo, 0)
    else:
        break

print("\n")

#Exercício 29
import random

def jogar_par_ou_impar():
    escolha = input("Escolha Par ou Impar: ")
    if escolha not in ["Par", "Impar"]:
        return "Escolha inválida! Escolha entre Par ou Impar."

    for _ in range(1):
        numero = random.randint(1, 10)
        numeroEscolha = int(input("Digite um número: "))
        print(f"O número aleatório gerado foi: {numero}")
        soma = numero + numeroEscolha
        print(f"A soma de {numero} + {numeroEscolha} é: {soma}")
        
        if escolha == "Par" and soma % 2 == 0:
            return "Ganhou!"
        elif escolha == "Impar" and soma % 2 != 0:
            return "Ganhou!"
        else:
            return "Perdeu!"

print (jogar_par_ou_impar())

print("\n")

#Exercício 30
soma = 0
media = 0

def cadastrar_aluno():
    nome = input("Digite seu nome: ")
    nota = []

    for i in range(3):
        while True:
            nota_atual = float(input(f"Digite a {i + 1}ª nota: \n"))
            if 0 <= nota_atual <= 10:
                nota.append(nota_atual)
                break
            else:
                print("A nota deve estar entre 0 e 10.")

    lista_aluno = [nome] + nota
    return lista_aluno

def calcular_media_aluno(lista_aluno):
    notas = lista_aluno[1:]
    media = sum(notas) / len(notas)
    return media

def mostrar_boletim(lista_aluno, media):
    nome = lista_aluno[0]
    notas = lista_aluno[1:]
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}\n")

todos_os_alunos = []

while True:
    lista_aluno = cadastrar_aluno()
    todos_os_alunos.append(lista_aluno)

    media = calcular_media_aluno(lista_aluno)
    mostrar_boletim(lista_aluno, media)

    outroAluno = input("Deseja cadastrar outro aluno? (s/n): \n")
    if outroAluno != 's':
        break

print("Aqui estão os boletins: \n")
for aluno in todos_os_alunos:
    media = calcular_media_aluno(aluno)
    mostrar_boletim(aluno, media)