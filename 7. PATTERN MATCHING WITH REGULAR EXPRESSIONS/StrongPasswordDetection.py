import re

def is_strong_password(password):
    # Check if the password is at least eight characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if the password has at least one digit
    if not re.search(r'\d', password):
        return False

    # If all criteria are met, the password is strong
    return True

# Test the function with example passwords
passwords = [
    'StrongP@ssword1',
    'Weak123',
    'Lowercaseuppercase',
    '12345678',
    'OnlyUpperCase',
]

for password in passwords:
    print(f'{password}: {"Strong" if is_strong_password(password) else "Weak"}')
