#import imapclient
#imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login('email_address@gmail.com', 'nsmsosqnzbwmqahl')

import imapclient
from datetime import datetime, timedelta
import pprint
import email
from email import message_from_bytes

# Accept username and password from user input
#username = input("Enter your Gmail username: ")
#password = input("Enter your Gmail APP Password: ")

# Connect to the IMAP server
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#imapObj.login(username, password)
imapObj.login('email_address@gmail.com', 'APP Password')

pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=True)

# Format the date using datetime module
since_date = (datetime.now() - timedelta(days=365)).strftime('15-Jan-2024')

# Use the dynamically generated date in the search criteria
UIDs = imapObj.search(['SINCE', since_date])
print(UIDs)

# Search for all emails in the 'INBOX'
#UIDs = imapObj.search(['ALL'])
#print("UIDs of all emails in INBOX:", UIDs)

# Search for emails with a specific subject (e.g., 'meaning of life')
#subject_to_search = 'enter_search_word/s'
#UIDs = imapObj.search(['SUBJECT', subject_to_search])
#print("UIDs of emails with the subject", subject_to_search, ":", UIDs)

# Fetch and print the body of each email
#rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

#for uid, message_data in rawMessages.items():
#    print(f"UID: {uid}")
#    pprint.pprint(message_data[b'BODY[]'])

# Fetch the raw email message with UID
rawMessage = imapObj.fetch([9343], ['BODY[]'])[9343][b'BODY[]']

# Use email library to parse the raw message
email_message = message_from_bytes(rawMessage)

# Get the sender's email address
sender_address = email_message.get('From')
print("Sender's Email Address:", sender_address)

# Get the sender's email address
#sender_address = email.utils.parseaddr(email_message.get('From'))[1]
#print("Sender's Email Address:", sender_address)

# Get the subject using get() method
subject = email_message.get('Subject')
print("Subject:", subject)

# Get the recipients' email addresses
to_addresses = [email.utils.parseaddr(addr)[1] for addr in email.utils.getaddresses(email_message.get_all('To', []))]
cc_addresses = [email.utils.parseaddr(addr)[1] for addr in email.utils.getaddresses(email_message.get_all('Cc', []))]
bcc_addresses = [email.utils.parseaddr(addr)[1] for addr in email.utils.getaddresses(email_message.get_all('Bcc', []))]

print("To:", to_addresses)
print("CC:", cc_addresses)
print("BCC:", bcc_addresses)

# Check for text and HTML parts
if email_message.is_multipart():
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain' and part.get('Content-Disposition') is None:
            text_part = part
        elif part.get_content_type() == 'text/html' and part.get('Content-Disposition') is None:
            html_part = part

# Print decoded text part if available
if 'text_part' in locals():
    print("Text Part:")
    print(text_part.get_payload(decode=True).decode(text_part.get_content_charset()))

# Print decoded HTML part if available
if 'html_part' in locals():
    print("HTML Part:")
    print(html_part.get_payload(decode=True).decode(html_part.get_content_charset()))

# Logout from the IMAP server
imapObj.logout()





