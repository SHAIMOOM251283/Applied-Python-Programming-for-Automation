helloFile = open('E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\8. READING AND WRITING FILES\\hello.txt')
print(helloFile.read())
#helloContent = helloFile.read()
#print(helloContent)

sonnetFile = open('E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\8. READING AND WRITING FILES\sonnet29.txt')
print(sonnetFile.readlines())

sonnetFile = open('E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\8. READING AND WRITING FILES\sonnet29.txt')
for line in sonnetFile.readlines():
    print(line)
sonnetFile.close()  # It's good practice to close the file when you're done with it

with open('E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\8. READING AND WRITING FILES\sonnet29.txt') as sonnetFile:
    for line in sonnetFile.readlines():
        print(line)
