#Refer to MyPythonScripts

import re

pattern = re.compile(r'''
    \d{3}       # Match three digits
    -           # Match a hyphen
    \d{3}       # Match another three digits
''', re.VERBOSE)
result = pattern.match('123-456')
print(result.group())  # Output: 123-456

#pattern = re.compile(r'\d{3}-\d{3}')
#print(result := pattern.match('123-456'))

#text = "The price is $123.45."
# Using \d to match digits
#matches = re.findall(r'\d', text)
#print(matches)  # Output: ['1', '2', '3', '4', '5']
#print(matches := re.findall(r'\d', text))

#text = "The zip code is 12345."
# Using \d{3} to match three consecutive digits
#matches = re.findall(r'\d{3}', text)
#print(matches)  # Output: ['123']
#print(matches := re.findall(r'\d{3}', text))


