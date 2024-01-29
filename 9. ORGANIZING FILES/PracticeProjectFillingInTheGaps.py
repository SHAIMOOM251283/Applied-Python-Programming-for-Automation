import os
import re
import shutil
def close_numbering_gaps(folder_path, prefix):
    file_pattern = re.compile(rf'{re.escape(prefix)}(\d+)(\.\w+)$')
    # Find all files with the given prefix
    files = [file for file in os.listdir(folder_path) if file_pattern.match(file)]
    # Sort files based on the numeric part of the filename
    files.sort(key=lambda x: int(file_pattern.match(x).group(1)))
    # Iterate through files and close gaps
    expected_number = 1
    for file in files:
        current_number = int(file_pattern.match(file).group(1))
        if current_number != expected_number:
            # Rename the file to close the gap
            new_name = f'{prefix}{expected_number:03d}{file_pattern.match(file).group(2)}'
            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        expected_number += 1
# Example usage
folder_path = 'E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\9. ORGANIZING FILES\\ForPracticeProject3'
prefix = 'spam'
close_numbering_gaps(folder_path, prefix)

#import os
#import re
#import shutil
#def insert_numbering_gap(folder_path, prefix, gap_index):
#    file_pattern = re.compile(rf'{re.escape(prefix)}(\d+)(\.\w+)$')
    # Find all files with the given prefix
#    files = [file for file in os.listdir(folder_path) if file_pattern.match(file)]
    # Sort files based on the numeric part of the filename
#    files.sort(key=lambda x: int(file_pattern.match(x).group(1)))
    # Iterate through files and insert the gap
#    for file in files:
#        current_number = int(file_pattern.match(file).group(1))
#        if current_number >= gap_index:
            # Rename the file to create a gap
#            new_name = f'{prefix}{current_number + 1:03d}{file_pattern.match(file).group(2)}'
#            shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
# Example usage
#folder_path = 'E:\\LEARNING PYTHON\\AUTOMATE THE BORING STUFF\\9. ORGANIZING FILES\\ForPracticeProject3'
#prefix = 'spam'
#gap_index = 2  # Insert a gap before file spam002.txt
#insert_numbering_gap(folder_path, prefix, gap_index)
