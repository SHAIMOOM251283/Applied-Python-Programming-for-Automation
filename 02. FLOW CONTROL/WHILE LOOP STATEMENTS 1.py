#In this code snippet, you initialize the variable spam with the value 0. 
#Then, there is an if statement that checks whether spam is less than 5. 
#Since spam is initially 0, the condition is true, and it enters the block. 
#It prints 'Hello, world.' and increments the value of spam by 1. 
#Now spam is 1, and if you were to run this code again, the condition if spam < 5 would still be true, and 'Hello, world.' would be printed again. 
#However, if you were to run this code repeatedly without restarting it, it would print 'Hello, world.' only once because the value of spam is updated to 1.
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

#In this code snippet, you use a while loop with the condition while spam < 5. 
#The loop will continue executing the indented block of code as long as the condition is true. 
#Inside the loop, it prints 'Hello, World.' and increments the value of spam by 1. 
#As long as spam remains less than 5, the loop continues to execute, printing 'Hello, World.' and updating the value of spam. Once spam becomes 5, the condition becomes false, and the loop exits.
spam = 0
while spam < 5:
    print('Hello, World.')
    spam = spam + 1