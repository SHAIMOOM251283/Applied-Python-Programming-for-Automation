import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(minutesFile)
#minutesFirstPage = pdfReader.getPage(0)
#pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
#minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
#pdfWriter = PyPDF2.PdfFileWriter()
#pdfWriter.addPage(minutesFirstPage)
#for pageNum in range(1, pdfReader.numPages):
#    pageObj = pdfReader.getPage(pageNum)
#    pdfWriter.addPage(pageObj)
#resultPdfFile = open('watermarkedCover.pdf', 'wb')
#pdfWriter.write(resultPdfFile)
#minutesFile.close()
#resultPdfFile.close()

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(minutesFile)
minutesFirstPage = pdfReader.pages[0]
pdfWatermarkReader = PyPDF2.PdfReader(open('watermark.pdf', 'rb'))
minutesFirstPage.merge_page(pdfWatermarkReader.pages[0])
pdfWriter = PyPDF2.PdfWriter()
pdfWriter.add_page(minutesFirstPage)
# Use len(reader.pages) instead of numPages
for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
