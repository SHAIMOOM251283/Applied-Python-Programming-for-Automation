import os
import PyPDF2

def copy_pages(input_pdf, output_pdf, start_page, end_page):
    input_pdf_path = os.path.join(os.path.dirname(__file__), input_pdf)
    output_pdf_path = os.path.join(os.path.dirname(__file__), output_pdf)

    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(start_page - 1, min(end_page, len(pdf_reader.pages))):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_name = input("Enter the name of the input PDF file: ")
    output_pdf_name = input("Enter the name of the output PDF file: ")
    start_page_num = int(input("Enter the start page number: "))
    end_page_num = int(input("Enter the end page number: "))

    copy_pages(input_pdf_name, output_pdf_name, start_page_num, end_page_num)
    print(f"Pages {start_page_num} to {end_page_num} copied to {output_pdf_name}")


