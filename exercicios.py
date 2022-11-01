turno = input(str("Digite o turno de estudo (M/T/N): ".replace("m","M")))

if(turno == "M"):
    print("Bom dia!")
else:
    if(turno == "T"):
        print("Boa tarde!")
    elif(turno == "N"):
        print("Boa noite!")
    elif(turno != "M" or turno != "T" or turno != "N"):
        print("Turno Inválido!")