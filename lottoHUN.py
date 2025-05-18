# Lottó program Python nyelven Magyarul
# Készítette: Szalanics Dávid
# Letölthető: https://github.com/Norrbot/lotto 
# Utolsó módosítás: 2025. 05. 18.

# Import sorok
import random
import time
import os

# Fügvények/eljárások/deffiníciók
def generate_lotto(total, max_number): # Random szám generátor
    return random.sample(range(1, max_number + 1), total)

def clear_screen(): # Képernyő törlés
    os.system('cls' if os.name == 'nt' else 'clear')

def vonal(): # Vonal, az átláthatóbb kimenetért
    print("----------------------------------------------------------")
    
def delay(ertek_mpben): # Várakozás
    time.sleep(ertek_mpben) # Beépített függvény, csak az étnevezés miatt lett kiszervezve

# Program törzs (vagy Main függvény, ha jobban tetszik)
while True: # Végtelen ciklus
    clear_screen()
    print("Üdvözöllek Játékos!") # A játékos üdvözlése
    delay(1)
    
    print("Válaszd ki, hogy milyen lottón szeretnél játszani?") # Interaktív bekérés
    print("1-Hatos, 2-Ötös, 3-Skandináv, 4-Euro Jackpot, 5-Kilépés")
    tipus = input("")
    
    print("")
    delay(1)
    print("Számok kalkulálása...") # Program üzenet
    delay(1)

# Input vizsgálatok
    if tipus == "1":
        vonal()
        print("A generált hatos lottószámok:", generate_lotto(6, 45))
    
    elif tipus == "2":
        vonal()
        print("A generált ötös lottószámok:", generate_lotto(5, 90))
    
    elif tipus == "3":
        vonal()
        print("A generált skandináv lottószámok:", generate_lotto(7, 35))
    
    elif tipus == "4":
        vonal()
        print("A generált euro jackpot számok V1:", generate_lotto(5, 50)) # Az Euro Jackpot 2
        print("A generált euro jackpot számok V2:", generate_lotto(2, 12)) # kimenetet kap
    
    elif tipus == "5": # Kilépési feltétel
        vonal()
        print("Köszönöm, hogy játszottál!") # Elköszönés a felhasználótól
        print("Viszlát!")
        delay(1)
        clear_screen()
        break # Kilépés
    else: # Hibakezelés
        vonal()
        print("HIBA! Nincs ilyen típus!")
    
    input("\nNyomj ENTER-t a folytatáshoz...") # Folytathatóság
