#import pyautogui, time
#time.sleep(3)
#pyautogui.click(530, 126); pyautogui.typewrite('Hello world!'), 0.25

import pyautogui
import time

time.sleep(3)
pyautogui.click(530, 126)
pyautogui.typewrite('Hello world!', interval=0.25)
