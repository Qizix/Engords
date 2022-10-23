from random import randint
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def testt(base, trysss, zapp):
    cls()
    res = 100
    tryss = trysss
    zap = zapp
    peres = int(res / zap)
    pair = base
    for i in range(20):
        trys = tryss
        t = randint(0, len(pair)-1)
        print(pair[t][1])
        while True:
            ans = input()
            if ans == pair[t][0]:
                print("You are right")
                break
            else:
                trys -= 1
                print("It is wrong")
                print("You have", trys, "attempts left \n")

                if trys == 0:
                    res -= peres
                    break
        print(pair[t][1], "-", pair[t][0])
        input()
        cls()
    print("Your result is -", res, "%")
    input("Press enter to end.")
    return res





