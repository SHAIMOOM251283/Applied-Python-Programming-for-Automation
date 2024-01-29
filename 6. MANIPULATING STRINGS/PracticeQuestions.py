#Escape characters are special characters that are used in strings to represent non-printable or difficult-to-type characters. 
#They are preceded by a backslash \ and are used to escape the normal interpretation of characters in a string. 
#When an escape character is encountered in a string, it signals that the character following it should be treated differently.
#Here are some common escape characters in Python:
#    \\: Backslash
#    \': Single quote
#    \": Double quote
#    \n: Newline
#    \t: Tab
#    \r: Carriage return
#    \b: Backspace
#    \f: Form feed
#For example:
print("This is a string with a newline character:\nSecond line.")
print("This is a string with a tab character:\tSeparated by a tab.")
print("This is a string with a backslash: \\")
#The output will be:
#This is a string with a newline character:
#Second line.
#This is a string with a tab character:    Separated by a tab.
#This is a string with a backslash: \

#In Python strings, the escape characters \n and \t represent special whitespace characters:
#\n: Newline
#When used in a string, \n creates a newline character, causing the text following it to start on a new line. 
#It's commonly used to break lines or create multiline strings.
#Example:
print("Hello\nWorld")
#Output:
#Hello
#World
#\t: Tab
#\t represents a tab character. 
#When used in a string, it adds horizontal space, simulating a tab indentation. It's often used for formatting text or aligning columns.
#Example:
print("Name\tAge")
print("John\t25")
print("Alice\t30")
#Output:
#Name    Age
#John    25
#Alice   30

#To include a backslash \ character in a string, you need to use a double backslash \\. 
#This is because a single backslash is an escape character in Python, and using it alone would be interpreted as the start of an escape sequence.
#Here's an example:
print("This is a single backslash: \\")
#Output:
#This is a single backslash: \
#In this example, the double backslash \\ is used to escape the special meaning of the backslash, allowing it to be treated as a regular character in the string.

#In Python, you can use either single quotes (') or double quotes (") to define string literals. 
#So, when you have a string with a single quote character inside it, you can use double quotes to define the string, or vice versa, without needing to escape the internal single quote.
#For example:
book_title = "Howl's Moving Castle"
#Or:
book_title = 'Howl\'s Moving Castle'
#The use of double quotes allows you to include a single quote character within the string without escaping it, and vice versa. 

#If you want to include newlines in a string without using the \n escape sequence directly, you can create a multiline string by enclosing the text within triple quotes (''' or """). 
#This allows you to span the string across multiple lines, and any newline characters within the triple-quoted string will be preserved in the final string.
#Here's an example:
multiline_string = '''This is a multiline string.
It spans across multiple lines.
Newlines are preserved.'''
#Or using double quotes:
multiline_string = """This is a multiline string.
It spans across multiple lines.
Newlines are preserved."""
#In both cases, the resulting multiline_string will include the newlines, and you can print it to see the formatted output:
print(multiline_string)
#Output:
#This is a multiline string.
#It spans across multiple lines.
#Newlines are preserved.
#This approach is useful when you want to create readable multiline strings without explicitly using the \n escape sequence.

#Hello world!'[1] evaluates to 'e'
#'Hello world!'[0:5] evaluates to 'Hello'
#'Hello world!'[:5] evaluates to 'Hello'
#'Hello world!'[3:] evaluates to 'lo world!'

#'Hello'.upper() evaluates to 'HELLO'
#'Hello'.upper().isupper() evaluates to True
#'Hello'.upper().lower() evaluates to 'hello'

#'Remember, remember, the fifth of November.'.split() evaluates to ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
#'-'.join('There can be only one.'.split()) evaluates to 'There-can-be-only-one.'

#To right-justify a string: Use the str.rjust(width) method.
#To left-justify a string: Use the str.ljust(width) method.
#To center a string: Use the str.center(width) method.

#To trim whitespace characters from the beginning or end of a string, you can use the following methods:
#To trim from the beginning (left side) of a string:
#Use str.lstrip(): This method removes leading (leftmost) whitespace characters.
original_string = "   Hello, World!   "
trimmed_left = original_string.lstrip()
#To trim from the end (right side) of a string:
#Use str.rstrip(): This method removes trailing (rightmost) whitespace characters.
original_string = "   Hello, World!   "
trimmed_right = original_string.rstrip()
#To trim from both the beginning and end of a string:
#Use str.strip(): This method removes leading and trailing whitespace characters.
original_string = "   Hello, World!   "
trimmed_both = original_string.strip()
