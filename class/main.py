from GameManager import GameManager


def main_menu():
    print(f"********************")
    print(f"*Power Grid Master!*")
    print(f"********************")

    print("1. New Game")
    print("2. Exit")

    print('Enter your option:')
    return int(input())

def bye():
    print("Thanks for playing!")
    print("Good bye")
    print("")

while(True):
    # let's play !
    option = main_menu()
    if option != 1:
        bye()
        break


