#import zipfile, os
#os.chdir('E:\\') # move to the folder with example.zip
#exampleZip = zipfile.ZipFile('example.zip')
#print(exampleZip.namelist())
#spamInfo = exampleZip.getinfo('spam.txt')
#print(spamInfo.file_size)
#print(spamInfo.compress_size)
#print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
#exampleZip.close()


#import zipfile, os
#os.chdir('E:\\')  # move to the folder with example.zip
#exampleZip = zipfile.ZipFile('example.zip')
# Print the list of files in the ZIP archive
#print(exampleZip.namelist())
#spamInfo = exampleZip.getinfo('spam.txt')
# Print the file size
#print(f'The file size of spam.txt is: {spamInfo.file_size} bytes')
# Print the compressed size
#print(f'The compressed size of spam.txt is: {spamInfo.compress_size} bytes')
# Check if both file size and compressed size are greater than zero before calculating the compression ratio
#if spamInfo.file_size > 0 and spamInfo.compress_size > 0:
    # Print the compression ratio
#    compression_ratio = round(spamInfo.file_size / spamInfo.compress_size, 2)
#    print(f'Compressed file is {compression_ratio}x smaller!')
#else:
#    print('Cannot calculate compression ratio: either file size or compressed size is zero.')
#exampleZip.close()

#import zipfile
#import os
# Specify the path to the ZIP file
#zip_file_path = 'E:\example.zip'
# Specify the directory where you want to extract the contents
#extracted_dir = 'path/to/extracted/folder'
# Create the extracted directory if it doesn't exist
#if not os.path.exists(extracted_dir):
#    os.makedirs(extracted_dir)
# Open the ZIP file
#with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all contents to the specified directory
#    zip_ref.extractall(extracted_dir)
# List the contents of the extracted directory
#extracted_files = os.listdir(extracted_dir)
#print("Contents of the ZIP file:")
#for file in extracted_files:
#    print(file)

import zipfile
import os
def format_size(size):
    # Helper function to format file sizes for better readability
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
# Specify the path to the ZIP file
zip_file_path = 'E:\example.zip'
# Specify the directory where you want to extract the contents
extracted_dir = 'path/to/extracted/folder'
# Create the extracted directory if it doesn't exist
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)
# Open the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all contents to the specified directory
    zip_ref.extractall(extracted_dir)
    # List the contents of the ZIP file with size information
    print("Contents of the ZIP file:")
    for file_info in zip_ref.infolist():
        file_name = file_info.filename
        file_size = format_size(file_info.file_size)
        compress_size = format_size(file_info.compress_size)
        print(f"{file_name} - Original Size: {file_size}, Compressed Size: {compress_size}")


