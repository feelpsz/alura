numero_secreto = 42
tentativas = 5

for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite um número de 1 a 100: ")
    print("Você digitou {}".format(chute_str))
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número de 1 a 100!")
        continue


    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    acerto_msg = "Parabéns, você acertou!"
    maior_msg = "Você errou! O seu chute foi maior que o número secreto!"
    menor_msg = "Você errou! O seu chute foi menor que o número secreto!"

    if (acerto):
        print(acerto_msg)
        break
    else:
        if (maior):
            print(maior_msg)
        elif (menor):
            print(menor_msg)

print("Fim de jogo!")