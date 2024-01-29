#The Boolean data type has two possible values: true and false. 
#In programming languages, these values are often represented using the keywords "true" and "false" (case-insensitive in some languages).
#my_boolean_variable = True
#var myBooleanVariable = false;
#boolean myBooleanVariable = true;
#These values are commonly used in conditional statements, loops, and other control flow structures to make decisions based on whether a condition is true or false.

#The three fundamental Boolean operators are:
#AND (&&): Returns true if both operands are true; otherwise, it returns false.
#Example:
result = (True and False)  # Result is False
#OR (||): Returns true if at least one of the operands is true; returns false if both are false.
#Example:
result = (True or False)  # Result is True
#NOT (!): Returns the opposite of the operand's truth value; if the operand is true, it returns false, and vice versa.
#Example:
result = not True  # Result is False
#These operators are often used in combination to create complex conditions and expressions in programming. 
#They are essential for constructing logical statements that determine the flow of a program based on certain conditions.

#Here are the truth tables for the three basic Boolean operators:
#AND (&&):
#A	    B	    A && B
#True	True	True
#True	False	False
#False	True	False
#False	False	False
#OR (||):
#| A | B | A || B |
#|-------|-------|--------|
#| True | True | True |
#| True | False | True |
#| False | True | True |
#| False | False | False |
#NOT (!):
#A	    !A
#True	False
#False	True

#(5 > 4) and (3 == 5)
#    The first part (5 > 4) is True.
#    The second part (3 == 5) is False.
#    The entire expression evaluates to True and False, which is False.
#not (5 > 4)
#    The expression inside the not is True.
#    The entire expression evaluates to not True, which is False.
#(5 > 4) or (3 == 5)
#    The first part (5 > 4) is True.
#    The second part (3 == 5) is False.
#    The entire expression evaluates to True or False, which is True.
#not ((5 > 4) or (3 == 5))
#    The expression inside the outer not is True (as evaluated in the previous step).
#    The entire expression evaluates to not True, which is False.
#(True and True) and (True == False)
#    The first part True and True is True.
#    The second part True == False is False.
#    The entire expression evaluates to True and False, which is False.
#(not False) or (not True)
#    The first part not False is True.
#    The second part not True is False.
#    The entire expression evaluates to True or False, which is True.

#The six comparison operators are used to compare values and produce a Boolean result (True or False). Here they are:
    #Equal to (==): Returns True if the values on both sides are equal.
    #Example: 5 == 5 evaluates to True.
    #Not equal to (!=): Returns True if the values on both sides are not equal.
    #Example: 5 != 4 evaluates to True.
    #Greater than (>): Returns True if the value on the left is greater than the value on the right.
    #Example: 6 > 4 evaluates to True.
    #Less than (<): Returns True if the value on the left is less than the value on the right.
    #Example: 3 < 7 evaluates to True.
    #Greater than or equal to (>=): Returns True if the value on the left is greater than or equal to the value on the right.
    #Example: 5 >= 5 evaluates to True.
    #Less than or equal to (<=): Returns True if the value on the left is less than or equal to the value on the right.
    #Example: 4 <= 6 evaluates to True.

#Equal to operator (==):
#The equal to operator is a comparison operator used to check if two values are equal.
#It returns a Boolean value (True or False) based on whether the values on both sides of the operator are equal.
#Example:
x = 5
y = 7
result = (x == y)  # This evaluates to False
#Assignment operator (=):
#The assignment operator is used to assign a value to a variable.
#It does not compare values; instead, it assigns the value on the right-hand side to the variable on the left-hand side.
#Example:
x = 5  # Assigns the value 5 to the variable x
y = x  # Assigns the value of x to the variable y
#In summary, == is used for comparison, checking if two values are equal, while = is used for assignment, assigning a value to a variable. 
#It's important not to confuse the two, as using the wrong operator can lead to unintended behavior in your code.

#In programming, a condition is a statement or expression that evaluates to either true or false. 
#Conditions are used to control the flow of a program by determining whether certain blocks of code should be executed or skipped based on the evaluation result. 
#They are fundamental to the concept of decision-making and branching in programming.
#The most common use of conditions is in control flow structures, such as:
#If statements: 
#These are used to execute a block of code only if a specified condition is true. If the condition is false, the block is skipped.
#Example (in Python):
x = 10
if x > 5:
    print("x is greater than 5")
#Else statements: 
#These are often used in conjunction with if statements to specify a block of code to be executed when the if condition is false.
#Example (in Python):
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#Elif statements: 
#Short for "else if," these are used to check multiple conditions in sequence. 
#If the preceding if or elif condition is true, the subsequent blocks are skipped.
#Example (in Python):
x = 5
if x > 5:
    print("x is greater than 5")
elif x < 5:
    print("x is less than 5")
else:
    print("x is equal to 5")
#Conditions are crucial for creating dynamic and flexible programs that can respond to different scenarios. 
#They allow you to make decisions and execute specific code based on the current state of your program or the values of variables.

#In the provided code snippet, there are three distinct blocks of code. Blocks in Python are defined by indentation. 
#Here are the three blocks identified:
#Outer Block
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
#This block includes the initialization of the spam variable and the start of the outermost if statement.
#Inner Block (under the second if statement)
        print('bacon')
#This block is indented under the second if statement and contains the print('bacon') statement.
#Else Block (under the else statement)
#else:
    print('ham')
    print('spam')
#This block is indented under the else statement and includes the print('ham') and print('spam') statements.
#The code consists of an outer block, an inner block, and an else block. 
#It's important to note that Python relies on indentation to define the scope of blocks, and proper indentation is crucial for the code to execute as intended.

spam = 1  # You can change the value of spam to test different cases
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
#In this code:
#    If the value stored in spam is equal to 1, it will print 'Hello'.
#    If the value stored in spam is equal to 2, it will print 'Howdy'.
#    If neither of the above conditions is true (i.e., anything else is stored in spam), it will print 'Greetings!'.

#If your program is stuck in an infinite loop while running in a terminal or console, you can usually interrupt the execution by pressing a specific key combination. 
#Windows:
    #Press Ctrl + C to break out of the infinite loop.

#"break" and "continue" are control flow statements used in loops (such as for and while loops) to modify the normal execution of the loop.
#break:
    #The break statement is used to exit a loop prematurely.
    #When a break statement is encountered inside a loop, the loop is terminated immediately, and the program continues with the next statement after the loop.
    #It is often used when a certain condition is met, and there is no need to continue the loop.
    #Example:
for i in range(5):
    if i == 3:
        break
    print(i)
#Output:
0
1
2
#continue:
    #The continue statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration.
    #It is helpful when you want to skip specific iterations based on a certain condition without terminating the entire loop.
#Example:
for i in range(5):
    if i == 2:
        continue
    print(i)
#Output:
0
1
3
4
#In summary, break is used to exit the loop prematurely, 
#while continue is used to skip the rest of the code in the current iteration and move to the next iteration of the loop.

#In a for loop in Python, range() is a built-in function that generates a sequence of numbers. 
#The three forms you mentioned—range(10), range(0, 10), and range(0, 10, 1)—are equivalent and will produce the same result when used in a for loop. 
#However, there are subtle differences in how they are expressed:
#range(10):
        #This form creates a sequence of numbers starting from 0 (default starting value) up to, but not including, 10.
        #It implicitly starts at 0 and increments by 1 (default step value).
    #Example:
for i in range(10):
    print(i)
#Output:
0
1
2
3
4
5
6
7
8
9
#range(0, 10):
    #This form explicitly specifies both the start (0) and the end (10) values for the sequence.
    #It still increments by 1 by default.
#Example:
for i in range(0, 10):
    print(i)
#Output is the same as the previous example.
#range(0, 10, 1):
    #This form explicitly specifies the start (0), end (10), and step (1) values for the sequence.
    #The step value determines the interval between numbers in the sequence. In this case, it increments by 1.
#Example:
for i in range(0, 10, 1):
    print(i)
#    Output is the same as the previous examples.
#In summary, all three forms generate the same sequence of numbers in a for loop. 
#The default values for start and step are 0 and 1, respectively, so if they are not explicitly specified, they take on these default values.

#A short program using a for loop and a while loop to print the numbers 1 to 10:
#Using a for loop:
for i in range(1, 11):
    print(i)
#Using a while loop:
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
#In the for loop example, range(1, 11) generates a sequence of numbers from 1 to 10 (inclusive), and the loop iterates over each number, printing it.
#In the while loop example, a counter variable is initialized to 1, and the loop continues as long as the counter is less than or equal to 10. 
#Inside the loop, the counter is printed, and then it is incremented by 1 in each iteration.
#Both programs will output the numbers 1 to 10.

#If you have a function named bacon() inside a module named spam, and you want to call it after importing the spam module, you can use the following syntax:
import spam
spam.bacon()
#This assumes that the bacon() function is defined within the spam module. 
#The import spam statement brings the entire module into your program, and then you can use dot notation (spam.bacon()) to access and call the bacon() function within the spam module.
#A python script can be used as a module. The spam.py is created in the directory so that spam can be imported. 