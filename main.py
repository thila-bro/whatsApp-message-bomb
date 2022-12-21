import pyautogui as pa
import time

time.sleep(5)


def pressing_tab_key():
    pa.keyDown("tab")
    pa.keyUp("tab")


def selecting_san_kote():
    pa.keyDown("shift")
    pa.keyDown("2")
    pa.keyUp("2")
    pa.keyUp("shift")
    pa.write("holmana")


def lover_emoji():
    pa.write(":lover")
    pressing_tab_key()


def red_heart_emoji():
    pa.write(":red heart")
    pressing_tab_key()


for i in range(1, 101):
    selecting_san_kote()
    pressing_tab_key()
    pa.write("lv u sudu menika ")
    lover_emoji()
    lover_emoji()
    red_heart_emoji()
    pa.press("enter")
