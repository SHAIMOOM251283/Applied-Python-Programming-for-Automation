#import PyPDF2
#minutesFile = open('meetingminutes.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(minutesFile)
#page = pdfReader.getPage(0)
#page.rotateClockwise(90)
#pdfWriter = PyPDF2.PdfFileWriter()
#pdfWriter.addPage(page)
#resultPdfFile = open('rotatedPage.pdf', 'wb')
#pdfWriter.write(resultPdfFile)
#resultPdfFile.close()
#minutesFile.close()

import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
page = pdfReader.pages[0]

# Use rotate instead of rotateClockwise
print(page.rotate(90))

pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(page)

resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
minutesFile.close()

