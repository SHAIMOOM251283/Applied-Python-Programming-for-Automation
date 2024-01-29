#Functions are a fundamental building block in programming that promotes code organization, reusability, readability, and maintainability. 
#They contribute to creating more modular, flexible, and efficient programs.

#The code within a function executes when the function is called, not when it is defined. 
#When you define a function, you are essentially creating a reusable block of code with a specific set of instructions. 
#The actual execution of those instructions occurs only when the function is invoked or called.
#Here's a simple example:
def my_function():
    print("This code is inside the function.")
print("This code is outside the function.")
# Now, let's call the function
my_function()
#In this example, the code inside the my_function function is not executed when the function is defined. 
#Instead, it runs only when the function is called with my_function() later in the code. 
#When you run this Python script, you will see the output:
#This code is outside the function.
#This code is inside the function.
#The order of execution is top-down, so the code outside the function is executed first, and the function code is executed when the function is called.
#This separation between function definition and function execution is a fundamental aspect of procedural and object-oriented programming paradigms, allowing for modular and reusable code.

#In Python, the def statement is used to create a function. The basic syntax for defining a function in Python is as follows:
def greet(name):
    print("Hello, " + name + "!")
# Now, you can call the function
greet("Alice")
#In this example, the def statement is used to define a function named greet that takes a parameter name. 
#The code inside the function is indented, and the function body consists of a single print statement. 
#The function is then called with the argument "Alice".
#Remember that the code inside the function is not executed when the function is defined; it executes only when the function is called. 
#The def statement sets up the function, and you can call it later in your code to execute the defined functionality.

#Function:
#A function is a block of code that performs a specific task or a set of tasks. 
#It is a way to organize and structure code into reusable components. 
#Functions typically have a name, a set of parameters (optional), and a body containing the code to be executed when the function is called. 
#In Python functions can also return a value.
#Example of a function definition in Python:
def add_numbers(a, b):
    return a + b
#Function Call:
#A function call is the act of executing or invoking a function to perform its defined task. 
#When you call a function, you provide the required arguments (if any) and trigger the execution of the function's code. 
#The function call returns a result (if the function has a return statement).
#Example of a function call in Python:
result = add_numbers(3, 5)
print(result)
#In this example, add_numbers(3, 5) is a function call. 
#It passes the arguments 3 and 5 to the add_numbers function, which then returns the result 8. 
#The result is stored in the variable result and printed.
#In summary, a function is a defined block of code, and a function call is the execution of that code with specific arguments. 
#Functions provide a way to structure and modularize code, and function calls make use of that structure to perform specific tasks.
def add_numbers(a, b):
    return a + b
# Function call
result = add_numbers(3, 5)
# Print the result
print(result)
#When you run this Python script, it defines the add_numbers function, calls it with the arguments 3 and 5, and prints the result, which should be 8 in this case.

#In a Python program, there is one global scope, and each function call creates its own local scope. Let's break down the concepts:
#Global Scope:
#There is only one global scope in a Python progrom. 
#This is the outermost scope where variables and functions defined outside of any function or class are accessible. 
#The global scope spans the entire module or script.
#Example of a global variable in the global scope:
global_variable = 10
def my_function():
    print(global_variable)
my_function()  # This will print 10
#Local Scopes:
#Each time a function is called, it creates its own local scope. 
#Variables defined inside the function are local to that function and are not accessible outside of it. 
#Once the function finishes execution, its local scope is destroyed.
#Example of a local variable in a local scope:
def my_function():
    local_variable = 5
    print(local_variable)
my_function()  # This will print 5
# Attempting to access local_variable here would result in an error.
#In summary, a Python program has one global scope, and each function call creates a separate local scope. 
#The global scope is accessible throughout the entire program, while local scopes are confined to the respective functions in which they are created.

#When a function call in Python returns, the local scope associated with that function is destroyed, and the variables defined within that local scope cease to exist. 
#This process is known as the "scope resolution" or "variable scope."
def my_function():
    local_variable = 10
    print("Inside function:", local_variable)
my_function()  # Call the function
# Attempting to access local_variable here would result in an error.
#In this example, the local_variable is defined within the local scope of the my_function function. 
#When the function is called, it prints the value of local_variable. 
#However, once the function call completes, attempting to access local_variable outside the function would result in an error because the variable no longer exists in the current scope.
#Understanding variable scope is crucial for writing clean and bug-free code, and it helps prevent unintended variable conflicts and memory issues.

#A return value is the value that a function provides back to the caller when the function is executed. 
#In many programming languages, including Python, functions can be designed to perform a computation or a task and then return a result that can be used in the rest of the program.
#In Python, the return statement is used to specify the value that a function should return. Here's a simple example:
def add_numbers(a, b):
    result = a + b
    return result
# Function call and using the return value
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)
#In this example, the add_numbers function takes two parameters (a and b), calculates their sum, and returns the result using the return statement. 
#The returned value is then stored in the variable sum_result and printed.
#Regarding whether a return value can be part of an expression, the answer is yes. 
#The return value of a function can be used in expressions, assignments, or any context where a value is expected. Here's an example:
def multiply_numbers(x, y):
    return x * y
# Using the return value in an expression
product_result = multiply_numbers(4, 6) + 2
print("Product result:", product_result)
#In this example, the return value of the multiply_numbers function is used in an expression where it is added to 2. The result is then printed.
#So, in summary, a return value is the value that a function sends back to the caller, and it can be used in various contexts, including expressions.
#In order to store the value returned by a function, you use the return statement in the function. 
#The return statement specifies the value that the function will send back to the caller. 
#Once the function encounters a return statement, it immediately stops execution, and the specified value is returned to the caller.

#If a function in Python does not have a return statement, or if it has a return statement without specifying a value, the function will implicitly return a special value called None. 
#None is a built-in constant in Python that represents the absence of a value or a null value.
#Here's an example:
def my_function():
    print("This function does not have a return statement")
# Calling the function
result = my_function()
print("Result:", result)
#In this example, my_function does not have a return statement. 
#When you call this function and assign its result to a variable (result in this case), the variable will hold the value None. 
#When you run this code, the output will be:
#This function does not have a return statement
#Result: None

#In Python, if you want to force a variable in a function to refer to the global variable (rather than creating a new local variable with the same name), you can use the global keyword. 
#The global keyword is used to indicate that a particular variable is a global variable, even if it's within the scope of a function.
#Here's an example:
global_variable = 10
def modify_global_variable():
    global global_variable  # Using the 'global' keyword to refer to the global variable
    global_variable += 5
# Before the function call
print("Before:", global_variable)
# Calling the function
modify_global_variable()
# After the function call
print("After:", global_variable)
#In this example:
#The global_variable is defined outside the function and initially has a value of 10.
#The modify_global_variable function is defined, and within the function, the global keyword is used before the variable name to indicate that it is a global variable.
#The function is called, and it increments the value of the global variable by 5.
#Before and after the function call, the value of the global variable is printed.
#When you run this code, you should see the output:
Before: 10
After: 15
##Without using the global keyword inside the function, a new local variable with the same name would be created, and the global variable wouldn't be modified. 
#Using global explicitly tells Python to use the global variable instead of creating a local one.
#The aim is to modify the existing global variable from within the function, not to create a new one.

#In Python, None is a special constant representing the absence of a value or a null value. 
#It is often used to indicate that a variable or a function does not return anything.
#The data type of None is its own type, called NoneType. You can check the type of None using the type() function:
result = None
print(type(result))  # Output: <class 'NoneType'>
#Here, result is assigned the value None, and the type() function is used to determine its type, which is NoneType. 
#The NoneType is a built-in type in Python that has only one possible value, which is None.

#The statement import areallyourpetsnamederic attempts to import a module named "areallyourpetsnamederic" in Python. 
#If there is no such module, it will raise an ImportError. 
#If the module exists, it will be imported, and you can use its attributes, functions, or classes in your code.

#If you have a function named bacon() in a module named spam, and you want to call it after importing the spam module, you would use the following syntax:
import spam
# Call the bacon() function from the spam module
spam.bacon()
#Here's a breakdown of the steps:
#Use the import statement to import the spam module.
#Call the bacon() function using the syntax spam.bacon(). 
#This specifies that you want to call the bacon() function that is part of the spam module.
#Make sure that the module (in this case, spam.py) is located in the same directory as your script or in a directory listed in the Python path. 
#If the module is in a different directory, you might need to adjust the Python path or use relative/absolute imports.

#To prevent a program from crashing when it encounters an error, you can use exception handling. 
#In Python, you can use a try block to enclose the code that might raise an exception, and then use except blocks to handle specific types of exceptions. 
#This way, if an error occurs, the program can gracefully handle it without crashing.
#Here's a simple example:
try:
    # Code that might raise an exception
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    # The following line will only be reached if no exception occurs
    print("Result:", result)
except ValueError as ve:
    # Handle a ValueError (e.g., if the user doesn't enter a valid integer)
    print(f"Error: {ve}")
except ZeroDivisionError:
    # Handle a ZeroDivisionError (e.g., if the user enters a denominator of 0)
    print("Error: Cannot divide by zero.")
except Exception as e:
    # Handle other types of exceptions
    print(f"An unexpected error occurred: {e}")
# The program continues to run after the exception is handled
print("Program continues...")
#In this example:
#The try block contains the code that might raise an exception, such as attempting to divide by zero or attempting to convert a non-integer input to an integer.
#The except blocks handle specific types of exceptions, such as ValueError and ZeroDivisionError. You can catch more general exceptions using Exception.
#If an exception occurs, the program jumps to the corresponding except block, and the program continues to execute from there.

#The try and except statements in Python are used for exception handling. 
#Here's a breakdown of what typically goes in the try and except clauses:
#try Clause:
#The try clause contains the code that might raise an exception. 
#This is the section where you anticipate that an error might occur. It is the part of the code that you want to monitor for exceptions.
#Example:
try:
    # Code that might raise an exception
    result = 10 / int(input("Enter a number: "))
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
#In this example, the try block contains code that involves dividing a number by user input. 
#If the user enters a non-integer or 0, it may raise a ValueError or ZeroDivisionError.
#except Clause:
#The except clause specifies the type of exception that the code in the try block might raise. 
#If an exception of the specified type occurs, the corresponding except block is executed.
#Example:
try:
    # Code that might raise an exception
    result = 10 / int(input("Enter a number: "))
    print("Result:", result)
except ValueError:
    # Handle a ValueError (e.g., non-integer input)
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    # Handle a ZeroDivisionError (e.g., division by zero)
    print("Error: Cannot divide by zero.")
#In this example, there are specific except blocks for handling ValueError and ZeroDivisionError. 
#If a ValueError occurs (e.g., user enters a non-integer), the first except block is executed. 
#If a ZeroDivisionError occurs, the second except block is executed.
#In summary, the try block contains the code that might raise an exception, and the except block(s) contain the code to handle specific types of exceptions. 
#You can have multiple except blocks to handle different types of exceptions or a more general except block to catch any unexpected exceptions.
