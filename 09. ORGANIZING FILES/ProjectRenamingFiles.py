#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format 
# to European DD-MM-YYYY.

import shutil, os, re

datePattern = re.compile(r"""^(.*?)    # all text before the date
                             (\d{1,2})-  # one or two digits for the month
                             (\d{1,2})-    # one or two digits for the day
                             (\d{4})      # four digits for the year
                             (.*)$      # all text after the date
                         """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename) # uncomment after testing




    

