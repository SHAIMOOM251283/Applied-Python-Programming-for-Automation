#PyAutoGUI has a failsafe feature that allows you to stop the program by moving the mouse to the upper-left corner of the screen. 
#This is a safety mechanism to prevent unintended actions and provides a quick way to halt the script.
#You can trigger the failsafe in PyAutoGUI by simply moving the mouse to the coordinates (0, 0) on the screen. Here's an example:
import pyautogui
# Your code here
# Trigger failsafe to stop the program
pyautogui.moveTo(0, 0)

#In PyAutoGUI, the size() function is used to get the current screen resolution. 
#The size() function returns a named tuple containing the width and height of the primary monitor.
#Here's an example:
import pyautogui
# Get the screen resolution
resolution = pyautogui.size()
# Print the width and height
print("Width:", resolution.width)
print("Height:", resolution.height)

#In PyAutoGUI, the position() function is used to get the current coordinates of the mouse cursor. 
#This function returns a named tuple with x and y attributes representing the x and y coordinates of the mouse cursor.
#Here's an example:
import pyautogui
# Get the current mouse cursor position
mouse_position = pyautogui.position()
# Print the x and y coordinates
print("X:", mouse_position.x)
print("Y:", mouse_position.y)

#pyautogui.moveTo(x, y, duration=0.0, tween=pyautogui.linear)
#Moves the mouse cursor to the absolute screen coordinates specified by x and y.
#The optional duration parameter allows you to set the time, in seconds, that the mouse movement should take. 
#If not specified, the movement is instant.
#The optional tween parameter sets the easing function for the mouse movement. 
#The default is linear, but you can choose other easing functions.
#Example:
import pyautogui
# Move to absolute coordinates (100, 100) with a duration of 1 second
pyautogui.moveTo(100, 100, duration=1.0)

#pyautogui.moveRel(xOffset, yOffset, duration=0.0, tween=pyautogui.linear)
#Moves the mouse cursor relative to its current position by the specified xOffset and yOffset.
#The optional duration parameter sets the time, in seconds, for the relative mouse movement. 
#If not specified, the movement is instant.
#The optional tween parameter sets the easing function for the mouse movement.
#Example:
import pyautogui
# Move the mouse cursor 50 pixels to the right and 50 pixels down with a duration of 1 second
pyautogui.moveRel(50, 50, duration=1.0)

#In PyAutoGUI, you can use the pyautogui.dragTo() and pyautogui.dragRel() functions to simulate dragging the mouse.
#pyautogui.dragTo(x, y, duration=0.0, button='left', tween=pyautogui.linear)
#Drags the mouse cursor to the absolute screen coordinates specified by x and y.
#The optional duration parameter sets the time, in seconds, for the drag movement. If not specified, the movement is instant.
#The optional button parameter specifies which mouse button to drag (default is the left button).
#The optional tween parameter sets the easing function for the mouse movement.
#Example:
import pyautogui
# Drag the mouse cursor to absolute coordinates (200, 200) with the left button pressed
pyautogui.dragTo(200, 200, duration=1.0)

#pyautogui.dragRel(xOffset, yOffset, duration=0.0, button='left', tween=pyautogui.linear)
#Drags the mouse cursor relative to its current position by the specified xOffset and yOffset.
#The optional duration parameter sets the time, in seconds, for the relative drag movement. If not specified, the movement is instant.
#The optional button parameter specifies which mouse button to drag (default is the left button).
#The optional tween parameter sets the easing function for the mouse movement.
#Example:
import pyautogui
# Drag the mouse cursor 50 pixels to the right and 50 pixels down with the left button pressed
pyautogui.dragRel(50, 50, duration=1.0)

#To simulate typing out the characters "Hello, world!" using PyAutoGUI, you can use the pyautogui.typewrite() function. 
#Here's an example:
import pyautogui
import time
# Sleep for a few seconds to give you time to focus on the input field
time.sleep(5)
# Type out the characters "Hello, world!"
pyautogui.typewrite("Hello, world!")

#In PyAutoGUI, you can use the pyautogui.press() function to simulate keypresses for special keys, including arrow keys. 
#Here's an example that demonstrates how to press the left arrow key:
import pyautogui
# Press the left arrow key
pyautogui.press('left')
#In this example, pyautogui.press('left') simulates pressing the left arrow key on the keyboard. 
#You can use similar syntax for other special keys:
#'up': Up arrow key
#'down': Down arrow key
#'right': Right arrow key
#'enter': Enter key
#'space': Spacebar
#'esc': Escape key
#and more.
# If you need to press a combination of keys, you can use the pyautogui.hotkey() function. 
#For example, to press Ctrl+C, you would use:
pyautogui.hotkey('ctrl', 'c')

#To capture the current contents of the screen and save it as an image file (e.g., "screenshot.png") using PyAutoGUI, you can use the pyautogui.screenshot() function. 
#Here's an example:
import pyautogui
# Capture the screenshot
screenshot = pyautogui.screenshot()
# Save the screenshot to a file
screenshot.save('screenshot.png')

#You can introduce a pause after each PyAutoGUI function call using the time.sleep() function from the time module. 
#Here's an example:
import pyautogui
import time
# Your PyAutoGUI code here
# Set a two-second pause after each PyAutoGUI function call
pyautogui.moveTo(100, 100)
time.sleep(2)
pyautogui.click()
time.sleep(2)
pyautogui.typewrite("Hello, world!")
time.sleep(2)
# Continue with more PyAutoGUI code
