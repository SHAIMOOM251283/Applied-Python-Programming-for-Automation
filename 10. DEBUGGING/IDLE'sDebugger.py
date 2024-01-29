#Start Debugging:
    #Function Key: F5
    #Keyboard Shortcut: Ctrl + F5

#Stop Debugging:
    #Function Key: Shift + F5
    #Keyboard Shortcut: Ctrl + Shift + F5

#Pause:
    #Function Key: No dedicated function key
    #Keyboard Shortcut: F6

#Continue:
    #Function Key: F5
    #Keyboard Shortcut: F5

#Step Over:
    #Function Key: F10
    #Keyboard Shortcut: F10

#Step Into:
    #Function Key: F11
    #Keyboard Shortcut: F11

#Step Out:
    #Function Key: Shift + F11
    #Keyboard Shortcut: Shift + F11

#Restart:
    #Function Key: Ctrl + Shift + F5
    #Keyboard Shortcut: Ctrl + Shift + F5

#Toggle Breakpoint:
    #Function Key: F9
    #Keyboard Shortcut: F9

#Step Back:
    #Function Key: No dedicated function key
    #Keyboard Shortcut: Not available for all debuggers

#print('Enter the first number to add:')
#first = input()
#print('Enter the second number to add:')
#second = input()
#print('Enter the third number to add:')
#third = input()
#print('The sum is ' + first + second + third)

#print('Enter the first number to add:')
#first = input()  # Breakpoint 1: Set a breakpoint here by clicking on the line number in the left margin.
#print('Enter the second number to add:')
#second = input()
#print('Enter the third number to add:')
#third = input()
# Breakpoint 2: Set another breakpoint before the line where you print the sum.
#print('The sum is ' + first + second + third)
#print('The sum is ' + str(int(first) + int(second) + int(third)))

import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
        if i == 500:
            print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')


