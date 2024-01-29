#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#browser = webdriver.Firefox()
#browser.get('http://nostarch.com')
#htmlElem = browser.find_element_by_tag_name('html')
#htmlElem.send_keys(Keys.END) # scrolls to bottom
#htmlElem.send_keys(Keys.HOME) # scrolls to top

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
url = 'http://nostarch.com'
driver.get(url)
htmlElem = driver.find_element(By.TAG_NAME, 'html')
htmlElem.send_keys(Keys.END)  # scrolls to bottom
htmlElem.send_keys(Keys.HOME)  # scrolls to top




