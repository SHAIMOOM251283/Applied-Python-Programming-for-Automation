import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

def encrypt_pdfs_in_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):
                input_path = os.path.join(root, file_name)
                output_path = os.path.join(root, f'{os.path.splitext(file_name)[0]}_encrypted.pdf')

                encrypt_pdf(input_path, output_path, password)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt_pdfs.py <folder_path> <password>")
        sys.exit(1)

    folder_path = sys.argv[1]
    password = sys.argv[2]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    encrypt_pdfs_in_folder(folder_path, password)
    print("PDF encryption completed.")

if __name__ == "__main__":
    main()
