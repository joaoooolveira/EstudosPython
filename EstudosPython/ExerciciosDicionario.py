#Exercício 1
jogador = {"nome": "João", "pontuação": "9", "nivel": "12"}

print(jogador)
print(f"Pontuação: {jogador["pontuação"]}\n")

#Exercício 2
filme = {"titulo": "Carros 2", "diretor": "John Lasseter", "ano_lancamento": "2011", "genero": "Família/Comédia"}

print(f"Filme: {filme["titulo"]}\nDiretor: {filme["diretor"]}\n")

#Exercício 3
funcionario = {"id": "95423", "nome": "João", "cargo": "Atendente", "salario": "R$2.000"}

print(f"Nome: {funcionario["nome"]}\nCargo: {funcionario["cargo"]}\n")

#Exercício 4
animal_estimacao = {"nome": "Amante", "especie": "Cavalo", "idade": "6 anos", "cor_pelo": "Marrom"}

print(f"Espécie: {animal_estimacao['especie']}\nIdade: {animal_estimacao['idade']}\n")

#Exercício 5
receita = {"nome_prato": "Carne de porco", "tempo_preparo": "6 minutos"}

print(f"Nome do prato: {receita['nome_prato']}\nTempo de preparo: {receita['tempo_preparo']}")

#Exercício 6
jogador = {"nome": "Heroi", "pontuação": 1000, "nivel": 1}

jogador["pontuação"] = 1250
jogador["nivel"] = 2

print(f"{jogador}\n")

#Exercício 7
livro = {"titulo": "Kimetsu no yaiba", "autor": "Koyoharu Gotouge", "estoque": 5}

livro["estoque"] += 10
livro["preco"] = "R$89,90"

print(f"{livro}\n")

#Exercício 8
aluno = {"nome": "Mariana", "idade": 17, "curso": "Programação"}
aluno["notas"] = [8.5, 9.0, 7.5]
aluno["curso"] = "Engenharia de Software"

print(f"{aluno}\n")

#Exercício 9
carrinho_item = {"produto": "Camiseta", "preco_unitario": 49.90, "quantidade": 2}
carrinho_item["quantidade"] = 3
total = carrinho_item["preco_unitario"] * carrinho_item["quantidade"]

carrinho_item["total_item"] = total

print(f"{carrinho_item}\n")

#Exercício 10
frutas = {"maca": 3.50, "banana": 2.00, "laranja": 4.00}
frutas["maca"] = 3.80
frutas["uva"] = 6.00

print(f"{frutas}\n")

#Exercício 11
perfil = {"nome": "Pedro", "idade": 22, "cidade": "Rio", "email": "pedro@email.com"}
perfil.pop("email")

print(f"{perfil}\n")

#Exercício 12
produto = {"id": "A123", "nome": "Teclado RGB", "estoque": 10, "marca": "GamerX"}
produto.pop("estoque")

print(f"{produto}\n")

#Exercício 13
tarefa = {"descricao": "Comprar pão", "prazo": "Hoje", "prioridade": "Alta"}
prazoremovido = tarefa.pop("prazo")

print(f"Valor removido: {prazoremovido}")
print(f"{tarefa}\n")

#Exercício 14
menu_cafe = {"café": 5.00, "bolo": 8.00, "suco": 6.50}
if "pao de queijo" in menu_cafe:
    print("Pão de queijo disponível!")
else:
    print("Pão de queijo não está está no menu.\n")

#Exercício 15
pedido = {"id": "P001", "cliente": "Fernanda", "status": "Processando"}
if "status" in pedido:
    print(f"{pedido['status']}\n")
else:
    print("Status do pedido não encontrado")

#Exercício 16
convidados = {"Ana": 28, "Beto": 30, "Carla": 25}

for nome in convidados.keys():
    print(f"{nome}")

print("\n")

#Exercício 17
carrinho = {"Maçã": 2, "Leite": 1, "Pão": 3}

for item in carrinho.items():
    print(f"{item}")

print("\n")

#Exercício 18
livro = {"Titulo": "Dom Casmurro", "Autor": "Machado de Assis", "Ano": 1899, "Genero": "Romance"}
for itens in livro.items():
    print(f"{itens}")

print("\n")

#Exercício 19
temperaturas = {"seg": 25.5, "ter": 28.0, "qua": 26.2, "qui": 27.5, "sex": 29.1}

for temp in temperaturas.values():
    print(f"{temp}")

print("\n")

#Exercício 20
vendas_mes = {"Janeiro": 12000, "Fevereiro": 15000, "Março": 13500, "Abril": 18000}

for vendas in vendas_mes.items():
    print(f"{vendas}")

print("\n")