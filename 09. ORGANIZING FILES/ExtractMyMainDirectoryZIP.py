import os
import zipfile

def extract_zip(zip_file_path, extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    # Specify the path for the ZIP file and the extraction directory
    zip_file_path = "my_main_directory.zip"
    extraction_directory = "extracted_contents"

    # Extract the contents of the ZIP file
    extract_zip(zip_file_path, extraction_directory)

    print(f"Contents of {zip_file_path} have been extracted to {extraction_directory}.")
