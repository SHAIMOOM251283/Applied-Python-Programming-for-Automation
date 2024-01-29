import os
def find_large_files(start_folder, min_size_in_bytes):
    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(start_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_size = os.path.getsize(file_path)
            # Check if the file size exceeds the specified threshold
            if file_size > min_size_in_bytes:
                print(f"Large File: {file_path} ({file_size} bytes)")
# Example usage with a minimum size of 100MB (100 * 1024 * 1024 bytes)
start_folder = 'C:\\Users\\Shaimoom\\Documents\\COMICS'
min_size_in_bytes = 100 * 1024 * 1024
find_large_files(start_folder, min_size_in_bytes)

#import os
#def find_files(start_folder):
    # Walk through the folder tree
#    for foldername, subfolders, filenames in os.walk(start_folder):
#        for filename in filenames:
#            file_path = os.path.join(foldername, filename)
#            file_size = os.path.getsize(file_path)
#            print(f"File: {file_path} ({file_size} bytes)")
# Example usage
#start_folder = 'E:\ALGORITHMS'
#find_files(start_folder)
