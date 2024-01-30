#VALID INPUT
while True:
  print('Enter your age:')
  age = input()
  if age.isdecimal():
    break
  print('Please enter a number for your age.')
while True:
  print('Select a new password (letters and numbers only):')
  password = input()
  if password.isalnum():
    break
  print('Passwords can only have letters and numbers.')

#while True:
#    age_input = input('Enter your age: ')
#    if age_input.isdecimal():
#        age = int(age_input)
#        break
#    print('Please enter a valid number for your age.')
#while True:
#    password = input('Select a new password (should contain both letters and numbers): ')
#    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
#        break
#    print('Password should contain both letters and numbers.')
