#spam = 7  # You can change this value to test the assertion
#assert not isinstance(spam, int) or spam >= 10, "The variable 'spam' should be an integer greater than or equal to 10."
# An assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

#eggs = "Hello"
#bacon = "hello"  # Change this value to test the assertion
#assert eggs.casefold() != bacon.casefold(), "The variables 'eggs' and 'bacon' should have different strings, ignoring case."
# An assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other.

#assert False, "This assert statement always triggers an AssertionError."
# An assert statement that always triggers an AssertionError.

#import logging
#logging.basicConfig(level=logging.DEBUG)
# The two lines that a program must have in order to be able to call logging.debug()

#import logging
#logging.basicConfig(filename='programLog.txt', level=logging.DEBUG)
# The two lines that a program must have in order to have logging.debug() send a logging message to a file named programLog.txt.

#In Python's logging module, there are five standard logging levels, listed in increasing order of severity:
#DEBUG: Detailed information, typically useful for diagnosing problems. This is the lowest severity level.
#INFO: General information about the program's execution. Typically, you use this level for high-level flow and important events.
#WARNING: Indicates a potential problem or something that might be an issue in the future, but the program can still continue.
#ERROR: Indicates a more serious problem that prevented a part of the program from functioning correctly.
#CRITICAL: A very severe error that may lead to the program's inability to continue running.

#logging.disable(logging.CRITICAL)
# Line of code to disable all logging messages.

#Using logging messages is generally preferred over using print() for several reasons:
#Configurability: The logging module allows you to configure the logging behavior globally for your entire application. You can easily change the log level, format, and destination without modifying the code. This is particularly useful in larger projects where different parts of the code may have different logging requirements.
#Severity Levels: Logging provides different severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), allowing you to categorize and filter messages based on their importance. This can be extremely helpful for debugging and troubleshooting, as you can control the amount of detail in your log output.
#Flexibility: With logging, you can easily direct log messages to different outputs, such as the console, files, databases, or external services, by configuring different log handlers. This makes it more versatile than print(), which sends output to the console by default.
#Structured Output: Logging messages can include additional contextual information (e.g., timestamps, source of the log message, etc.) without cluttering your code. This structured output is often more helpful for understanding the flow of the program and diagnosing issues.
#Silent Production Mode: In production environments, you can configure logging to output only critical errors, suppressing less important log messages. This allows you to keep your logs concise and focused on issues that require attention.
#Integration with Libraries: Many libraries and frameworks use the logging module for their own logging. By using the same logging infrastructure, you can consolidate log messages from different parts of your application and third-party libraries.
#Conditional Logging: With logging statements, you can easily conditionally include or exclude log messages based on certain conditions or settings. This provides more control over what gets logged in different scenarios.
#While print() statements can be convenient for quick debugging, logging is a more sophisticated and scalable approach, particularly for larger and more complex projects. It offers better control, configurability, and consistency in handling log messages throughout your codebase.

# "Step Into" allows you to step through code line by line, entering into functions.
# "Step Over" lets you execute the entire current line, skipping over function details.
# "Step Out" is used to complete the execution of the current function and return to the calling context.

# Clicking "Go" in the Debug Control window during debugging, the debugger will continue the execution of your program until one of the following events occurs:
#Breakpoint is Encountered:
    #If there is a breakpoint set in the code, the debugger will stop when the program reaches that breakpoint. 
#Program Completes Execution:
    #If the program reaches its end and completes execution, the debugger will stop. This is applicable when running    program in debug mode until it finishes.
#Exception is Raised:
    #If an unhandled exception occurs during the execution of the program, the debugger will stop at the point where the exception is raised. 
#User Interrupts:
    #Manually interrupt the execution by pressing a "Stop" or "Interrupt" button. This will cause the debugger to stop at the current point in the code.

# A breakpoint is a designated point in the source code where the debugger will pause the execution of the program, allowing inspection of its state, variables, and overall behavior. 

#def example_function():
#    x = 10
#    y = 20
#    import pdb; pdb.set_trace()  # Set breakpoint here. Use built in pdb (Python Debugger) 
#    z = x + y
#    print(z)
#example_function()
# Add breakpoint at the left side of the margin.

