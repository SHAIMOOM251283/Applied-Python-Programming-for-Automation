baconFile = open('bacon.txt', 'w') 
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a') 
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

#import os
# Get the directory of the script
#script_dir = os.path.dirname(os.path.abspath(__file__))
# Create the file 'bacon.txt' in the same directory as the script
#baconFile = open(os.path.join(script_dir, 'bacon.txt'), 'w')
#baconFile.write('Hello world!\n')
#baconFile.close()
# Open the file in append mode and write additional content
#baconFile = open(os.path.join(script_dir, 'bacon.txt'), 'a')
#baconFile.write('Bacon is not a vegetable.')
#baconFile.close()
# Open the file and read its content
#baconFile = open(os.path.join(script_dir, 'bacon.txt'))
#content = baconFile.read()
#baconFile.close()
# Print the content
#print(content)
