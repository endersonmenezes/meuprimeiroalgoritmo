# Alguma coisa acontece
print("Bueah Bueah Bueah!")

# Varias coisas aconteçam
print("Papai, mamãe!")

# Recebe informação
nome: str = input("Qual é o seu nome?")
texto: str = f"Olá, {nome}!"

if nome == "Enderson":
    print("Seja bem vindo administrador do sistema!")
elif nome == "Elias":
    print("Seja bem vindo aluno!")
else:
    print("Seja bem vindo visitante!")


match nome:
    case "Enderson":
        print("Seja bem vindo administrador do sistema!")
    case "Elias":
        print("Seja bem vindo aluno!")
    case _:
        print("Seja bem vindo visitante!")

# Números (Inteiros, Pontos Flutuantes)
numero = int(input("Digite um número:"))
if numero > 0:
    print("Número positivo")
    if numero == 20:
        print("Número é 20")
elif numero < 0:
    print("Número negativo")

# Booleanos

# Texto
print(texto)

