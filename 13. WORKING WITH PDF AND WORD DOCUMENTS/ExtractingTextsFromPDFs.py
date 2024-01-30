#import PyPDF2
#pdfFileObj = open('meetingminutes.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
#pageObj = pdfReader.getPage(0)
#print(pageObj.extractText())

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print(len(pdfReader.pages))
pageObj = pdfReader.pages[0]
print(pageObj.extract_text())
#pdfFileObj.close()

#import fitz  # PyMuPDF
#pdf_file_path = 'meetingminutes.pdf'
# Open the PDF file
#pdf_document = fitz.open(pdf_file_path)
# Get the number of pages in the PDF
#num_pages = pdf_document.page_count
#print(f"Number of pages: {num_pages}")
# Get the text from the first page (index 0)
#page = pdf_document.load_page(0)
#text = page.get_text("text")
#print(text)
# Close the PDF file
#pdf_document.close()
