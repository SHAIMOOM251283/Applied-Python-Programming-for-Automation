import pyautogui
import time

def nudge_mouse():
    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Define the nudge distance (adjust as needed)
    nudge_distance = 5

    # Calculate the new position by nudging the mouse
    new_x = current_x + nudge_distance
    new_y = current_y + nudge_distance

    # Move the mouse cursor to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.1)

if __name__ == "__main__":
    try:
        while True:
            # Nudge the mouse cursor every 10 seconds
            nudge_mouse()

            # Wait for 10 seconds
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
