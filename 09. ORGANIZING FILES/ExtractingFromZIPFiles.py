import zipfile, os
os.chdir('E:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
#exampleZip.extractall()
#exampleZip.extractall('E:\donkey')
#exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'E:\LEARNING PYTHON\AUTOMATE THE BORING STUFF\9. ORGANIZING FILES')
exampleZip.close()

