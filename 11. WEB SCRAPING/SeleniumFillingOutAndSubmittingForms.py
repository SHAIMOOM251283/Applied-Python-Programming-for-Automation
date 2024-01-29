#from selenium import webdriver
#browser = webdriver.Firefox()
#browser.get('http://gmail.com')
#emailElem = browser.find_element_by_id('Email')
#emailElem.send_keys('not_my_real_email@gmail.com')
#passwordElem = browser.find_element_by_id('Passwd')
#passwordElem.send_keys('12345')
#passwordElem.submit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def automate_gmail_sign_in(username, password):
    driver = webdriver.Firefox()
    # Open Gmail login page
    driver.get('https://accounts.google.com')
    # Find the email input field and enter the username
    email_input = driver.find_element('id', 'identifierId')
    email_input.send_keys(username)
    email_input.send_keys(Keys.RETURN)
    # Wait for the password input field to be visible
    time.sleep(2)
    # Find the password input field and enter the password
    password_input = driver.find_element('name', 'password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    # Wait for a few seconds to allow the login process to complete
    time.sleep(5)
    # Close the browser window
    driver.quit()
# Replace 'your_username' and 'your_password' with your actual Gmail username and password
automate_gmail_sign_in('username', 'password')


    