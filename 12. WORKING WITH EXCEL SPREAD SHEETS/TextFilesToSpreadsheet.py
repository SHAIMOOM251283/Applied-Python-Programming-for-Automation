import openpyxl

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# List of text file names
text_files = ['text_file_1.txt', 'text_file_2.txt', 'text_file_3.txt']

# Loop through text files and insert content into corresponding columns
for col_index, text_file in enumerate(text_files, start=1):
    with open(text_file, 'r') as file:
        lines = file.readlines()

        # Insert each line into the corresponding column
        for row_index, line in enumerate(lines, start=1):
            sheet.cell(row=row_index, column=col_index, value=line.strip())

# Save the workbook
workbook.save('output_spreadsheet.xlsx')
