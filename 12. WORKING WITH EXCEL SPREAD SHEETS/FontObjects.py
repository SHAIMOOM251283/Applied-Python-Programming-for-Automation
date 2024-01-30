import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.active

fontObj1 = Font(name='Times New Roman', bold=True)
styleObj1 = NamedStyle(name="styleObj1", font=fontObj1)
sheet['A1'].style = styleObj1  # Assign the style to the cell
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
styleObj2 = NamedStyle(name="styleObj2", font=fontObj2)
sheet['B3'].style = styleObj2  # Assign the style to the cell
sheet['B3'] = '24 pt Italic'

wb.save('styles.xlsx')
