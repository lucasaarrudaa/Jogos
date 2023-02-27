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

# posso criar listas de valores
#valores = [0,1,2,3,4] pode misturar com strings, mas n faz sentido
#se há algum valor dentro da minha lista
# 6 in valores retorna False
# 3 in valores retorna True
# "a" in "banana" retorna true
# para acessar o valor na 5 posição: valores[5] retorna 4
#min(valores) max(valores) len(valores) funcoes de lista
# valores.append(7) adiciona +1 valor
# valores.pop() retorna o ultimo elemento, e também remove ele.

### posso colocar meus tuples dentro da minha lista.
# e depois acessar cada um elemento da lista e também posso acessar s[o um elemento da minha tuple, dentro da lista
# o contrário também é valido!!
# ex:
# p1 = ("nico", 39)
# p2 = ("caio", 30)

# instrutores = [p1,p2]
# instrutores retorna: [("nico", 39), ("caio", 30)]
#  retorna: ("nico", 39)
# instrutores[0][1] retorna: 39.

# ex2: se eu preciso ler dados de um arquivo, n sei quantas linhas tem um arquivo...
# como n sei quantas palavras tem um arquivo, tem que usar essa lista e alimentar essa lista.
# palavras = [] fico lendo la, cada vez q eu acho uma linha no meu arquivo eu vou chamar append, adicioanr uma nova palavra nessa lista
# palavras.append("banana")
# palavras.append("abacaxi")
# agr nao quero q ninguem mexa no arquivo, agora uso um tuple.
# funcao tuple()
# nova = tuple(palavras)
# nova retorna: ("banana", "abacaxi")
# outra funcao list()
# outra = list(nova)
# outra retorna: ["banana","abacaxi"]
# ---------- SET ----------------
#   Não tem índice
#   Nao permite duplicados
# ---------- DICIONÁRIO ----------
# instrutores = {"nico" : 39, "caio" : 30}
# * É SEMPRE EM PARES CHAVE E VALOR.
# Se nao soubessemos a idade de nico e tivéssemos só o nome, poderiamos saber:
# instrutores["nico"] retorna: 39
# COMO ABRIR ARQUIVO PYHTON
# arquivo = open("nomearquivo.txt, leitra,escrita...") w = escrita, r = leitura , a = de append que é adicionar/incrementar conteudo
#arquivo = "palavras.txt", "w"
# a escerita apaga os arquivo, caso exista já uma rquivo com esse nome nesse codigo, caso nao queira apagar
# arquivo retorna o arquivo, nome, mode que é o w; r; a; b; e o encoding que é o tipo de caracteres que ele usa.
#arquivo = open("palavras.txt", "w")              o b abre o arquivo no modo binario. ex rb cria uma copia. e wb tambem
# arquivo.write("banana") retorna: 6 que é aquantidade de caracteres que ele escreveu no arquivo
# arquivo.write("melancia")
# arquivo.close()
# boa prática fechar o arquivo, pq quando ele abre o arquivo, o python pede o sistema operacional no canal de comunicacao
# esse canal que ta aberto agora, ta dando trabalho para o sistema operacional
# se chamar o arquivo palavras.txt vai retornar: bananamelancia
# arquivo = open("palavras.txt", "a") retorna bananamelancia
# se eu quiser fazer novas linhas
# arquivo.write("morango\n")
# arquivo.write("maça\n")
# arquivo.close()
# ele abriu o conteudo mas ficou na mesma linha.. maça ta na proxima.
# retorna:
# bananamelanciamorango
# maça
# arquivo = open("frutas.txt", r")
# para ler um arquivo e ler denovo, tem que fechar ele, porque ele fica com a posicao no ultimo caractere. se retornar antes de fechar, vai retornar string  vazia.
# for linha in arquivo retorna: linha por linha
# print(linha) vai retornar todas as linhas
#
# a função print adiciona um \n no final., mas mesmo assim já tinha um.. o print itnha um (linha, end="n") no final, embutidfo
# se quisermos apenas uma linha, usa a funcao readLine()
# arquivo = open("palavras.txt","r")
# linha = arquivo.readLine()
# ao final de cada palavra, há um \n ao final de cada linha, de cada palavra, mas
# oara returar is espaços em branco no comeco e final da string, usa .strip()
# essa funcao também remove caracteres especiais como o \n
# print(linha.)
# se der algum erro na leitura do arquivo, podemos chamar o with
# ex: with open("frutas.txt") as arquivo:
#       for linha in arquivo:
#           print(linha)