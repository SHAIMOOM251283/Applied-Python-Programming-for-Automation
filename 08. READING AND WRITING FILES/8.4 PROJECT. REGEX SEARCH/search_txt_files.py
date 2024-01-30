import os
import re

def search_files_in_folder(folder_path, regex_pattern):
    # Get a list of all .txt files in the specified folder
    txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

    if not txt_files:
        print(f"No .txt files found in {folder_path}")
        return

    # Iterate through each .txt file and search for the regular expression
    for txt_file in txt_files:
        file_path = os.path.join(folder_path, txt_file)
        print(f"Searching in {file_path}:")

        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(regex_pattern, line):
                    print(f"  Line {line_number}: {line.strip()}")

        print("\n")

if __name__ == "__main__":
    # Get user input for folder path and regular expression
    folder_path = input("Enter the folder path: ")
    regex_pattern = input("Enter the regular expression: ")

    # Call the function to search for the pattern in .txt files
    search_files_in_folder(folder_path, regex_pattern)
