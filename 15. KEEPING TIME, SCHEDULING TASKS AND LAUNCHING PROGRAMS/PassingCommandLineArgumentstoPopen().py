#import subprocess
#subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])

import subprocess
import os

# Set the current directory to the desired location
current_directory = os.getcwd()

# Specify the file path in the current directory
file_path = os.path.join(current_directory, 'hello.txt')

# Create the hello.txt file in the current directory
with open(file_path, 'w') as file:
    file.write("Hello, world!")

# Open Notepad with the file in the current directory
subprocess.Popen(['C:\\Windows\\notepad.exe', file_path])
