import os
import shutil

def copy_files_by_extensions(source_folder, destination_folder, file_extensions):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Walk through the source folder
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            # Check if the file has one of the desired extensions
            if any(filename.lower().endswith(ext.lower()) for ext in file_extensions):
                source_path = os.path.join(foldername, filename)
                destination_path = os.path.join(destination_folder, filename)

                # Copy the file to the destination folder
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {filename}")

# Example usage with new file extensions
source_folder = r'E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\9. ORGANIZING FILES\my_main_directory'
destination_folder = r'E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\9. ORGANIZING FILES\subfolder'
file_extensions = ['.jpg', '.txt']

copy_files_by_extensions(source_folder, destination_folder, file_extensions)
