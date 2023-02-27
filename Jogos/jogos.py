import forca
import jogoadivinhacao

print("*********************************")
print("Escolha o seu jogo!")
print("*********************************")
print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual Jogo?"))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
    
elif (jogo == 2):
    print("Jogando adivinhação")
    jogoadivinhacao.jogar()
