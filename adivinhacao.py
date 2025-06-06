import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1,100)
    tentativas = 0
    print("🎯 Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    while True:
        try: 
            palpite = int(input("Digite seu palpite: "))
            tentativas +=1
            if palpite < 1 or palpite > 100:
                print("Numero inválido")
                continue
            if palpite < numero_secreto:
                print("Número baixo")
            elif palpite > numero_secreto:
                print("Número alto")
            else:
                print(f"Parabéns, você acertou em {tentativas} chances")
                break
        except ValueError :
            print("Entrada errada, digite um número inteiro")


jogo_adivinhacao()