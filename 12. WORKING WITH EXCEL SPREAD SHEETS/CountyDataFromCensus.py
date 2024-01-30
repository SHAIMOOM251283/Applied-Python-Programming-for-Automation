#import os
#os.chdir()
#import census2010
#census2010.allData['AK']['Anchorage']
#anchoragePop = census2010.allData['AK']['Anchorage']['pop']
#print('The 2010 population of Anchorage was ' + str(anchoragePop))

import os
import sys

# Set the current working directory
os.chdir(r'E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\12. WORKING WITH EXCEL SPREAD SHEETS')

# Add the directory to the sys.path so that Python can find the module
sys.path.append(r'E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\12. WORKING WITH EXCEL SPREAD SHEETS')

# Now you can import census2010
import census2010

# Rest of your code remains the same
print(census2010.allData['AK']['Anchorage'])
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))
