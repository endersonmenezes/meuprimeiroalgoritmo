# Benchmark entre Try/Except e dict.get()

## Dependências
import timeit
import random

## Start up
dicionario_vazio = {}
dicionario_pequeno = {"nome": "Elias", "saldo": 1000}
dicionario_grande = {"nome": "Elias", "saldo": 1000, "cidade": "São Paulo", "estado": "SP", "pais": "Brasil"}
dicionario_random_gigante = {}
for i in range(1000):
    # random word
    random_word = ""
    for j in range(10):
        random_word += chr(random.randint(65, 90))
    random_key = ""
    for j in range(10):
        random_key += chr(random.randint(65, 90))
    dicionario_random_gigante[random_word] = i

random_key_to_test = random.choice(list(dicionario_random_gigante.keys()))

## Funções
def try_except(dicionario, key):
    try:
        return dicionario[key]
    except KeyError:
        return None
    
def dict_get(dicionario, key="nome"):
    return dicionario.get(key)


## Testes Rápidos
quantidade_de_vezes = 1000000
print("-----------")
print("Dicionário Vazio")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_vazio, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_vazio), number=quantidade_de_vezes))
print("\n")
print("Dicionário Pequeno")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_pequeno, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_pequeno), number=quantidade_de_vezes))
print("\n")
print("Dicionário Grande")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_grande, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_grande), number=quantidade_de_vezes))
print("\n")
print("Dicionário Random Gigante")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_random_gigante, random_key_to_test), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_random_gigante), number=quantidade_de_vezes))
print("\n")

## Teste Médio
quantidade_de_vezes = quantidade_de_vezes * 10
print("-----------")
print("Dicionário Vazio")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_vazio, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_vazio), number=quantidade_de_vezes))
print("\n")
print("Dicionário Pequeno")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_pequeno, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_pequeno), number=quantidade_de_vezes))
print("\n")
print("Dicionário Grande")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_grande, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_grande), number=quantidade_de_vezes))
print("\n")
print("Dicionário Random Gigante")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_random_gigante, random_key_to_test), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_random_gigante, random_key_to_test), number=quantidade_de_vezes))
print("\n")

## Teste Longo
quantidade_de_vezes = quantidade_de_vezes * 100
print("-----------")
print("Dicionário Vazio")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_vazio, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_vazio), number=quantidade_de_vezes))
print("\n")
print("Dicionário Pequeno")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_pequeno, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_pequeno), number=quantidade_de_vezes))
print("\n")
print("Dicionário Grande")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_grande, "nome"), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_grande), number=quantidade_de_vezes))
print("\n")
print("Dicionário Random Gigante")
print("Try/Except: ", timeit.timeit(lambda: try_except(dicionario_random_gigante, random_key_to_test), number=quantidade_de_vezes))
print("Dict.Get: ", timeit.timeit(lambda: dict_get(dicionario_random_gigante, random_key_to_test), number=quantidade_de_vezes))
print("\n")