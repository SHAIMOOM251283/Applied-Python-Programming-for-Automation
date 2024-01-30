import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active  # Use the active attribute

sheet.freeze_panes = 'A2'

wb.save('freezeExample.xlsx')
