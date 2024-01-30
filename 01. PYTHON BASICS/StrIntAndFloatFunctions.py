#print('I am ' + 29 + ' years old.')

print(str(29))

print('I am ' + str(29) + ' years old.')

print(str(0))

print(str(-3.14))

print(int('42'))

print(int('-99'))

print(int(1.25))

print(int(1.99))

print(float('3.14'))

print(float(10))

#print('Input a value for spam:')
#spam = input()
#print(spam)

spam = input('Input a value for spam: ')
print(spam)
spam = int(spam) #use the int() function to get the integer form of spam and then store this as the new value in spam.
print(spam)
print(spam * 10 / 5) #treat the spam variable as an integer instead of a string

result = float(spam) * 10 / 5
print(result)

value = int(99.99)
print(value)

#value = int('99.99') #Error
#print(value)

#error = int('twelve') #Error
#print(error)

value = int(7.7) + 1
print(value)

#Strings are text, while integers and floats are both numbers.

#print(42 == '42')
print(42 == 42.0)
print(42.0 == 0042.000)

value1 = 42
value2 = '42'
result = value1 == value2
print(result)

