import os
for filename in os.listdir():
   if filename.endswith('.txt'):
     os.unlink(filename)
     #print(filename)

#import os
#directory_path = 'E:\\'  
#for filename in os.listdir(directory_path):
#    if filename.endswith('.rxt'):
        # Full path to the file
#        file_path = os.path.join(directory_path, filename)
        # Uncomment the line below to delete the file
#        os.unlink(file_path)
        #print(file_path)
