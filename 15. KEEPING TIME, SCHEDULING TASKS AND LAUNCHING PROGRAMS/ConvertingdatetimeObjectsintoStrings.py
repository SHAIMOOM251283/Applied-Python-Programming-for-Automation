#import datetime
#oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
#print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
#print(oct21st.strftime('%I:%M %p'))
#print(oct21st.strftime("%B of '%y"))

import datetime

# Create a datetime object for the current date and time
current_datetime = datetime.datetime.now()

# Format the datetime object as a string for display
formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted string
print(f"Formatted Date and Time: {formatted_string}")
