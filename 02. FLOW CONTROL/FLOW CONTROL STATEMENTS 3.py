name = input("Enter you name: ")

if name == 'Alice':
    print('Hi, Alice')
else:
    age = int(input("Enter your age: "))

    if age < 12:
        print('You are not Alice, kiddo')
    
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
    
    elif age > 100:
        print('You are not Alice, grannie.')

