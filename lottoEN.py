# Lotto program in Python (English version)
# Created by: Szalanics Dávid
# Source: https://github.com/Norrbot/lotto 
# Last modified: 2025. 05. 18.

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
    time.sleep(seconds)  # Built-in function, extracted for readability

# Program body (or main function if you prefer)
while True:  # Infinite loop
    clear_screen()
    print("Welcome, Player!")  # Greeting the player
    delay(1)

    print("Choose the type of lotto you want to play:")  # Interactive input
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
        print("Generated Euro Jackpot numbers V1:", generate_lotto(5, 50))  # Euro Jackpot has two sets
        print("Generated Euro Jackpot numbers V2:", generate_lotto(2, 12))  # of output numbers

    elif choice == "5":  # Exit condition
        print_separator()
        print("Thank you for playing!")  # Farewell message
        print("Goodbye!")
        delay(1)
        clear_screen()
        break  # Exit

    else:  # Error handling
        print_separator()
        print("ERROR! Invalid choice!")

    input("\nPress ENTER to continue...")  # To continue
