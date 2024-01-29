import shutil, os
os.chdir('E:\\')
shutil.copy('E:\\spam.txt', 'E:\\delicious')
shutil.copy('eggs.txt', 'E:\\delicious\\eggs2.txt')

#shutil.copy('E:\\eggs.txt', 'E:\\delicious')
#shutil.copy('E:\\eggs.txt', 'E:\\delicious\\eggs2.txt')
