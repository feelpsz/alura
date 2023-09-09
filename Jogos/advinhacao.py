import random

def jogar():

    print("******************************************************************")
    print("*****************Bem-vindo ao jogo de advinhação!*****************")
    print("********Você terá 5 chances para advinhar o número secreto********")
    print("******************************************************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000
    dificuldade = int(input("Digite o nível de digiculdade que deseja (1 - Fácil; 2 - Intermediário; 3 - Difícil) "))


    if(dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    elif(dificuldade == 3):
        tentativas = 5

    print("Você escolheu o nível {} e terá apenas {} tentativas".format(dificuldade,tentativas))

    for rodada in range(1, tentativas +1):

        print("Tentativa {} de {}".format(rodada,tentativas))
        chute_str = input("Digite o seu palpite (Número entre 1 e 100): ")
        print("Você digitou {}".format(chute_str))
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve palpitar um número de 1 a 100!")
            continue

        acerto = chute == numero_secreto
        acerto_msg = "Parabéns, você advinhou o número secreto!"
        maior = chute > numero_secreto
        maior_msg = "O seu chute foi maior que o número secreto!"
        menor = chute < numero_secreto
        menor_msg = "O seu chute foi menor que o número secreto!"
        pontos_msg = "Você obteve um total de {} pontos".format(pontos)

        if(acerto):
            print(acerto_msg)
            print(pontos_msg)
            break
        else:
            if(maior):
                print(maior_msg)
            elif(menor):
                print(menor_msg)

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print("Fim de jogo!")


if(__name__ == "__main__"):
    jogar()