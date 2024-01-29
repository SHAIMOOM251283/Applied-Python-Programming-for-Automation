import zipfile
import os

zip_filename = 'example_zipfile.zip'
text_file_name = 'example.txt'
subfolder_name = 'subfolder'
file_in_subfolder = 'subfolder/file.txt'

# Create a text file at the root level
with open(text_file_name, 'w') as text_file:
    text_file.write('This is a text file at the root level.')

# Create the subfolder and file
os.makedirs(subfolder_name, exist_ok=True)
with open(file_in_subfolder, 'w') as text_file:
    text_file.write('This is a text file inside the subfolder.')

with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    # Create a text file at the root level
    zip_file.write(text_file_name, arcname=text_file_name)

    # Create a sub-folder
    zip_file.write(subfolder_name, arcname=subfolder_name)

    # Create a file inside the sub-folder
    zip_file.write(file_in_subfolder, arcname=file_in_subfolder)

print(f'Zip file "{zip_filename}" created with sub-folder and files.')
