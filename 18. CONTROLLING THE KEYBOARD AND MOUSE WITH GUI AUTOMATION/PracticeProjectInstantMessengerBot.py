# The code can send messages in google talk. 

import pyautogui
import time

# Function to simulate key presses with a delay
def type_with_delay(text, delay=0.1):
    pyautogui.typewrite(text, interval=delay)

# Function to perform the specified tasks
def perform_tasks():
    # Click on the search field
    pyautogui.click(470, 146)

    # Type "name_of_recipient" in the search field
    type_with_delay("name_of_recipient")

    # Press the down arrow twice
    pyautogui.press('down')
    pyautogui.press('down')

    # Press Enter to select the time
    pyautogui.press('enter')

    # Move the cursor to coordinates 690, 915
    pyautogui.moveTo(690, 915)

    # Type the specified text
    type_with_delay("Cheers to the love that grows stronger with each passing day.")

    # Press Enter
    pyautogui.press('enter')

# Add a delay before running the script to give time to switch to the desired application
time.sleep(5)

# Call the function to perform the tasks
perform_tasks()
