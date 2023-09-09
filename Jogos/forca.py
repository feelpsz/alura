import random
def jogar():

    imprime_abertura()
    palavra_secreta = lista_palavras()
    letras_certas = run_letras_certas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    print("A palavra possuí {} letras!".format(len(palavra_secreta)))


    while(not enforcou and not acertou):

        chute = input("Digite o seu chute: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas[index] = letra
                index += 1
        else:
            erros += 1
            print("Errou! Você possuí {} tentativas!".format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = "_" not in letras_certas
        print(letras_certas)

    if(acertou):
        print("Parabéns, você acertou a palavra secreta! {}".format(palavra_secreta))
    else:
        print("Você errou! A palavra secreta era {}, tente outra vez!".format(palavra_secreta))
    print("Fim do jogo!")

def imprime_abertura():
    print("******************************************************************")
    print("*******************Bem-vindo ao jogo de forca!!*******************")
    print("*******Você terá 5 chances para advinhar a Palavra Secreta!*******")
    print("******************************************************************")

def lista_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def run_letras_certas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


if(__name__ == "__main__"):
    jogar()
