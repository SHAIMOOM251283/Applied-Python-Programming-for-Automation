#import smtplib
# Set up the connection to the SMTP server
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# Start the TLS (Transport Layer Security) connection
#smtpObj.starttls()
# Greet the server with EHLO
#smtpObj.ehlo()
# Log in to your Gmail account
#smtpObj.login('emailaddress@gmail.com', 'AppPassword')

import smtplib

# Set up the connection to the SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Start the TLS (Transport Layer Security) connection
smtpObj.starttls()

# Greet the server with EHLO
smtpObj.ehlo()

# Log in to your Gmail account and capture the response
login_response = smtpObj.login('email_address@gmail.com', 'APP Password')

# Print or use the response as needed
print(login_response)

# Close the connection
#smtpObj.quit()

# Close the connection and print the result
close_response = smtpObj.quit()
print(close_response)

