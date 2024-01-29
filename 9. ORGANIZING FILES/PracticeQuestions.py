import shutil
src_file = 'path/to/source/file.txt'
dst_file = 'path/to/destination/file.txt'
shutil.copy(src_file, dst_file)
# This function is used to copy a single file from the source (src) to the destination (dst).

import shutil
src_file = 'path/to/source/file.txt'
dst_file = 'path/to/destination/file.txt'
shutil.copy(src_file, dst_file)
# This function is used to recursively copy an entire directory tree from the source (src) to the destination (dst).

import shutil
src_dir = 'path/to/source/directory'
dst_dir = 'path/to/destination/directory'
shutil.copytree(src_dir, dst_dir)
# shutil.copy() is used for copying individual files, while shutil.copytree() is used for recursively copying entire directory trees.

import os
current_name = 'old_file.txt'
new_name = 'new_file.txt'
# Specify the current name and the new name
os.rename(current_name, new_name)
# To rename files in Python, the os.rename() function is used.

from send2trash import send2trash
file_path = 'path/to/file.txt'
send2trash(file_path)
# The send2trash module moves files or directories to the trash or recycle bin, providing a way to recover them

import shutil, os
file_path = 'path/to/file.txt'
dir_path = 'path/to/directory'
# Remove a file
os.remove(file_path)
# Remove a directory and its contents
shutil.rmtree(dir_path)
# The shutil functions permanently delete files and directories.

from zipfile import ZipFile
# Open an existing ZIP file in read mode
with ZipFile('example.zip', 'r') as zip_file:
    # Print the list of files in the ZIP file
    file_list = zip_file.namelist()
    print("Files in the ZIP file:", file_list)
    # Extract all files in the ZIP file to a specified directory
    extraction_path = 'extracted_files'
    zip_file.extractall(extraction_path)
    print(f"Files extracted to {extraction_path}")
# The ZipFile method that is equivalent to the open() method for regular file objects is ZipFile() itself.
    
from zipfile import ZipFile
# Create a new ZIP file or overwrite an existing one
with ZipFile('new_example.zip', 'w') as zip_file:
    # Add a single file to the ZIP file
    file_to_add = 'file_to_add.txt'
    zip_file.write(file_to_add, arcname='path/in/zip/file_to_add.txt')
    print(f"{file_to_add} added to the ZIP file")

    # Add multiple files to the ZIP file
    files_to_add = ['file1.txt', 'file2.txt']
    for file in files_to_add:
        zip_file.write(file, arcname=f'path/in/zip/{file}')
    print(f"Files added to the ZIP file")
# At this point, the new ZIP file is automatically closed


