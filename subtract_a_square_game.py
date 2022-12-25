# My name is Kareem Hasseeb, Iam a student at FCAI_CU <3
# main menu
import random
# main menu
print("           Subtract a square          ")


def turnChecker(n):
    if n % 2 == 0:
        turn = player1
    else:
        turn = player2
    return turn


restart = 1
while restart != "x":
    player1 = input("Enter Player1 Name: ")
    if player1 == "":
        player1 = "Player1"
    player2 = input("Enter Player2 Name: ")
    if player2 == "":
        player2 = "Player2"
    coinsNum = random.randint(10, 101)
    squares = []
    for p in range(1, coinsNum):
        squares.append(p * p)
    counter = 0
    print("\n\n♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n\n")
    print("Enter a square : ")
    while coinsNum > 1:
        print("\n", coinsNum, "\n")
        while True:
            try:
                l = int(input("{} turn: ".format(turnChecker(counter))))
            except ValueError:
                print("You must enter a number")
                continue
            if l in squares:
                break
            print("The number must be square number")

        if coinsNum > l:
            coinsNum -= l
            counter += 1
    print("\n", coinsNum, "\n")
    print( turnChecker(counter-1), "WINS !")
    restart = input("press any key to start again, or x to exit. ")