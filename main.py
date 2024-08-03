import argparse
import os
from random import randint


def parse_args():
    parser = argparse.ArgumentParser(description="Gra: Zgadnij losową liczbę")
    parser.add_argument(
        "--max-attempts",
        type=int,
        default=5,
        help=("- Maksymalna cyfra to 5"),
    )
    parser.add_argument(
        "--max_number",
        type=int,
        default=100,
        help=("- Zakres górny wynosi 100"),
    )
    parser.add_argument(
        "--min_number",
        type=int,
        default=0,
        help=("- Zakres dolny zakres wynosi 1"),
    )
    parser.add_argument("--attempts", type=int, default=0, help=("- Liczba prób"))

    args = parser.parse_args()
    return args


def display_message_after_win(win_game, clear_screen=True) -> str:
    win_game: str = input("Czy chcesz zagrać jeszcze raz? y/n ")
    clear_screen = os.system("cls")

    if win_game == "y":
        clear_screen
        print("-" * 20)
        print("Zaczynasz od nowa")
        print("-" * 20)
        main()
    if win_game == "n":
        print("\n")
        print("-" * 20)
        print("Koniec Gry")
        print("-" * 20)
    return win_game

def main():
    args = parse_args()
    number_drawn: int = randint(1, 100)
    print("-" * 20)
    print("GRA: Znajdz wylosowaną liczbę")
    print("-" * 20)
    while True:
        try:
            guess_number: int = input("Podaj liczbę która została wylosowana: ")
            print(f"\n - Pozostało {args.max_attempts} prób \n")
            if int(guess_number) > number_drawn:
                print(" - Podana liczba jest większa niż wylosowana! \n")
            if int(guess_number) < number_drawn:
                print(" - Podana liczba jest mniejsza niż wylosowana! \n")
            args.attempts += 1
            if int(guess_number) > args.max_number:
                print(" - Zakres górny wynosi 100! \n")
            if int(guess_number) < args.min_number:
                print(" - Zakres dolny wynosi 1! \n")
        except ValueError as e:
            print(" - Podano złą wartość*")
            print(" - Wymaganą wartością jest liczba*")
            print(f"{e}")
            return display_message_after_win(win_game="")
        finally:
            args.max_attempts -= 1
        if number_drawn == int(guess_number):
            print("Brawo! To ta liczba!\n")
            print("-" * 20,f"\n - Wylosowana liczba to: {number_drawn} | Liczba prób: {args.attempts}")
            return display_message_after_win(win_game="")
        if args.max_attempts < 0:
            print("-" * 20, "\n")
            print("Wykorzystano Wszystkie próby \n")
            print(f"Liczba która była wylosowana to: {number_drawn}")
            print("\n", "-" * 20, "\n")
            return display_message_after_win(win_game="")

if __name__ == "__main__":
    main()
