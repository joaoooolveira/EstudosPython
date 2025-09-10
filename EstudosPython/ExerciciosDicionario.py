"""#Exercício 1
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

print(f"{frutas}")"""