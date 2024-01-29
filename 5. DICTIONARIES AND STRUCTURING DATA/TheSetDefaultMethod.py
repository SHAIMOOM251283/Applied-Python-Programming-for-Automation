spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white') 
print(spam)

#The method returns the value 'black' because this is now the value set for the key 'color'. 
#When spam.setdefault('color', 'white') is called, the value for that key is not changed to 'white' because spam already has a key named 'color
