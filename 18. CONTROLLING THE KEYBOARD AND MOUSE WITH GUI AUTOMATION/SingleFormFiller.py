import time
import pyautogui

def fill_form():
    # Allow more time for the browser to open
    time.sleep(5)

    # Click the Name field
    pyautogui.click(600, 531)
    time.sleep(1)

    # Type a name and press tab
    pyautogui.write("Your Name")
    pyautogui.press('tab')
    time.sleep(1)

    # Type greatest fear and press tab
    pyautogui.write("Your Greatest Fear")
    pyautogui.press('tab')
    time.sleep(1)

    # Select wizard power source
    wizard_power_source_count = 3  # Choose the correct number (1 for wand, 2 for amulet, 3 for crystal ball, 4 for money)
    for _ in range(wizard_power_source_count):
        pyautogui.press('down')
        time.sleep(1)
    pyautogui.press('enter')  # Press 'Enter' after selecting the wizard power source
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    # Select answer to RoboCop question
    robo_cop_answer_count = 2  # Choose the correct number (1 for spacebar, 2 for right arrow, etc.)
    for _ in range(robo_cop_answer_count):
        pyautogui.press('right')
        time.sleep(1)

    # Press tab twice to move to the next field
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    # Type additional comment and press tab
    pyautogui.write("Additional Comment")
    pyautogui.press('tab')
    time.sleep(1)

    # Press enter to submit
    pyautogui.press('enter')
    time.sleep(2)  # Adjust the delay according to your browser's response time

    # Click the link to return to the form page
    pyautogui.click(600, 300)
    time.sleep(2)  # Adjust the delay according to your browser's response time

if __name__ == "__main__":
    fill_form()
