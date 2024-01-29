import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

import requests
# Make a request to the URL
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# Check if the request was successful (status code 200)
if res.status_code == requests.codes.ok:
    # Get the text content
    text_content = res.text
    # Specify the file path where you want to save the text
    file_path = 'output.txt'
    # Open the file in write mode and write the text content
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text_content)
    print(f'Text saved to {file_path}')
else:
    # Print an error message if the request was not successful
    print(f'Error: Unable to fetch content. Status code: {res.status_code}')
