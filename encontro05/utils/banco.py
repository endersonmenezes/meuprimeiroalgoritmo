def criar_conta(contas, nome, saldo, cidade=None):
    id = len(contas) + 1
    conta = {
        "id": id,
        "nome": nome,
        "saldo": saldo,
        "cidade": cidade
    }
    contas[id] = conta
    return conta

def exibe_conta(contas, id):
    conta = contas.get(id)
    if not conta:
        print("Conta não encontrada")
        return
    print("---")
    print("Nome:", conta["nome"])
    print("Saldo:", conta["saldo"])
    print("ID:", conta["id"])
    print("Cidade:", conta.get("cidade", "Não informada"))
    try:
        print("Cidade:", conta["cidade"])
    except KeyError:
        print("Cidade: Não informada")
    print("---")