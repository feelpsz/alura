
def jogar():


    print("******************************************************************")
    print("*******************Bem-vindo ao jogo de forca!!*******************")
    print("*******Você terá 5 chances para advinhar a Palavra Secreta!*******")
    print("******************************************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Digite o seu chute: ")
        chute = chute.strip()
        index = 0
        index = index + 1

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("A letra {} foi encontrada na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")


if(__name__ == "__main__"):
    jogar()