import random
import time

def generate_lotto(total, max_number):
    return random.sample(range(1, max_number + 1), total)

def vonal():
    print("----------------------------------------------------------")

while True:
    print("Üdvözöllek Játékos!")
    time.sleep(1)
    tipus = input("Válaszd ki, hogy milyen lottón szeretnél játszani? ")
    print("1-hatos, 2-ötös, 3-skandi, 4-euro, 5-exit")

    print("")
    time.sleep(1)
    print("Számok kalkulálása...")
    time.sleep(1)

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
        print("A generált euro jackpot számok V1:", generate_lotto(5, 50))
        print("A generált euro jackpot számok V2:", generate_lotto(2, 12))
    
    elif tipus == "5":
        vonal()
        print("Viszlát!")
        break
    else:
        vonal()
        print("HIBA! Nincs ilyen típus!")
