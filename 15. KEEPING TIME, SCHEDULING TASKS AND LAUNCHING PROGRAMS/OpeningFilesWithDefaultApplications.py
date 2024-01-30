fileObj = open('hello1.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)