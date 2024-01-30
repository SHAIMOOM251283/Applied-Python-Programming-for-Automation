#import datetime
#print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
#print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
#print(datetime.datetime.strptime("October of '15", "%B of '%y"))
#print(datetime.datetime.strptime("November of '63", "%B of '%y"))

import datetime

# String representing a date
date_string = "2024-01-10"

# Convert the string to a datetime object
date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")

# Perform date manipulation
new_date = date_object + datetime.timedelta(days=7)

# Print the results
print(f"Original Date: {date_object}")
print(f"New Date: {new_date}")
