#import zipfile
#def read_zip(zip_file_path):
#    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Get a list of all the files and folders in the ZIP file
#        zip_contents = zip_ref.namelist()
        # Print the contents
#        print("Contents of the ZIP file:")
#        for item in zip_contents:
#            print(item)
#if __name__ == "__main__":
    # Specify the path for the ZIP file
#    zip_file_path = "my_main_directory.zip"
    # Read and print the contents of the ZIP file
#    read_zip(zip_file_path)

import zipfile
import os

def read_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Get a list of all the files and folders in the ZIP file
        zip_contents = zip_ref.namelist()

        # Print the contents and their sizes
        print("Contents of the ZIP file:")
        for item in zip_contents:
            size = zip_ref.getinfo(item).file_size
            print(f"{item} - {size} bytes")

if __name__ == "__main__":
    # Specify the path for the ZIP file
    zip_file_path = "my_main_directory.zip"

    # Read and print the contents of the ZIP file with sizes
    read_zip(zip_file_path)
