import pyautogui
import time

time.sleep(3)

#pyautogui.click(530, 126)
#pyautogui.click(530, 150)

#pyautogui.typewrite('Hello world!', interval=0.25)

#pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
#pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.25)


pyautogui.click(530, 126)
pyautogui.typewrite('Hello world!', interval=0.25)

pyautogui.press('enter')  # Press Enter to move to the next line

pyautogui.click(530, 150)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=0.25)

#pyautogui.press('enter')

#pyautogui.click(530, 173)
#pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

