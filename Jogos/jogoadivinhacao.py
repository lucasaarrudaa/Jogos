import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    pontos = 1000
    numero_secreto = int(random.randrange(1, 101))
    total_de_tentativas = 0
    niveis = ["(1) Fácil" ,"(2) Médio" ,"(3) Díficil"]
    print("---------------------------------")
    print("Qual o nível de dificuldade?")
    print("---------------------------------")
    print(niveis[0], niveis[1], niveis[2])

    nivel = int(input("Defina o Nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
        print("---------------------------------")
        print("Você tem 20 tentativas")
    elif (nivel == 2):
        total_de_tentativas = 10
        print("---------------------------------")
        print("Você tem 10 tentativas")
    elif (nivel == 3):
        total_de_tentativas = 5
        print("---------------------------------")
        print("Você tem 5 tentativas")

    for rodada in range(1, total_de_tentativas + 1):
        print("---------------------------------")
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou! e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior do que o número secreto. \n")
                print("pontos:", pontos)
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = abs(pontos - pontos_perdidos)
            elif (menor):
                print("Você errou! O seu chute foi menor do que o número secreto. \n")
                print("pontos:", pontos)
                pontos_perdidos = abs(numero_secreto - chute) # 40 - 20 = 20 o sinal nao importa, como fazer um numero absoluto com python?
                pontos = abs(pontos - pontos_perdidos) #função abs () chute = 4 pontos = 100 numer secre = 96
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(
                          numero_secreto, pontos))
    print ("Fim do jogo")
if(__name__=="__main__"):
    jogar()

