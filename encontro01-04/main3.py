import tqdm
import time

def receber_numero() -> float | int:
    numero: str = input("Digite um número:")
    if '.' in numero:
        numero = float(numero)
    elif ',' in numero:
        numero = numero.replace(',', '.')
        numero = float(numero)
    elif numero.isdigit():
        numero = int(numero)
    else:
        print("Erro ao processar dados!")
        exit(1)
    return numero


numero: float | int = receber_numero()
numero_2: float | int = receber_numero()
operacao: str = input("Digite a operação (+, -, *, /):")
match operacao:
    case '+':
        resultado: float | int = numero + numero_2
        print(f"Resultado: {resultado}")
    case '-':
        resultado: float | int = numero - numero_2
        print(f"Resultado: {resultado}")
    case '*':
        resultado: float | int = numero * numero_2
        print(f"Resultado: {resultado}")
    case '/':
        try:
            resultado: float | int = numero / numero_2
            print(f"Resultado: {resultado}")
        except ZeroDivisionError:
            print("Divisão por zero!")
    case _:
        print("Operação inválida!")
        exit(1)

# if operacao not in operacoes_validas:
#    print("Operação inválida!")
#    exit(1)
# if operacao == '+':
#    resultado: float | int = numero + numero_2
#    print(f"Resultado: {resultado}")

nome = "ENDERSON MENEZES CANDIDO"
print(dir(nome))
nome = nome.split(' ')
print(nome)
print(type(nome))
for palavra in nome:
    print(palavra.capitalize(), end=' ')

numero_novo = receber_numero()
if numero_novo > 5:
    print("Número maior que 5")
    contador = 0
    with tqdm.tqdm(total=numero_novo) as pbar:
        while contador < numero_novo:
            time.sleep(1)
            contador += 1
            pbar.update(1)
        
elif numero_novo < 5:
    print("Número menor que 5")
elif numero_novo == 5:
    print("Número igual a 5")
else:
    print("Número inválido!")
    exit(1)




