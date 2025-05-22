# Lotto program in Python
# Created by: David Szalanics
# Source: https://github.com/Norrbot/lotto

# Import section
import random
import time
import os

# Functions / procedures / definitions
def generate_lotto(total, max_number):  # Random number generator
    return random.sample(range(1, max_number + 1), total)

def clear_screen():  # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():  # Separator line for clearer output
    print("----------------------------------------------------------")

def delay(seconds):  # Delay
    time.sleep(seconds)

def HUN():
    while True:
        clear_screen()
        print("Üdvözöllek Játékos!")  # A játékos üdvözlése
        delay(1)

        print("Válaszd ki, hogy milyen lottón szeretnél játszani?")  # Interaktív bekérés
        print("1-Hatos, 2-Ötös, 3-Skandináv, 4-Euro Jackpot, 5-Kilépés")
        tipus = input("")

        print("")
        delay(1)
        print("Számok kalkulálása...")  # Program üzenet
        delay(1)

        # Input vizsgálatok
        if tipus == "1":
            print_separator()
            print("A generált hatos lottószámok:", generate_lotto(6, 45))

        elif tipus == "2":
            print_separator()
            print("A generált ötös lottószámok:", generate_lotto(5, 90))

        elif tipus == "3":
            print_separator()
            print("A generált skandináv lottószámok:", generate_lotto(7, 35))

        elif tipus == "4":
            print_separator()
            print("A generált euro jackpot számok V1:", generate_lotto(5, 50))
            print("A generált euro jackpot számok V2:", generate_lotto(2, 12))

        elif tipus == "5":  # Kilépési feltétel
            print_separator()
            print("Köszönöm, hogy játszottál!")
            print("Viszlát!")
            delay(1)
            clear_screen()
            break  # Kilépés

        else:
            print_separator()
            print("HIBA! Nincs ilyen típus!")

        input("\nNyomj ENTER-t a folytatáshoz...")

def EN():
    while True:
        clear_screen()
        print("Welcome, Player!")  # Greeting the player
        delay(1)

        print("Choose the type of lotto you want to play:")
        print("1 - Six-number lotto, 2 - Five-number lotto, 3 - Scandinavian, 4 - Euro Jackpot, 5 - Exit")
        choice = input("")

        print("")
        delay(1)
        print("Calculating numbers...")  # Program message
        delay(1)

        # Input evaluation
        if choice == "1":
            print_separator()
            print("Generated six-number lotto numbers:", generate_lotto(6, 45))

        elif choice == "2":
            print_separator()
            print("Generated five-number lotto numbers:", generate_lotto(5, 90))

        elif choice == "3":
            print_separator()
            print("Generated Scandinavian lotto numbers:", generate_lotto(7, 35))

        elif choice == "4":
            print_separator()
            print("Generated Euro Jackpot numbers V1:", generate_lotto(5, 50))
            print("Generated Euro Jackpot numbers V2:", generate_lotto(2, 12))

        elif choice == "5":  # Exit condition
            print_separator()
            print("Thank you for playing!")
            print("Goodbye!")
            delay(1)
            clear_screen()
            break

        else:
            print_separator()
            print("ERROR! Invalid choice!")

        input("\nPress ENTER to continue...")

# Main program
lang = input("Please select the language / Válassz nyelvet (1-HUN, 2-EN): ")

if lang == "1":
    HUN()
elif lang == "2":
    EN()
else:
    EN()
