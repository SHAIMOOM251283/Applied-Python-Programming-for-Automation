#import PyPDF2
#pdfFile = open('meetingminutes.pdf', 'rb')
#pdfReader = PyPDF2.PdfReader(pdfFile)
#pdfWriter = PyPDF2.PdfWriter()
#for pageNum in range(1, len(pdfReader.pages)):
#    pdfWriter.addPage(pdfReader.getPage(pageNum))
#pdfWriter.encrypt('swordfish')
#resultPdf = open('encryptedminutes.pdf', 'wb')
#pdfWriter.write(resultPdf)
#resultPdf.close()

import PyPDF2

pdfFile = open('bruteforceproject.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFile)
pdfWriter = PyPDF2.PdfWriter()

# Use len(pdfReader.pages) instead of numPages
for pageNum in range(1, len(pdfReader.pages)):
    # Use pdfReader.pages[page_number] instead of getPage(page_number)
    pdfWriter.add_page(pdfReader.pages[pageNum])

pdfWriter.encrypt('ABANDON')
resultPdf = open('encryptedbruteforceproject.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
pdfFile.close()



