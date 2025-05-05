# Exemplo de Orientação a Objetos

## The Sims Imaginário

class Pessoa:

    def __init__(self, nome, idade, cidade="Não informado!"):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def ():
        # TODO: Conecta ao banco e atualiza TODAS as pessoas.
        # TODO: Criar essa função fora da classe

    def andar(self):
        print(f"{self.nome} está andando.")
atualizar
    def falar(self):
        print(f"{self.nome} está falando.")

    def dormir(self):
        print(f"{self.nome} está dormindo.")

    def adotar(self, crianca):
        print(f"{self.nome} adotou {crianca.nome}.")

    def get_cidade(self):
        print(f"{self.nome} mora em {self.cidade}.")

class Crianca(Pessoa):
    def __init__(self, nome, idade, responsavel: Pessoa=None):
        super().__init__(nome, idade)
        self.responsavel = responsavel
        if responsavel:
            self.cidade = responsavel.cidade
            print(f"{self.nome} é filho(a) de {responsavel.nome} e mora em {self.cidade}.")

    def brincar(self):
        print(f"{self.nome} está brincando.")

elias = Pessoa("Elias", 25)
elias.andar()
elias.falar()
elias.cidade = "Campo Mourão"
joazinho = Crianca("Joazinho", 10, elias)
# ... um milhao de pessoas
elias.get_cidade()
joazinho.get_cidade()
joazinho.brincar()