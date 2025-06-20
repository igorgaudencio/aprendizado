def par_ou_impar():
    entrada = input("Digite um número inteiro: ")
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida, por favor digite um número inteiro.")
        return
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

par_ou_impar()