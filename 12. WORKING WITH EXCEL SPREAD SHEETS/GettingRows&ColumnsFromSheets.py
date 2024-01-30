import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']  # Use wb['Sheet1'] directly instead of wb.get_sheet_by_name('Sheet1') due to deprecation
print(tuple(sheet['A1':'C3']))
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

#import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
column_2 = list(sheet.columns)[1]  # Convert generator to list and access the second column
print(column_2)
for cellObj in column_2:
    print(cellObj.value)

