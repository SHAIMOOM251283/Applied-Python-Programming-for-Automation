#import PyPDF2
#pdf1File = open('meetingminutes.pdf', 'rb')
#pdf2File = open('meetingminutes2.pdf', 'rb')
#pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
#pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
#pdfWriter = PyPDF2.PdfFileWriter()
#for pageNum in range(pdf1Reader.numPages):
#    pageObj = pdf1Reader.getPage(pageNum)
#    pdfWriter.addPage(pageObj)
#for pageNum in range(pdf2Reader.numPages):
#    pageObj = pdf2Reader.getPage(pageNum)
#    pdfWriter.addPage(pageObj)
#pdfOutputFile = open('combinedminutes.pdf', 'wb')
#pdfWriter.write(pdfOutputFile)
#pdfOutputFile.close()
#pdf1File.close()
#pdf2File.close()

import fitz  # PyMuPDF
def merge_pdfs(pdf_list, output_filename):
    pdf_writer = fitz.open()

    for pdf_file in pdf_list:
        pdf_reader = fitz.open(pdf_file)
        pdf_writer.insert_pdf(pdf_reader)

    pdf_writer.save(output_filename)
    pdf_writer.close()

if __name__ == "__main__":
    pdf_files = ['meetingminutes.pdf', 'meetingminutes2.pdf']
    output_file = 'combinedminutes.pdf'

    merge_pdfs(pdf_files, output_file)
