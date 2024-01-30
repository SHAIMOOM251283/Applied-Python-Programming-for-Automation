#import openpyxl
#from openpyxl.chart import Reference, Series, BarChart
#wb = openpyxl.Workbook()
#sheet = wb.active  # Use the active attribute
#for i in range(1, 11):  # create some data in column A
#    sheet['A' + str(i)] = i
#refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
#seriesObj = Series(refObj, title='First series')
#chartObj = BarChart()
#chartObj.append(seriesObj)
# Set the position and size directly on chartObj
#chartObj.top = 50
#chartObj.left = 100
#chartObj.width = 300
#chartObj.height = 200
#sheet.add_chart(chartObj)
#wb.save('sampleChart.xlsx')

import openpyxl
from openpyxl.chart import Reference, Series, BarChart

wb = openpyxl.Workbook()
sheet = wb.active  # Use the active attribute

for i in range(1, 11):  # create some data in column A
    sheet['A' + str(i)] = i

refObj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
seriesObj = Series(refObj, title='First series')
chartObj = BarChart()
chartObj.append(seriesObj)

# Set the position and size in pixels
chartObj.top = 50 * 0.75  # 50 pixels converted to points
chartObj.left = 100 * 0.75  # 100 pixels converted to points
chartObj.width = 300 * 0.75  # 300 pixels converted to points
chartObj.height = 200 * 0.75  # 200 pixels converted to points

sheet.add_chart(chartObj)
wb.save('sampleChart.xlsx')
