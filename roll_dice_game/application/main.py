import random
rollDice = input("Do you wanna roll a dice(y/n)?").capitalize()

def dice():
    return random.randrange(1, 6)

if rollDice == "Y":
    numeroSelecionado = int (input("Choose a number between 1 and 6: "))
    if(numeroSelecionado == dice()):
        print("Congratulations you choose the rigth number")
    else:
        print("Wrong number!")
else:
    print("Closing program.")
