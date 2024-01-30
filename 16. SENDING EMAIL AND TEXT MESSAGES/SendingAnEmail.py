import smtplib

# Set up the connection to the SMTP server
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Start the TLS (Transport Layer Security) connection
smtpObj.starttls()

# Greet the server with EHLO
smtpObj.ehlo()

# Log in to your Gmail account
smtpObj.login('my_email_address@gmail.com', 'APP Password')

# Prepare the email content
sender_email = 'my_email_address@gmail.com'
receiver_email = 'recipient_email_address@gmail.com'
subject = 'Subject: So long.'
body = 'Dear Alice, so long and thanks for all the fish. Sincerely, Bob'
message = f'{subject}\n\n{body}'

# Send the email
sendmail_response = smtpObj.sendmail(sender_email, receiver_email, message)

# Print or use the response as needed
print(sendmail_response)

# Close the connection
#smtpObj.quit()

# Close the connection and print the result
close_response = smtpObj.quit()
print(close_response)

