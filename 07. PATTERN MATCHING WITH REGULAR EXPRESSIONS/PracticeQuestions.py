import re

# Create a regular expression pattern to match digits
pattern = re.compile(r'\d')
# Use the pattern to search for matches in a string
result = pattern.search('The price is $123.45.')
# Print the matched substring
print(result.group())  # Output: 1

# Create a case-insensitive regular expression pattern to match 'apple'
pattern = re.compile(r'apple', re.IGNORECASE)
# Use the pattern to search for matches in a string
result = pattern.search('I like Apples.')
# Print the matched substring
print(result.group())  # Output: Apples

# Create a regular expression pattern to match digits
pattern = re.compile(r'\d')
# Use the pattern to find all matches in a string
matches = pattern.findall('The price is $123.45.')
# Print all matched substrings
print(matches)  # Output: ['1', '2', '3', '4', '5']

#In Python, the re.compile() function is used to create regular expression objects.
#This function is part of the re module, which provides support for regular expressions.

# Without using a raw string
pattern_without_raw = re.compile('\d\d-\d\d-\d\d\d\d')
# Using a raw string
pattern_with_raw = re.compile(r'\d\d-\d\d-\d\d\d\d')

# Create a regular expression pattern
pattern = re.compile(r'\d+')
# Use search() to find the first occurrence of one or more digits in a string
result = pattern.search('The price is $123.45.')
# Check if a match was found
if result:
    print('Match found:', result.group())  # Output: Match found: 123
else:
    print('No match found')

# Create a regular expression pattern to match digits and an optional decimal part
pattern = re.compile(r'\d+(\.\d+)?')
# Use search() to find the first occurrence of digits with an optional decimal part
result = pattern.search('The price is $123.45.')
# Check if a match was found
if result:
    print('Match found:', result.group())  # Output: Match found: 123.45
else:
    print('No match found')

# Create a regular expression pattern with capturing groups
pattern = re.compile(r'(\d+)-(\d+)-(\d+)')
# Use search() to find the first occurrence of the pattern in a string
result = pattern.search('Date: 2022-12-19')
# Check if a match was found
if result:
    # Get the entire matched substring
    print('Full match:', result.group(0))  # Output: Full match: 2022-12-19
    # Get the content matched by the first capturing group
    print('Group 1:', result.group(1))  # Output: Group 1: 2022
    # Get the content matched by the second capturing group
    print('Group 2:', result.group(2))  # Output: Group 2: 12
    # Get the content matched by the third capturing group
    print('Group 3:', result.group(3))  # Output: Group 3: 19
else:
    print('No match found')

# Create a regular expression pattern with capturing groups
pattern = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# Use search() to find the first occurrence of the pattern in a string
result = pattern.search('Phone number: 555-123-4567')
# Check if a match was found
if result:
    # Get the entire matched substring
    print('Full match:', result.group(0))  # Output: Full match: 555-123-4567
    # Get the content matched by the first capturing group
    print('Group 1:', result.group(1))  # Output: Group 1: 555
    # Get the content matched by the second capturing group
    print('Group 2:', result.group(2))  # Output: Group 2: 123-4567
else:
    print('No match found')

# Create a regular expression pattern to match literal parentheses and period
pattern = re.compile(r'\(\d+\) and \.\d+')
# Use search() to find the pattern in a string
result = pattern.search('(123) and .456')
# Check if a match was found
if result:
    print('Match found:', result.group())  # Output: Match found: (123) and .456
else:
    print('No match found')

pattern = re.compile(r'\d+')
text = 'The price is $123.45 and $678.90.'
matches = pattern.findall(text)
print(matches)
# Output: ['123', '45', '678', '90']

pattern = re.compile(r'(\d+)-(\d+)')
text = 'Phone numbers: 555-1234 and 678-5678.'
matches = pattern.findall(text)
print(matches)
# Output: [('555', '1234'), ('678', '5678')]

pattern = re.compile(r'cat|dog')
text = 'I have a cat and a dog.'
matches = pattern.findall(text)
print(matches)
# Output: ['cat', 'dog']

# Using | without parentheses
pattern = re.compile(r'dog|cat and mouse')
text = 'I have a cat and mouse, and also a dog and mouse.'
matches = pattern.findall(text)
print(matches)
# Output: ['cat and mouse', 'dog']

# Using | with parentheses
pattern = re.compile(r'(cat|dog) and mouse')
text = 'I have a cat and mouse, and also a dog and mouse.'
matches = pattern.findall(text)
print(matches)
# Output: ['cat', 'dog']

pattern = re.compile(r'colou?r')
text1 = 'color'
text2 = 'colour'
match1 = pattern.search(text1)
match2 = pattern.search(text2)
print(match1.group())  # Output: color
print(match2.group())  # Output: colour

pattern = re.compile(r'<.*?>')
text = '<p>Hello</p><p>World</p>'
match = pattern.search(text)
print(match.group())  # Output: <p>Hello</p>

pattern = re.compile(r'a+')
text1 = 'aaa'
text2 = 'bbb'
match1 = pattern.search(text1)
match2 = pattern.search(text2)
print(match1.group())  # Output: aaa
print(match2)  # Output: None (no match)

pattern = re.compile(r'b*')
text1 = 'bbb'
text2 = 'aaa'
match1 = pattern.search(text1)
match2 = pattern.search(text2)
print(match1.group())  # Output: bbb
print(match2.group())  # Output: '' (empty string, matches zero 'b' characters)

pattern = re.compile(r'a{3}')
text1 = 'aaa'
text2 = 'aaaa'
match1 = pattern.search(text1)
match2 = pattern.search(text2)
print(match1.group())  # Output: aaa
print(match2)  # Output: None (no match)

pattern = re.compile(r'b{2,4}')
text1 = 'bb'
text2 = 'bbb'
text3 = 'bbbb'
text4 = 'bbbbb'
match1 = pattern.search(text1)
match2 = pattern.search(text2)
match3 = pattern.search(text3)
match4 = pattern.search(text4)
print(match1)  # Output: None (no match)
print(match2.group())  # Output: bbb
print(match3.group())  # Output: bbbb
print(match4.group())  # Output: bbbb (matches first four 'b' characters)

pattern = re.compile(r'\d{3}')
text = '12345'
match = pattern.search(text)
print(match.group())  # Output: 123

pattern = re.compile(r'\w+')
text = 'hello_world_123'
match = pattern.search(text)
print(match.group())  # Output: hello_world_123

pattern = re.compile(r'\s+')
text = '   This is a sentence with spaces   '
match = pattern.search(text)
print(repr(match.group()))  # Output: '   '

pattern = re.compile(r'\D+')
text = '123abc456'
match = pattern.search(text)
print(match.group())  # Output: abc

pattern = re.compile(r'\W+')
text = 'hello_world_123!'
match = pattern.search(text)
print(match.group())  # Output: !

pattern = re.compile(r'\S+')
text = '   This is a sentence with spaces   '
match = pattern.search(text)
print(match.group())  # Output: 'This'

pattern = re.compile(r'\S+')
text = '   This is a sentence with spaces   '
matches = pattern.findall(text)
print(matches)  # Output: ['This', 'is', 'a', 'sentence', 'with', 'spaces']

# Case-sensitive pattern
pattern_case_sensitive = re.compile(r'apple')
# Case-insensitive pattern using re.IGNORECASE flag
pattern_case_insensitive = re.compile(r'apple', re.IGNORECASE)
text = 'I have an Apple and an orange.'
# Case-sensitive search
match_case_sensitive = pattern_case_sensitive.search(text)
print(match_case_sensitive)  # Output: None (no match)
# Case-insensitive search
match_case_insensitive = pattern_case_insensitive.search(text)
print(match_case_insensitive.group())  # Output: Apple

# Without re.DOTALL
pattern_without_dotall = re.compile(r'.')
# With re.DOTALL
pattern_with_dotall = re.compile(r'.', re.DOTALL)
text = 'Line 1\nLine 2'
# Without re.DOTALL
match_without_dotall = pattern_without_dotall.search(text)
print(repr(match_without_dotall.group()))  # Output: 'L' (matches the first character)
# With re.DOTALL
match_with_dotall = pattern_with_dotall.search(text)
print(repr(match_with_dotall.group()))  # Output: 'L' (matches the first character, including newline)

pattern = re.compile(r'a.*b')
text = 'axxxbxxxbyyyb'
match = pattern.search(text)
print(match.group())  # Output: 'axxxbxxxbyyyb'

pattern = re.compile(r'a.*?b')
text = 'axxxbxxxbyyyb'
match = pattern.search(text)
print(match.group())  # Output: 'axxxb'

pattern = re.compile(r'[0-9a-z]')
text = 'Abc123XYZ'
matches = pattern.findall(text)
print(matches)  # Output: ['b', 'c', '1', '2', '3']

pattern = re.compile(r'[0-9a-z]+')
text = 'Abc123XYZ'
match = pattern.search(text)
print(match.group())  # Output: 'bc123'

numRegex = re.compile(r'\d+')
text = '12 drummers, 11 pipers, five rings, 3 hens'
result = numRegex.sub('X', text)
print(result) # Output: X drummers, X pipers, five rings, X hens

# Regular expression without re.VERBOSE
pattern_without_verbose = re.compile(r'\d{3}-\d{2}-\d{4}')
# Regular expression with re.VERBOSE
pattern_with_verbose = re.compile(r'''
    \d{3}  # Match three digits
    -      # Match a hyphen
    \d{2}  # Match two digits
    -      # Match a hyphen
    \d{4}  # Match four digits
''', re.VERBOSE)
text = '123-45-6789'
match_without_verbose = pattern_without_verbose.search(text)
match_with_verbose = pattern_with_verbose.search(text)
print(match_without_verbose.group())  # Output: '123-45-6789'
print(match_with_verbose.group())     # Output: '123-45-6789'

pattern = re.compile(r'^\d{1,3}(,\d{3})*$')
# Test cases
valid_numbers = ['42', '1,234', '6,368,745']
invalid_numbers = ['12,34,567', '1234']
for number in valid_numbers:
    match = pattern.match(number)
    print(f'{number}: {"Valid" if match else "Invalid"}')
for number in invalid_numbers:
    match = pattern.match(number)
    print(f'{number}: {"Valid" if match else "Invalid"}')
#Output
#42: Valid (Matches because it has 1 to 3 digits and no commas.)
#1,234: Valid (Matches because it starts with 1 to 3 digits, followed by a comma and three digits, and the pattern can repeat.)
#6,368,745: Valid (Matches for the same reason as 1,234.)
#12,34,567: Invalid (Does not match because it has only two digits between the commas.)
#1234: Invalid (Does not match becase it lacks commas.)

pattern = re.compile(r'^[A-Z][a-zA-Z]* Nakamoto$')
# Test cases
valid_names = ['Satoshi Nakamoto', 'Alice Nakamoto', 'RoboCop Nakamoto']
invalid_names = ['satoshi Nakamoto', 'Mr. Nakamoto', 'Nakamoto', 'Satoshi nakamoto']
for name in valid_names:
    match = pattern.match(name)
    print(f'{name}: {"Valid" if match else "Invalid"}')
for name in invalid_names:
    match = pattern.match(name)
    print(f'{name}: {"Valid" if match else "Invalid"}')
#Output
#Satoshi Nakamoto: Valid
#Alice Nakamoto: Valid
#RoboCop Nakamoto: Valid
#satoshi Nakamoto: Invalid
#Mr. Nakamoto: Invalid
#Nakamoto: Invalid
#Satoshi nakamoto: Invalid

pattern = re.compile(r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$', re.IGNORECASE)
# Test cases
valid_sentences = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.'
]
invalid_sentences = [
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.'
]
for sentence in valid_sentences:
    match = pattern.match(sentence)
    print(f'{sentence}: {"Valid" if match else "Invalid"}')
for sentence in invalid_sentences:
    match = pattern.match(sentence)
    print(f'{sentence}: {"Valid" if match else "Invalid"}')
#Output
#Alice eats apples.: Valid
#Bob pets cats.: Valid
#Carol throws baseballs.: Valid
#Alice throws Apples.: Valid
#BOB EATS CATS.: Valid
#RoboCop eats apples.: Invalid
#ALICE THROWS FOOTBALLS.: Invalid
#Carol eats 7 cats.: Invalid






