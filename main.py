import pyautogui as pa
import time

time.sleep(5)
for i in range(1, 501):
    pa.write(str(i))
    pa.press("enter")
