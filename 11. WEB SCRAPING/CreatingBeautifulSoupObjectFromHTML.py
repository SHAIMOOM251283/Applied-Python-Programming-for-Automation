#import requests, bs4
#res = requests.get('http://nostarch.com')
#res.raise_for_status()
#noStarchSoup = bs4.BeautifulSoup(res.text)
#type(noStarchSoup)

import requests
import bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')  # Explicitly specify the parser
print(type(noStarchSoup))

import requests, bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))

# Both of the codes cases are creating BeautifulSoup objects from HTML content, and the type of these objects is what gets printed. 
