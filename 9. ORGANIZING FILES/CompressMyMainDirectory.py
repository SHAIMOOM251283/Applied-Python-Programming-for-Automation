import os
import zipfile

def create_directory_structure():
    # Specify the main directory path
    main_directory = "my_main_directory"

    # Create the main directory
    os.makedirs(main_directory, exist_ok=True)

    # Create a text file in the main directory
    with open(os.path.join(main_directory, "main_text_file.txt"), "w") as main_file:
        main_file.write("This is the main text file.")

    # Create a sub-directory
    sub_directory = os.path.join(main_directory, "my_sub_directory")
    os.makedirs(sub_directory, exist_ok=True)

    # Create a text file in the sub-directory
    with open(os.path.join(sub_directory, "sub_text_file.txt"), "w") as sub_file:
        sub_file.write("This is the sub-text file.")

def compress_directory(directory_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, directory_path)
                zip_file.write(file_path, arcname)

if __name__ == "__main__":
    create_directory_structure()

    # Specify the paths for the main directory and the output ZIP file
    main_directory_path = "my_main_directory"
    zip_file_path = "my_main_directory.zip"

    # Compress the main directory into a ZIP file
    compress_directory(main_directory_path, zip_file_path)

    print(f"{main_directory_path} has been compressed into {zip_file_path}.")
