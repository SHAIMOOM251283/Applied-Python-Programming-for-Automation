import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
   # Get address from command line.
   address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# Usage: 
# The script or the directory containing this script has to be added to the PATH.
# The code has to be used along wih the batch file mapIt.bat.
# Open terminal, type mapIt and the search location. 