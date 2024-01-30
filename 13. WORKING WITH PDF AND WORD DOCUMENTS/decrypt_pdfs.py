import os
import fitz  # PyMuPDF

def decrypt_pdf(input_path, output_path, password):
    try:
        pdf_document = fitz.open(input_path)

        if pdf_document.isEncrypted:
            if pdf_document.authenticate(password):
                pdf_document.save(output_path)
                pdf_document.close()
                print(f"Decrypted: {input_path}")
            else:
                print(f"Invalid password for: {input_path}")
        else:
            print(f"Unencrypted: {input_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def decrypt_pdfs_in_folder(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):
                input_path = os.path.join(root, file_name)
                output_path = os.path.join(root, f'{os.path.splitext(file_name)[0]}_decrypted.pdf')

                decrypt_pdf(input_path, output_path, password)

def main():
    if len(os.sys.argv) != 3:
        print("Usage: python decrypt_pdfs.py <folder_path> <password>")
        os.sys.exit(1)

    folder_path = os.sys.argv[1]
    password = os.sys.argv[2]

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        os.sys.exit(1)

    decrypt_pdfs_in_folder(folder_path, password)
    print("PDF decryption completed.")

if __name__ == "__main__":
    main()
