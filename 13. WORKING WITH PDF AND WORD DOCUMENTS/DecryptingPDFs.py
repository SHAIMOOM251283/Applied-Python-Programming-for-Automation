#import PyPDF2
#pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
#print(pdfReader.is_encrypted)
#pdfReader.getPage(0)
#pdfReader.decrypt('rosebud')
#pageObj = pdfReader.getPage(0)

import PyPDF2
# Open the encrypted PDF file
with open('encrypted.pdf', 'rb') as file:
    pdfReader = PyPDF2.PdfReader(file)
    # Check if the PDF is encrypted
    if pdfReader.is_encrypted:
        # Attempt to decrypt with the password 'rosebud'
        pdfReader.decrypt('rosebud')
    # Access the first page using the 'pages' attribute
    pageObj = pdfReader.pages[0]
    # Now you can use 'pageObj' as needed
    # For example, you can extract text from the page
    text = pageObj.extract_text()
    print(text)
