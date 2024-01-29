spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken') # ValueError: list.remove(x): x not in list
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # only the first instance of the value will be removed
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
while 'cat' in spam:
    spam.remove('cat') # remove all cat from list
print(spam)