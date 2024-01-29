#import os
#for folderName, subfolders, filenames in os.walk('E:\\delicious'):
#   print('The current folder is ' + folderName)
#   for subfolder in subfolders:
#     print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#for filename in filenames:
# print('FILE INSIDE ' + folderName + ': '+ filename)
# print('')

import os

root_folder = 'E:\\delicious'

for folderName, subfolders, filenames in os.walk(root_folder):
    print('The current folder is ' + folderName)

    # Rename files in the current folder
    for filename in filenames:
        current_file_path = os.path.join(folderName, filename)

        # Define a new name for the file (you can modify this logic as needed)
        new_filename = "new_" + filename

        # Construct the new path for the file
        new_file_path = os.path.join(folderName, new_filename)

        # Rename the file
        os.rename(current_file_path, new_file_path)

        print('Renamed: ' + current_file_path + ' to ' + new_file_path)

    print('')




