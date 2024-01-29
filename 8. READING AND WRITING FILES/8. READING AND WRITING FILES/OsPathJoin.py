import os
#print(len(os.path.join('usr', 'bin', 'spam')))

#path = os.path.join('usr', 'bin', 'spam')
#print(path)
# Check the length of the string
#length_of_path = len(path)
#print("Length of the path:", length_of_path)

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))



