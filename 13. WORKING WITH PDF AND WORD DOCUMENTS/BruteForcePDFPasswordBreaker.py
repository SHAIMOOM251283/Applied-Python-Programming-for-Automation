import PyPDF2

def try_passwords(pdf_file, wordlist):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for word in wordlist:
        word = word.strip()  # Remove any extra whitespace
        try:
            if pdf_reader.decrypt(word):
                print(f"Password found: {word}")
                return
        except PyPDF2.utils.PdfReadError:
            pass  # Incorrect password, continue to the next one
    print("Password not found in this wordlist.")

# Example usage:
file_path = 'encryptedbruteforceproject.pdf'  # Replace with your file path
with open('dictionary.txt', 'r') as file:
    wordlist = file.readlines()

try_passwords(file_path, wordlist)











