#phoneRegex = re.compile(r'''(
#                        (\d{3}|\(\d{3}\))? # area code
#                        (\s|-|\.)? # separator
#                        \d{3} # first 3 digits
#                        (\s|-|\.) # separator
#                        \d{4} # last 4 digits
#                        (\s*(ext|x|ext.)\s*\d{2,5})? # extension
#                        )''', re.VERBOSE)

import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?        # area code
    (\s|-|\.)?                # separator
    \d{3}                      # first 3 digits
    (\s|-|\.)                 # separator
    \d{4}                      # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

text = """
My phone numbers are:
123-456-7890
(123) 456-7890
(123)-456-7890
123.456.7890
1234567890
123-456-7890 ext. 12345
123-456-7890 ext. 123
"""

matches = phoneRegex.findall(text)

for match in matches:
    print(match[0].strip())  # Output the full matched phone number
