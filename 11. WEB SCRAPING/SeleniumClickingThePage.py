#from selenium import webdriver
#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')
#linkElem = browser.find_element_by_link_text('Read It Online')
#print(type(linkElem))
#linkElem.click() # follows the "Read It Online" link

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create a Firefox driver
driver = webdriver.Firefox()
# Open a web page
url = 'http://inventwithpython.com'
driver.get(url)
# Find the link element by its text (you can use other locators too)
link_text = 'Read for Free'
# Wait for the link to be clickable
link_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, link_text))
)
# Click on the link
link_element.click()



