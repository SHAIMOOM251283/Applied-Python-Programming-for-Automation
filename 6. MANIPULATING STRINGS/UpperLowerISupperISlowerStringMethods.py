spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

print('How are you?')
feeling = input()
if feeling.lower() == 'great': #string is converted to lower case
   print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())
print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())