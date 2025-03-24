from utils.banco import criar_conta, exibe_conta
from utils.config import contas

print("** Banco da Codaqui **")

# --------------------- #
# - Criação de Contas - #
criar_conta(contas=contas, nome="Elias", saldo=1000)
criar_conta(contas=contas, nome="Letycia", saldo=2000, cidade="São Paulo")
# --------------------- #

exibe_conta(contas=contas, id=2)

# --------------------- #
# print("Uma função é um bloco de código que executa uma tarefa específica. Normalmente ela tem parametros e retorno.")
# print("Um metódo é uma função que pertence a uma classe.")
# print("Um procedimento é uma função que não tem retorno.")
# --------------------- #


# Como sacar?
# Como depositar?
# Como transferir?
# Como exibir o saldo?
