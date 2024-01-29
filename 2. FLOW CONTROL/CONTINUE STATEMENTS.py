#while True:
#    print('Who are you?')
#    name = input()
#    if name != 'Joe':
#        continue
#    print('Hello, Joe. What is the password? (It is a fish.)')
#    password = input()
#    if password == 'swordfish':
#        break 
#print('Access granted.')

#while True:
#    print('Who are you?')
#    name = input()
#    if name != 'Joe':
#        continue
#    print('Hello, Joe. What is the password? (It is a fish.)')
#    password = input()
#    if password != 'swordfish':
#        continue
#    elif password == 'swordfish':
#        print('Access granted.')
#        break

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    
    while True:
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input()
        if password != 'swordfish':
            continue
        elif password == 'swordfish':
            print('Access granted.')
            break

    break
