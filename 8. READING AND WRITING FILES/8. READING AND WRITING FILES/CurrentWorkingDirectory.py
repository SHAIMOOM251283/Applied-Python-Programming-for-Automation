import os
print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())
os.chdir('C:\\ThisFolderDoesNotExist')
print(os.getcwd)