from random import randint
import argparse
import os

def tries():
    TRIES = 0

    parser = argparse.ArgumentParser(description="Gra: Zgadnij losową liczbę")

    parser.add_argument('--max-tries', type=int, default=5, help=('maksymalna cyfra to 5'))
    parser.add_argument('--max', type=int, default=100, help=('maksymalny zakres wynosi 100'))
    parser.add_argument('--min', type=int, default=0, help=('minimalny zakres wynosi 1'))

    args = parser.parse_args()
    MAX_TRIES: int = args.max_tries
    MAX: int = args.max
    MIN: int = args.min

    args = parser.parse_args()


    return TRIES,MAX_TRIES,MAX,MIN,parser


def win() -> str:
    clear = lambda: os.system('cls')

    WIN_ASK: str = input("Czy chcesz zagrać jeszcze raz? y/n ")
    if WIN_ASK == "y":
        clear()
        print("-" * 20)
        print("Zaczynasz od nowa")
        print("-" * 20)
        game()

    if WIN_ASK == "n":
        print("\n")
        print("-" * 20)
        print("Koniec Gry")
        print("-" * 20)


    return WIN_ASK

def game():

    TRIES, MAX_TRIES,parser,MAX,MIN = tries()
    DIGIT: int = randint(1,100)
    # print(DIGIT)
    print("-" * 20)
    print("GRA: Znajdz wylosowaną liczbę")
    print("-" * 20)
    print(f"- Pozostało {MAX_TRIES} prób")
    print("-" * 20)
    ASK: int = input("Podaj liczbę która została wylosowana: ")

    while True:

        MAX_TRIES -= 1
        print(f"\n - Pozostało {MAX_TRIES} prób \n")


        try:

            if int(ASK) > DIGIT:
                print(" - Podana liczba jest większa niż wylosowana! \n")
                ASK: int = input("Podaj liczbę która została wylosowana: ")

            if int(ASK) < DIGIT:
                # if int(ASK) < MIN:
                #     print("!"*20)
                #     print("Zakres wynosi 1-100!")
                #     print("!"*20)

                print(" - Podana liczba jest mniejsza niż wylosowana! \n")
                ASK: int = input("Podaj liczbę która została wylosowana: ")

            TRIES += 1


            if DIGIT == int(ASK):
                print(f"Brawo! To ta liczba!\n")
                print("-"*20, f"\n - Wylosowana liczba to: {DIGIT} | Liczba prób: {TRIES}")

                return win()

            if MAX_TRIES <= 1:
                print("-" *20, '\n')
                print(f"Wykorzystano Wszystkie próby \n")
                print(f"Liczba która była wylosowana to: {DIGIT}")
                print('\n', "-" *20,'\n')

                return win()
        except:
                print(" - Podano złą wartość*")
                print(" - Wymaganą wartością jest liczba*")
                return win()


game()
