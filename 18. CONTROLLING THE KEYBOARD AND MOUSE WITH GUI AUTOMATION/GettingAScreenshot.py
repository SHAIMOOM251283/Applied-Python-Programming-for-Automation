import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))

import pyautogui
# Capture the screenshot
im = pyautogui.screenshot()
# Save the screenshot to a file
im.save("screenshot.png")
