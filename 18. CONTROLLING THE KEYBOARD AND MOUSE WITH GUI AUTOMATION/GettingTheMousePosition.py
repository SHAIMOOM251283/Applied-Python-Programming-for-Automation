#import pyautogui
#print(pyautogui.position())

import pyautogui

for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    print(pyautogui.position())  # Print current mouse position
    pyautogui.moveRel(0, 100, duration=0.25)
    print(pyautogui.position())  # Print current mouse position
    pyautogui.moveRel(-100, 0, duration=0.25)
    print(pyautogui.position())  # Print current mouse position
    pyautogui.moveRel(0, -100, duration=0.25)
    print(pyautogui.position())  # Print current mouse position

