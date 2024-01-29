#The webbrowser, requests, BeautifulSoup, and Selenium modules are Python libraries that serve different purposes when working with web-related tasks.
# webbrowser is for opening URLs in a web browser.
# requests is for making HTTP requests and handling responses.
# BeautifulSoup is for parsing and navigating HTML or XML documents, mainly used in web scraping.
# Selenium is for automating web browsers, commonly used in testing and dynamic web scraping scenarios.

#The requests.get() function returns a Response object. 
#To access the downloaded content as a string value, you can use the text attribute of the Response object.
import requests
# Make a GET request to a URL
response = requests.get('https://www.example.com')
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Access the downloaded content as a string
    content_string = response.text
    print(content_string)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

# In the Requests library the most common HTTP status code indicating a successful response is 200 OK.
import requests
# Make a GET request to a URL
response = requests.get('https://www.example.com')
# Check if the request was successful (status code 200)
if response.status_code == 200:
    print('Download successful')
    # Access the downloaded content as a string
    content_string = response.text
    print(content_string)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

#To get the HTTP status code of a requests response, you can use the status_code attribute of the Response object.
import requests
# Make a GET request to a URL
response = requests.get('https://www.example.com')
# Get the HTTP status code
status_code = response.status_code
# Print the HTTP status code
print(f"HTTP Status Code: {status_code}")
# Check if the request was successful (status code 200)
if status_code == 200:
    print('Download successful')
    # Access the downloaded content as a string
    content_string = response.text
    print(content_string)
else:
    # Print an error message if the request was not successful
    print(f"Error: {status_code}")

#To save a requests response to a file, you can use the content attribute of the Response object and write it to a file.
import requests
# Make a GET request to a URL
response = requests.get('https://www.example.com')
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the content from the response
    content = response.content
    # Specify the filename to save the content to
    filename = 'output_file.txt'
    # Open the file in binary write mode and write the content
    with open(filename, 'wb') as file:
        file.write(content)
    print(f"Downloaded content saved to {filename}")
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

#Keyboard shortcut for opening a browser's devloper tools:
#Google Chrome:
#    Windows/Linux: Press Ctrl + Shift + I or F12.
#    macOS: Press Cmd + Opt + I.
#Mozilla Firefox:
#    Windows/Linux: Press Ctrl + Shift + I or F12.
#    macOS: Press Cmd + Opt + I.
#Microsoft Edge:
#    Windows/Linux: Press Ctrl + Shift + I or F12.
#    macOS: Press Cmd + Opt + I.

#To view the HTML of a specific element on a web page using the browser's developer tools, follow these general steps:
#Open Developer Tools:
#    Use the appropriate keyboard shortcut to open the developer tools in your browser. (For example, Ctrl + Shift + I or F12 in Chrome and Firefox).
#Select the Element:
#    Navigate to the "Elements" or "Inspector" tab within the developer tools.
#    Use the mouse to right-click on the element you want to inspect on the webpage.
#    In the context menu that appears, select "Inspect" or "Inspect Element." This will highlight the corresponding HTML code in the "Elements" tab.
#View HTML:
#    Once the element is selected and highlighted in the "Elements" tab, you can view its corresponding HTML code.
#    The HTML code for the selected element will be displayed within the "Elements" or "Inspector" tab, allowing you to see the structure, attributes, and content of that specific element.
#Navigate in the DOM Tree:
#    In the "Elements" or "Inspector" tab, you can navigate through the Document Object Model (DOM) tree to explore the HTML structure of the entire page.

#The CSS selector string to find an element with an id attribute of "main" is:
    #main
#In CSS, the # symbol is used to denote an id selector, and "main" is the value of the id attribute. 
#This selector specifically targets the HTML element that has the id attribute set to "main". 
#When using this selector in a stylesheet or when querying the DOM with JavaScript or in browser developer tools, it will match the element with the specified id.

#The CSS selector string to find elements with a CSS class of "highlight" is:
#    .highlight
#In CSS, the . (dot) is used to denote a class selector, and "highlight" is the name of the class. 
#This selector will match all HTML elements that have the "highlight" class applied to them. 
#When using this selector in a stylesheet or when querying the DOM with JavaScript or in browser developer tools, it will select elements with the specified class.

#To select all <div> elements that are nested inside another <div> element, you can use the descendant combinator ( ). 
#The CSS selector string would be:
#    div div
#This selector targets all <div> elements that are descendants of another <div> element, regardless of how deeply they are nested. 
#It will not select <div> elements that are not nested within another <div>.

#To select a <button> element with a value attribute set to "favorite," you can use the attribute selector. The CSS selector string would be:
#    button[value="favorite"]
#This selector targets <button> elements specifically with a value attribute set to "favorite." 
#It's using the attribute selector syntax [attribute="value"] to narrow down the selection to buttons with the specified attribute value.

#If you have a Beautiful Soup Tag object stored in the variable spam for the HTML element <div>Hello world!</div>, you can get the string content 'Hello world!' using the .text attribute or the .get_text() method. 
#Here's how you can do it:
#Using .text attribute:
# Assuming 'spam' is the Beautiful Soup Tag object
spam = object
content_string = spam.text
print(content_string)
#Using .get_text() method:
# Assuming 'spam' is the Beautiful Soup Tag object
content_string = spam.get_text()
print(content_string)
#Both of these methods will extract the textual content within the <div> element and store it in the content_string variable. 
#The result will be 'Hello world!'. Choose the method that fits your preference or specific use case.

#To store all the attributes of a Beautiful Soup Tag object in a variable named linkElem, you can use the .attrs attribute of the Tag object. 
#Here's an example:
# Assuming 'tag' is the Beautiful Soup Tag object
tag = object
linkElem = tag.attrs
# Now 'linkElem' is a dictionary containing all the attributes of the tag
print(linkElem)
#In this example, linkElem will be a dictionary where the keys are attribute names, and the values are the corresponding attribute values. 
#This dictionary will contain all the attributes associated with the Beautiful Soup Tag object.

#To properly import the Selenium module, you need to ensure that it is installed first. You can install it using a package manager like pip. 

#In Selenium, the find_element_* and find_elements_* methods are used to locate elements on a web page. 
#The key difference between them lies in the number of elements they return:
#find_element_*:
#    Returns the first matching element.
#    If no matching element is found, it raises a NoSuchElementException.
#    Examples include find_element_by_id, find_element_by_name, find_element_by_xpath, etc.
#Example:
from selenium import webdriver
driver = webdriver.Chrome()
element = driver.find_element_by_id("example_id")
#find_elements_*:
#    Returns a list of all matching elements.
#    If no matching element is found, it returns an empty list.
#    Examples include find_elements_by_name, find_elements_by_xpath, find_elements_by_class_name, etc.
from selenium import webdriver
driver = webdriver.Chrome()
elements = driver.find_elements_by_class_name("example_class")

#Selenium's WebElement objects have several methods for simulating mouse clicks and keyboard interactions. 
#Here are some commonly used methods:
#Simulates a mouse click on the element.
element = driver.find_element_by_id("example_id")
element.click()
#Simulates a right-click on the element.
element = driver.find_element_by_id("example_id")
webdriver.ActionChains(driver).context_click(element).perform()
#Simulates a double-click on the element.
element = driver.find_element_by_id("example_id")
webdriver.ActionChains(driver).double_click(element).perform()
#Sends a sequence of keys to the element.
element = driver.find_element_by_name("example_name")
element.send_keys("Hello, World!")
#Clears the text content of the element.
element = driver.find_element_by_css_selector("input[type='text']")
element.clear()
#Submits a form associated with the element.
form_element = driver.find_element_by_css_selector("form")
form_element.submit()

#An easier way to submit a form with Selenium is to locate the form element and use the submit() method directly on the form's WebElement object. 
#This method simulates the clicking of the submit button without explicitly interacting with the button itself. Here's an example:
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
# Find the form element
form_element = driver.find_element_by_css_selector("form")
# Submit the form
form_element.submit()

#Selenium provides the forward(), back(), and refresh() methods to simulate clicking the browser's Forward, Back, and Refresh buttons, respectively. 
#Here's how you can use these methods:
#Simulating Clicking the Back Button.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
# Perform some actions on the page
# Simulate clicking the Back button
driver.back()
#Simulating Clicking the Forward Button.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
# Perform some actions and go back
# Simulate clicking the Forward button
driver.forward()
#Simulating Clicking the Refresh Button.
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
# Perform some actions on the page
# Simulate clicking the Refresh button
driver.refresh()




