# The code uses the form https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

import time
import pyautogui

def fill_form(name, greatest_fear, wizard_power, robo_cop_answer, additional_comment):
    # Allow more time for the browser to open
    time.sleep(5)

    # Click the Name field
    pyautogui.click(600, 531)
    time.sleep(1)

    # Type a name and press tab
    pyautogui.write(name)
    pyautogui.press('tab')
    time.sleep(1)

    # Type greatest fear and press tab
    pyautogui.write(greatest_fear)
    pyautogui.press('tab')
    time.sleep(1)

    # Select wizard power source
    for _ in range(wizard_power):
        pyautogui.press('down')
        time.sleep(1)
    pyautogui.press('enter')  # Press 'Enter' after selecting the wizard power source
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    # Select answer to RoboCop question
    for _ in range(robo_cop_answer):
        pyautogui.press('right')
        time.sleep(1)

    # Press tab twice to move to the next field
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    # Type additional comment and press tab
    pyautogui.write(additional_comment)
    pyautogui.press('tab')
    time.sleep(1)

    # Press enter to submit
    pyautogui.press('enter')
    time.sleep(2)  # Adjust the delay according to your browser's response time

    # Click the link to return to the form page
    pyautogui.click(600, 300)
    time.sleep(2)  # Adjust the delay according to your browser's response time

if __name__ == "__main__":
    # Define the values for each form
    form_data = [
        {"name": "Alice", "greatest_fear": "eavesdropping", "wizard_power": 1, "robo_cop_answer": 1, "additional_comment": "The Good!"},
        {"name": "Bob", "greatest_fear": "bees", "wizard_power": 2, "robo_cop_answer": 2, "additional_comment": "The Bad!"},
        {"name": "Carol", "greatest_fear": "puppets", "wizard_power": 3, "robo_cop_answer": 3, "additional_comment": "The Ugly!"},
        {"name": "Alex Murphy", "greatest_fear": "ED-209", "wizard_power": 4, "robo_cop_answer": 4, "additional_comment": "And The Dollar!"}
    ]

    for data in form_data:
        fill_form(data["name"], data["greatest_fear"], data["wizard_power"], data["robo_cop_answer"], data["additional_comment"])
