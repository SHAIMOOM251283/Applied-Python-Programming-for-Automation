name = input("Enter your name: ")

if name == 'Alice':
    print('Hi, Alice.')
else:
    age = int(input("Enter your age "))

    if age < 12:
        print('You are not Alice, kiddo')
    
    else: 
        print('You are neither Alice nor a little kid.')