# Meu primeiro comentário
# Apresentando meu primeiro algoritmo
dia = input("Que dia é hoje?!")
valid_days = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
if dia not in valid_days:
    print("Dia inválido")
    exit()
if dia == "quinta":
    print("Hoje é dia de feira, não preciso me trocar!")
elif dia == "terça":
    print("Hoje é dia de aula de música!")
print("Pegar o elevador")
print("Ir na venda")
print("Comprar chiclete")
chiclete = 0
while chiclete < 10:
    print("Mascar chiclete")
    chiclete += 1
    if chiclete == 9:
        print("Está ficando sem gosto!")
print("Jogar chiclete fora")
