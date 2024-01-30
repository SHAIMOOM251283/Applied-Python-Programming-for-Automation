#The Unix epoch is a reference point used in computing to calculate time. 
#It represents the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC) on Thursday, January 1, 1970 (not counting leap seconds).

#In Python, you can use the time module to get the current time in seconds since the epoch.
import time
current_time = time.time()
print(current_time)

#You can use the time module in Python to pause the execution of your program for a specific duration. 
#The time.sleep() function is commonly used for this purpose. 
#To pause your Python program for exactly 5 seconds, you can use the following code:
import time
print("This is before the pause.")
time.sleep(5)  # Pause for 5 seconds
print("This is after the pause.")

#The round() function in Python is used to round a floating-point number to the nearest integer. 
#The syntax of the round() function is as follows:
#round(number[, ndigits])
#The round() function returns a floating-point number if ndigits is specified, and an integer otherwise. 
#When ndigits is specified, the result is a floating-point number rounded to the specified number of decimal places.
# Example 1: Round to the nearest integer
result1 = round(3.14)
print(result1)  # Output: 3
# Example 2: Round to one decimal place
result2 = round(3.14159, 1)
print(result2)  # Output: 3.1
# Example 3: Round to the nearest integer (no ndigits specified)
result3 = round(3.6)
print(result3)  # Output: 4
#The round() function rounds the number to the nearest integer.

#The datetime class is used to represent a specific point in time, including information about the year, month, day, hour, minute, second, and microsecond.
#Instances of the datetime class can be created to represent a particular date and time.
#Examples of creating datetime objects:
from datetime import datetime
# Current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
# Specific date and time
specific_datetime = datetime(2022, 1, 14, 12, 30, 0)
print("Specific Date and Time:", specific_datetime)
#The timedelta class represents the difference between two dates or times, measured in days, hours, minutes, seconds, and microseconds.
#Instances of the timedelta class are created by subtracting one datetime object from another.
#Examples of creating timedelta objects:
from datetime import datetime, timedelta
# Calculate the difference between two datetimes
datetime1 = datetime(2022, 1, 10)
datetime2 = datetime(2022, 1, 15)
difference = datetime2 - datetime1
print("Difference between two datetimes:", difference)
# Create a timedelta with a specific duration
duration = timedelta(days=5, hours=3)
print("Timedelta with a specific duration:", duration)
#A simple example combining both datetime and timedelta:
from datetime import datetime, timedelta
# Current date and time
current_datetime = datetime.now()
# Create a timedelta representing 2 days
two_days = timedelta(days=2)
# Add the timedelta to the current datetime
new_datetime = current_datetime + two_days
print("Current datetime:", current_datetime)
print("New datetime after adding 2 days:", new_datetime)

#To run the spam() function in a separate thread, you can use the threading module in Python. Here's an example:
import threading
def spam():
    # Your code inside the spam function
    print("Executing code inside spam function")
# Create a thread and pass the spam function as the target
thread = threading.Thread(target=spam)
# Start the thread
thread.start()
# Wait for the thread to finish (optional)
thread.join()
# The code inside spam() will run concurrently in the separate thread
#In this example, a new thread is created using the threading.Thread class, and the spam function is passed as the target. 
#The start() method is then called to initiate the execution of the thread. 
#The join() method is optional and can be used if you want the main program to wait for the thread to finish before proceeding.

#To avoid concurrency issues with multiple threads, you should consider using synchronization mechanisms and follow best practices for thread safety. 
#Some common techniques to prevent concurrency issues:
#locking (mutexes)
#thread-safe data structures
#thread-safe libraries
#exception handling
#thread local storage
#atomic operations
import threading
shared_variable = 0
lock = threading.Lock()
def increment():
    global shared_variable
    with lock:
        shared_variable += 1
# Create threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
# Start threads
thread1.start()
thread2.start()
# Wait for threads to finish
thread1.join()
thread2.join()
# Print the final value of shared_variable
print("Final value of shared_variable:", shared_variable)
#In this example, two threads (thread1 and thread2) are created, and both execute the increment function concurrently. 
#The threading.Lock ensures that only one thread can modify the shared_variable at a time, preventing potential race conditions. 
#The final value of shared_variable is printed after both threads have completed their execution.

#You can use the subprocess module in Python to run external programs, including calc.exe. Here's an example of how you can do it:
import subprocess
# Specify the path to calc.exe
calc_path = r'C:\Windows\System32\calc.exe'
# Use subprocess to run calc.exe
subprocess.run(calc_path)
