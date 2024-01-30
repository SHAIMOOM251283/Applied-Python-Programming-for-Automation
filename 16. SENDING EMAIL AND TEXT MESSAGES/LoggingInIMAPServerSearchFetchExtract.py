#import imapclient
#imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login('email_address@gmail.com', 'APP Password')
#imapObj.select_folder('INBOX', readonly=True)
#UIDs = imapObj.search(['SINCE 05-Jan-2024'])
#UIDs
#rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
#import pyzmail
#message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
#message.get_subject()
#message.get_addresses('from')
#message.get_addresses('to')
#message.get_addresses('cc')
#message.get_addresses('bcc')
#message.text_part != None
#message.text_part.get_payload().decode(message.text_part.charset)
#message.html_part != None
#message.html_part.get_payload().decode(message.html_part.charset)
#imapObj.logout()

#import imaplib
#import email
#from datetime import datetime
# Connect to the IMAP server
#mail = imaplib.IMAP4_SSL('imap.gmail.com')
#mail.login('email_address@gmail.com', 'APP Password')
# Select the INBOX folder
#mail.select('inbox')
# Define the date since which you want to search
#since_date = datetime(2024, 1, 15).strftime("%d-%b-%Y")
#result, data = mail.search(None, '(SINCE {date})'.format(date=since_date))
#if result == 'OK':
#    for num in data[0].split():
#        result, msg_data = mail.fetch(num, '(RFC822)')
#        if result == 'OK':
#            raw_message = msg_data[0][1]
#            message = email.message_from_bytes(raw_message)
#
#            print("Subject:", message["Subject"])
#            print("From:", message.get("From", ""))
#            print("To:", message.get("To", ""))
#            print("CC:", message.get("CC", ""))
#            print("BCC:", message.get("BCC", ""))
# Logout from the IMAP server
#mail.logout()

import imaplib
import email
from datetime import datetime

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('email_address@gmail.com', 'APP Password')

# Select the INBOX folder
mail.select('inbox')

# Define the date since which you want to search
since_date = datetime(2024, 1, 15).strftime("%d-%b-%Y")
result, data = mail.search(None, '(SINCE {date})'.format(date=since_date))

if result == 'OK':
    for num in data[0].split():
        result, msg_data = mail.fetch(num, '(RFC822)')
        if result == 'OK':
            raw_message = msg_data[0][1]
            message = email.message_from_bytes(raw_message)

            print("Subject:", message["Subject"])
            print("From:", message.get("From", ""))
            print("To:", message.get("To", ""))
            print("CC:", message.get("CC", ""))
            print("BCC:", message.get("BCC", ""))

            # Check for text/plain part
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    print("Text part:", part.get_payload(decode=True).decode(part.get_content_charset()))

            # Check for text/html part
            for part in message.walk():
                if part.get_content_type() == "text/html":
                    print("HTML part:", part.get_payload(decode=True).decode(part.get_content_charset()))

# Logout from the IMAP server
mail.logout()

