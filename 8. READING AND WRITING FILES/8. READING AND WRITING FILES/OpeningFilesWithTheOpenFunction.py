#helloFile = open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r')

helloFile = open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r')
print(helloFile.read())
helloFile.close()  # It's good practice to close the file when you're done with it

with open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r') as helloFile:
    print(helloFile.read())

with open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r') as helloFile:
    content = helloFile.read()
    print(content)

with open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r', encoding='utf-8') as helloFile:
    content = helloFile.read()
    print(content)

try:
    with open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt', 'r') as helloFile:
        content = helloFile.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")


#import os
#file_path = 'E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt'
# Open the file using the default text editor
#os.system(f'start notepad.exe {file_path}')




