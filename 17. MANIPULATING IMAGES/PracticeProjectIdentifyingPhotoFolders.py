import os
from PIL import Image
from concurrent.futures import ProcessPoolExecutor, as_completed

def is_photo_folder(folder_path):
    supported_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in supported_extensions:
                return True
    return False

def process_folder(folder_path):
    if is_photo_folder(folder_path):
        print(f"Potential photo folder found: {folder_path}")

def search_photo_folders(root_path):
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_folder, os.path.join(root, folder)) for root, dirs, _ in os.walk(root_path) for folder in dirs]

        for future in as_completed(futures):
            # Handle exceptions if any task fails
            try:
                future.result()
            except Exception as e:
                print(f"Error processing folder: {e}")

    print("All tasks completed.")

if __name__ == "__main__":
    # Replace 'C:\\' with the root path of your hard drive or the specific folder you want to start the search from.
    root_directory = 'C:\\'
    
    search_photo_folders(root_directory)
