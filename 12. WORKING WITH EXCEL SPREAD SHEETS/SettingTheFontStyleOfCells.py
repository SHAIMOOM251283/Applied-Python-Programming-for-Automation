import openpyxl
from openpyxl.styles import Font, NamedStyle

wb = openpyxl.Workbook()
sheet = wb.active  # using the active attribute to get the default sheet

italic24Font = Font(size=24, italic=True)
styleObj = NamedStyle(name="italic24Font", font=italic24Font)

sheet['A1'].style = styleObj  # Assign the style to the cell
sheet['A1'] = 'Hello world!'
wb.save('styled.xlsx')
