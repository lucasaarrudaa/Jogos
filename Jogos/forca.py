import random

def variaveis_jogo():
    acertou = False
    enforcou = False
    erros = 0
    acertos = 0
    return acertou, enforcou, erros, acertos

def aviso_letras_e_quantidade_de_letras(letras_acertadas):
    print(letras_acertadas)
    print("Você pode errar 7 vezes")

def parametro_acertar_e_errar(letras_acertadas, erros):
    acertou = "_" not in letras_acertadas
    enforcou = erros == 7
    return acertou, enforcou

def jogar():
    boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    aviso_letras_e_quantidade_de_letras(letras_acertadas)
    acertou, enforcou, erros, acertos = variaveis_jogo()

    while (not enforcou and not acertou):

        chute = pede_chute()                 ##strip tira os espaços em branco
        if (chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas, acertos)
        else:
            erros += 1
            jogadas_restantes = 7 - erros
            marcou_chute_errado(jogadas_restantes)
            desenha_forca(erros)
            print(letras_acertadas)

        acertou, enforcou = parametro_acertar_e_errar(letras_acertadas, erros)
        mensagem_ganhador(acertou)
        mensagem_enforcado(enforcou, palavra_secreta)

    fim_de_jogo()

def boas_vindas():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("frutas.txt", "r")
    frutas = []

    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)

    arquivo.close()
    frutas_aleatorias = random.randrange(0, len(frutas))
    palavra_secreta = frutas[frutas_aleatorias].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas

def pede_chute():
    chute = (input("Digite uma letra:  \n"))
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, chute, letras_acertadas, acertos):
    index = 0
    for letra in palavra_secreta:  # para cada letra na palavra secreta, se o chute for = a letra, o index acrescenta 1. na posição da letra na lista_palavra_acertada
        if (chute == letra.upper()):
            print("encontrei a letra {} na posição {}".format(letra, index))
            letras_acertadas[index] = letra
        index += 1
    acertos += 1
    print(letras_acertadas)

def marcou_chute_errado(jogadas_restantes):
    print("ERROU! Você tem {} jogadas restantes".format(jogadas_restantes))

def mensagem_ganhador(acertou):
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def mensagem_enforcado(enforcou, palavra_secreta):
    if enforcou:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def fim_de_jogo():
    print("       ....FIM DE JOGO....")

if(__name__ == "__main__"):
    jogar()
