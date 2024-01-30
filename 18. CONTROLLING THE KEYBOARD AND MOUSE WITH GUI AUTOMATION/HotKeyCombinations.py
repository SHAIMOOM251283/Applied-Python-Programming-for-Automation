import pyautogui
import time

time.sleep(3)
pyautogui.press('enter')

def commentAfterDelay():
    pyautogui.click(530, 196)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.', interval=0.25)
    time.sleep(2)
    #pyautogui.hotkey('alt', '3')
    pyautogui.hotkey('ctrl', 's')
commentAfterDelay()