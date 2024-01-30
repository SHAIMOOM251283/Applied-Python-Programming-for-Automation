empty_dict = {}

my_dict = {'foo': 42}
print(my_dict['foo'])  # Output: 42

my_list = [1, 2, 3, 4]
my_list[0] = 10 #Mutable, meaning you can modify, add, or remove elements after the list is created.
print(my_list)  # Output: 1 #Elements are accessed by their position (index) in the list.
print(my_list[0])  # Output: 10

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict['key1'] = 'new_value' #Also mutable. You can change the value associated with a key, add new key-value pairs, or remove existing ones.
print(my_dict['key1'])  # Output: 'value1' #Elements are accessed by their keys.

spam = {'bar': 100}
# Trying to access a key that doesn't exist
value = spam['foo']  # This will raise a KeyError

spam = {'bar': 100}
# Check if the key exists before accessing it
if 'foo' in spam:
    value = spam['foo']
    print(value)
else:
    print("Key 'foo' does not exist in the dictionary.")

spam = {'cat': 42, 'dog': 17, 'parrot': 5}
# Check if 'cat' is a key in the dictionary directly
if 'cat' in spam:
    print("'cat' is a key in spam")
# Check if 'cat' is a key in the list of keys
if 'cat' in spam.keys():
    print("'cat' is a key in spam.keys()")

spam = {'cat': 42, 'dog': 17, 'parrot': 5}
# Check if 'cat' is a key in the dictionary directly
if 'cat' in spam:
    print("'cat' is a key in spam")
# Check if 'cat' is a key in the list of keys
if 42 in spam.values():
    print("'42' is a value in spam.values()")
else: print('"42" is not a value in spam.values().')

spam = {'cat': 42, 'dog': 17, 'parrot': 5}
# Check if 'cat' is a key in the dictionary directly
if 'cat' in spam:
    print("'cat' is a key in spam")
# Check if 'cat' is a value in spam.values()
if 'cat' in spam.values():
    print("'cat' is a value in spam.values()")
else:
    print("'cat' is not a value in spam.values()")

number = 42 
float_number = 3.14 #When working with numbers (integers or floats), you don't need to use single or double quotes. Numbers can be written directly as literals.

word = 'cat'
phrase = "Hello, World!" #When working with strings (words or text), you should use single or double quotes to define the string.

my_dict = {'word': 'definition', 'color': 'blue', 'number': '42'} #If you're dealing with keys or values that are strings in a dictionary, you should use quotes

my_dict = {'count': 42, 'pi': 3.14, 'temperature': 25} #For numbers (integers or floats), you don't use quotes.

spam = {'color': 'white'}
if 'color' not in spam:
    spam['color'] = 'black'
spam.setdefault('color', 'black')

from pprint import pprint
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Pretty print the dictionary
pprint(my_dict)