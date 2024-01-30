import os
import PyPDF2

def copy_pages(input_pdf, output_pdf, page_numbers):
    input_pdf_path = os.path.join(os.path.dirname(__file__), input_pdf)
    output_pdf_path = os.path.join(os.path.dirname(__file__), output_pdf)

    with open(input_pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_number in page_numbers:
            if 1 <= page_number <= len(pdf_reader.pages):
                page = pdf_reader.pages[page_number - 1]
                pdf_writer.add_page(page)
            else:
                print(f"Skipping invalid page number {page_number}. The PDF has {len(pdf_reader.pages)} pages.")

        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

    print(f"Pages {', '.join(map(str, page_numbers))} copied to {output_pdf}")

if __name__ == "__main__":
    input_pdf_name = input("Enter the name of the input PDF file: ")
    output_pdf_name = input("Enter the name of the output PDF file: ")

    page_numbers_str = input("Enter the page numbers to copy (comma-separated): ")
    page_numbers = [int(num.strip()) for num in page_numbers_str.split(',')]

    copy_pages(input_pdf_name, output_pdf_name, page_numbers)