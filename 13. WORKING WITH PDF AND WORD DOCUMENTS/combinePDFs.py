#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

import PyPDF2
import os
# Get all the PDF filenames.
pdfFiles = [filename for filename in os.listdir('.') if filename.endswith('.pdf')]
# Sort the PDF filenames in a case-insensitive manner.
pdfFiles.sort(key=lambda x: x.lower())
pdfWriter = PyPDF2.PdfWriter()
# Loop through all the PDF files.
for filename in pdfFiles:
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfReader(pdfFileObj)       
        # Check if the PDF is encrypted and provide the password if needed.
        if pdfReader.is_encrypted:
            password = input(f"Enter password for {filename}: ")
            pdfReader.decrypt(password)
        # Loop through all the pages (including the first) and add them.
        #for pageNum in range(len(pdfReader.pages)):
        #    pageObj = pdfReader.pages[pageNum]
        #    pdfWriter.add_page(pageObj)
        # Loop through all the pages (except the first) and add them.
        for pageNum in range(1, len(pdfReader.pages)):
            pageObj = pdfReader.pages[pageNum]
            pdfWriter.add_page(pageObj)
# Save the resulting PDF to a file.
with open('allminutes.pdf', 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)




