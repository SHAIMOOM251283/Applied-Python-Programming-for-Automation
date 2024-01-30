name = input("Enter your name: ")
password = input("Enter your password: ")

if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

else:
    print('Unknown user.')

