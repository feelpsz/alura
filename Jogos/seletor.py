import advinhacao
import forca

print("*************************")
print("***Escolha o seu jogo!***")
print("*************************")

print("1 - Jogo da Advinhação")
print("2 - Jogo da Forca")

jogo = int(input("Digite o jogo que deseja executar: "))

if(jogo == 1):
    print("Executando o jogo da Advinhação!")
    advinhacao.jogar()
elif(jogo == 2):
    print("Executando o jogo da Forca!")
    forca.jogar()
