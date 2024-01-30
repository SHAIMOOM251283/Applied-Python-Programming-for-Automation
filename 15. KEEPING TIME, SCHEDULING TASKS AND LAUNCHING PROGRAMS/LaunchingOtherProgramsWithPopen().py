import subprocess
#subprocess.Popen('C:\\Windows\\System32\\calc.exe')

calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
print(calcProc.poll() == None)
print(calcProc.wait()) 
print(calcProc.poll())

#calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
# Wait for the Calculator process to complete
#return_code = calcProc.wait()
# The return_code variable now holds the exit code of the Calculator process
#print(f"Calculator process completed with exit code: {return_code}")

#calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
# Wait for the Calculator process to complete
#calcProc.wait()
# The script will continue only after the Calculator process has finished
#print("Calculator process has completed.")



