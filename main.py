from random import randint
import argparse

def tries():
    TRIES = 0

    parser = argparse.ArgumentParser(description="Gra: Zgadnij losową liczbę")

    parser.add_argument('--max-tries', type=int, default=5, help=('maksymalna cyfra to 5'))
    parser.add_argument('--max', type=int, default=100, help=('maksymalny zakres wynosi 100'))
    parser.add_argument('--min', type=int, default=1, help=('minimalny zakres wynosi 1'))

    args = parser.parse_args()
    MAX_TRIES = args.max_tries
    MAX = args.max
    MIN = args.min

    args = parser.parse_args()


    return TRIES,MAX_TRIES,MAX,MIN,parser


def win():
    WIN_ASK = input("Czy chcesz zagrać jeszcze raz? y/n ")
    if WIN_ASK == "y":
        print("-" * 50, "\n\n\n")
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
    # TRIES = tries()
    DIGIT = randint(1,100)
    print(DIGIT)
    print("-" * 20)
    # print(parser.description)
    print("-" * 20)
    print(f"- Pozostało {MAX_TRIES} prób")
    print("-" * 20)
    ASK = input("Podaj liczbę która została wylosowana: ")

    while True:


        if int(ASK) > DIGIT:
            print(" - Podana liczba jest większa niż wylosowana!")
            ASK = input("Podaj liczbę która została wylosowana: ")

        if int(ASK) < DIGIT:
            print(" - Podana liczba jest mniejsza niż wylosowana!")
            ASK = input("Podaj liczbę która została wylosowana: ")

        TRIES += 1
        MAX_TRIES -= 1
        print(f"- Pozostało {MAX_TRIES} prób")


        if DIGIT == int(ASK):
            print(f"Brawo! To ta liczba!\n")
            print("-"*20, f"\n - Wylosowana liczba to: {DIGIT} | Liczba prób: {TRIES}")

            return win()

        if MAX_TRIES <= 0:
            print(f"Wykorzystano Wszystkie próby")

            return win()


game()
