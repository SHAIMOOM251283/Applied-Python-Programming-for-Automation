from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By for element finding
from selenium.webdriver.common.keys import Keys
import time

# Create a Firefox webdriver instance
driver = webdriver.Firefox()

# Open the 2048 game webpage
game_url = "https://gabrielecirulli.github.io/2048/"
driver.get(game_url)

# Focus on the game board (corrected line)
game_board = driver.find_element(By.TAG_NAME, "body")  # Use By.TAG_NAME
game_board.click()

# Start the game loop
while True:
    try:
        # Send keystrokes in a repeating pattern
        game_board.send_keys(Keys.UP)
        time.sleep(0.1)  # Adjust delay as needed
        game_board.send_keys(Keys.RIGHT)
        time.sleep(0.1)
        game_board.send_keys(Keys.DOWN)
        time.sleep(0.1)
        game_board.send_keys(Keys.LEFT)
        time.sleep(0.1)
    except Exception as e:
        print("Game ended or error occurred:", e)
        break

# Close the browser window
#driver.quit()
