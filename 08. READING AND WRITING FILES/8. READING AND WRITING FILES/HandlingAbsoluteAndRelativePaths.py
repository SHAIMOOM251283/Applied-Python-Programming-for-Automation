import os
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
print(os.getcwd())

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))
print((os.path.dirname(calcFilePath), os.path.basename(calcFilePath)))
print(calcFilePath.split(os.path.sep))