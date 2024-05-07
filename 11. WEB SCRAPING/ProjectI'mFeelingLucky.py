import webbrowser
import sys
from googlesearch import search
import time
print('Googling...')  # display text while searching Google
query = ' '.join(sys.argv[1:])
for j in search(query, num_results=5):
    webbrowser.open(j)
    time.sleep(2)  # Adding a delay of 2 seconds between opening each result

# Usage: 
# The script or the directory containing this script has to be added to the PATH.
# The code has to be used along wih the batch file lucky.bat.
# Example: rename the script lucky.py
# Open terminal, type lucky and the search word.  