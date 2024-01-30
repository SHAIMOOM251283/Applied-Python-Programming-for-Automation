#import pyautogui
#pyautogui.locateOnScreen('submit.png')

import pyautogui
import cv2
import numpy as np
import time

# Replace with the absolute path to a simple, distinct image on your screen
image_path = r'E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\18. CONTROLLING THE KEYBOARD AND MOUSE WITH GUI AUTOMATION\\image.png'

try:
    # Capture the current screen content
    screenshot = pyautogui.screenshot()

    # Save the screenshot for reference (optional)
    screenshot.save('screenshot.png')

    # Convert the screenshot to grayscale for better matching
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Load the image you want to find
    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Try to locate the image in the screenshot
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.8:  # You may need to adjust this threshold based on your images
        print(f"Image found at coordinates: {max_loc}")

        # Get the width and height of the template image
        w, h = template.shape[::-1]

        # Draw a rectangle around the located area
        cv2.rectangle(screenshot_gray, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 0, 255), 2)

        # Display the result (optional)
        cv2.imshow('Result', screenshot_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        time.sleep(2)

        # Perform additional operations
        # Example 1: Click at the center of the located area
        pyautogui.click(max_loc[0] + w // 2, max_loc[1] + h // 2)

        # Example 2: Perform multiple clicks at the located area using locateAllOnScreen
        #for loc in pyautogui.locateAllOnScreen('image.png'):
        #    pyautogui.click(pyautogui.center(loc))
        
        for loc in pyautogui.locateAllOnScreen('image.png', confidence=0.7):
            pyautogui.click(pyautogui.center(loc))

    else:
        print("Image not found on the screen")
except pyautogui.ImageNotFoundException:
    print("Image not found. Check the path.")

   

