from random import randint
from gtts import gTTS
from playsound import playsound
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def teach(base):
    pair = base
    cls()
    while input() != "stop":
        t = randint(0, len(pair)-1)
        print(pair[t][1], end="")
        input()
        print(pair[t][0])
        gTTS(pair[t][0]).save('sample.mp3')
        playsound('sample.mp3')
        input()
        cls()
    os.remove("sample.mp3")




