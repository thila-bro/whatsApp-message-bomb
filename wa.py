import random
import pyjokes

import pyautogui as pg

import time

import pyperclip

animal = ('aziz', 'asel', 'kanishaka', 'walasa')

time.sleep(2)

for i in range(1, 100):
    a = random.choice(animal)
    # print(a + " wants a code challenge 😂😉")
    # joke = pyjokes.get_joke(language='en', category='all')
    # print(joke)

    pg.write(a + " wants a code challenge ")
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('ctrl')
    pg.press("enter")

