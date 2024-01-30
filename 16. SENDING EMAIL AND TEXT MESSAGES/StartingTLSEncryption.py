import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

# Send the EHLO command and print the response
response = smtpObj.ehlo()
print(response)
