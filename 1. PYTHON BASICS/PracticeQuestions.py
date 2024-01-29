# Operators:
#    * (Multiplication)
#    - (Subtraction)
#    / (Division)
#    + (Addition)

# Values:
#    'hello' (String)
#    -88.8 (Float)
#    5 (Integer)

# Operators perform operations on values.
# Values are the actual data entities.

# spam (this is a variable)
# 'spam' (this is a string)

# Three common data types in programming:
# Integer (int): Represents whole numbers without any decimal points. Examples include 1, -5, and 1000.
# Float (float): Represents numbers with decimal points or in exponential form. Examples include 3.14, -0.5, and 2.5e3.
# String (str): Represents sequences of characters. Strings are used to represent text. Examples include 'hello', "world", and '123'.

# An expression in programming is made up of one or more operands and operators. These components combine to produce a value. 
# Here's a breakdown:
# Operands: These are the values or variables that the operators act upon. For example, in the expression 2 + 3, the operands are 2 and 3.
# Operators: These are symbols or keywords that perform operations on one or more operands. In the expression 2 + 3, the operator is +, and it adds the values of the operands.
# Expressions can be simple or complex. 
# Simple expressions might involve a single value or a variable, while complex expressions involve multiple values, variables, and operators.
# Expressions, when evaluated, result in a single value. 
# The value can be of any data type, such as integers, floating-point numbers, strings, or others, depending on the operations and data types involved in the expression. 
# Expressions are used to perform calculations, manipulate data, and make decisions in a program.
x = 5
y = 3
result = x + y  # This expression (x + y) evaluates to 8, and the result is assigned to the variable 'result'.
#print(result)

# In programming, expressions and statements are two fundamental concepts, but they serve different purposes:
# Expression:
#        An expression is a combination of values, variables, and operators that, when evaluated, results in a single value.
#        Expressions can be as simple as a single variable or complex combinations of multiple values and operators.
#        Examples of expressions include 2 + 3, x * y, or len("hello").
#        The primary purpose of an expression is to compute a value.
# Statement:
#        A statement is a complete line of code that performs a specific action. It can include one or more expressions and is often terminated by a newline character.
#        Statements can include assignments, loops, conditionals, function calls, and other actions.
#        Examples of statements include variable assignments (x = 5), conditional statements (if x > 0:), or loops (for i in range(5):).
#        The primary purpose of a statement is to execute a specific task or operation.
# In summary, expressions are components that result in a value when evaluated, while statements are complete units of code that perform actions. 
# A statement may contain expressions, but an expression alone is not a complete statement.

bacon = 20
bacon + 1
# The variable bacon is assigned the value 20, and then bacon + 1 is computed. 
# However, the result of bacon + 1 is not stored or assigned to any variable. Therefore, the value of bacon remains unchanged.
# If you want to update the value of bacon by adding 1 to it, you should reassign the result back to the variable:
bacon = 20
bacon = bacon + 1
# Now, after this code runs, the variable bacon will contain the value 21.

# 'spam' + 'spamspam': This expression concatenates two strings. The result will be a new string formed by joining the two original strings.
# Result: 'spamspamspam'
# 'spam' * 3: This expression repeats the string 'spam' three times (multiplies the string by 3).
# Result: 'spamspamspam'
# In both cases, the result is the same string, 'spamspamspam'.

# In Python, variable names have certain rules and conventions. According to Python's naming rules:
#    Variable names must begin with a letter (a-z, A-Z) or an underscore (_).
#    The rest of the variable name can include letters, numbers, and underscores.
# Applying these rules:
#    'eggs' is a valid variable name because it starts with a letter ('e') and is followed by other letters.
#    100 is invalid as a variable name because it begins with a number. Variable names cannot start with a number according to Python's naming rules.
# Here's an example:
eggs = 'This is a valid variable name.'
# 100 = 'This is an invalid variable name.'  # This would raise a SyntaxError

# In Python, you can use the following three functions to get the integer, floating-point number, or string version of a value:
# int(x): This function can be used to convert a value to an integer. It truncates the decimal part of a floating-point number or converts a string representation of an integer to an actual integer.
# Example:
value = int(3.14)  # Converts 3.14 to 3
# float(x): This function converts a value to a floating-point number. It can convert integers, strings representing numbers, or other compatible types to floating-point numbers.
# Example:
value = float("5.7")  # Converts the string "5.7" to the float 5.7
# str(x): This function converts a value to a string. It can be used to convert integers, floating-point numbers, or other data types to their string representations.
# Example:
value = str(42)  # Converts the integer 42 to the string "42"

# The expression 'I have eaten ' + 99 + ' burritos.' causes an error because you are attempting to concatenate a string ('I have eaten ') with an integer (99) directly. 
# In Python, the + operator is overloaded for string concatenation when used with strings, but it doesn't work seamlessly with other data types like integers.
# To fix this, you need to convert the integer 99 to a string before concatenating it with the other strings. 
# You can do this using the str() function:
result = 'I have eaten ' + str(99) + ' burritos.'
print(result)
# This will output:I have eaten 99 burritos.
# By using str(99), you convert the integer 99 to a string before concatenating it, making the expression valid.