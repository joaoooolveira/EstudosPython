"""#Exercício 1
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
        print("Digite apenas números.")"""

#Exercício 5
while True:
    try:
        preco = float(input("Digite o preço do produto: R$"))
        print(f"Preço registrado: R${preco:.2f}")
        break
    except:
        print("Preço inválido.")