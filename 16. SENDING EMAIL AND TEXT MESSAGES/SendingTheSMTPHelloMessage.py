import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()  # Establish a secure connection
response = smtpObj.ehlo()  # Send the EHLO command

print(response)

