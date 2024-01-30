import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((50, 200)))
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))
print(pyautogui.pixelMatchesColor(50, 200, (255, 135, 144)))
