from random import randint
import argparse
import os
def tries():
    attempts = 0
    parser = argparse.ArgumentParser(description="Gra: Zgadnij losową liczbę")
    parser.add_argument('--max-attempts', type=int, default=5, help=('- Maksymalna cyfra to 5'))
    parser.add_argument('--max_number', type=int, default=100, help=('- Zakres górny wynosi 100'))
    parser.add_argument('--min_number', type=int, default=0, help=('- Zakres dolny zakres wynosi 1'))
    args = parser.parse_args()
    max_attempts: int = args.max_attempts
    min_number: int = args.min_number
    max_number: int = args.max_number
    args = parser.parse_args()

    return attempts,max_attempts,args,max_number,min_number
def limit_numbers(max_number,min_number):
    attempts,max_attempts,args,max_number,min_number = tries()
    max_number = 100
    min_number = 0
if __name__ == '__limit_numbers__':
    limit_numbers()
def win(win_game, clear_screen = False) -> str:
    def clear_screen():
        clear = os.system('cls')

    win_game: str = input("Czy chcesz zagrać jeszcze raz? y/n ")
    if win_game == "y":
        # clear_screen()
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
    attempts,max_attempts,args,max_number,min_number = tries()
    number_drawn: int = randint(1,100)
    print("-" * 20)
    print("GRA: Znajdz wylosowaną liczbę")
    print("-" * 20)
    while True:

        try:
            guess_number: int = input("Podaj liczbę która została wylosowana: ")
            print(f"\n - Pozostało {max_attempts} prób \n")
            if int(guess_number) > number_drawn:
                print(" - Podana liczba jest większa niż wylosowana! \n")
            if int(guess_number) < number_drawn:
                print(" - Podana liczba jest mniejsza niż wylosowana! \n")
            attempts += 1
            if int(guess_number) > max_number:
                print(" - Zakres górny wynosi 100! \n")
            if int(guess_number) < min_number:
                print(" - Zakres dolny wynosi 1! \n")
        except ValueError as e:
                print(" - Podano złą wartość*")
                print(" - Wymaganą wartością jest liczba*")
                print(f"{e}")
                return win(win_game="")
        finally:
            max_attempts -= 1
        if number_drawn == int(guess_number):
            print(f"Brawo! To ta liczba!\n")
            print("-"*20, f"\n - Wylosowana liczba to: {number_drawn} | Liczba prób: {attempts}")
            return win(win_game="")
        if max_attempts < 0:
            print("-" *20, '\n')
            print(f"Wykorzystano Wszystkie próby \n")
            print(f"Liczba która była wylosowana to: {number_drawn}")
            print('\n', "-" *20,'\n')
            return win(win_game="")

if __name__ == '__main__':
    main()