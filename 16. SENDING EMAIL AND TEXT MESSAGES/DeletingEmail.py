import imapclient
from datetime import datetime, timedelta
import pprint
import email
from email import message_from_bytes

# Connect to the IMAP server
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('email_address@gmail.com', 'App Password')

pprint.pprint(imapObj.list_folders())
imapObj.select_folder('INBOX', readonly=False)

# Use a specific date in the search criteria (e.g., '15-Jan-2024')
UIDs = imapObj.search(['ON', '15-Jan-2024'])
print(UIDs)

# Input the UID at runtime
uid_to_delete = input("Enter the UID of the email you want to delete: ")

try:
    # Delete the email with the specified UID
    imapObj.delete_messages([int(uid_to_delete)])

    # Permanently remove the deleted messages
    imapObj.expunge()

    print(f"Email with UID {uid_to_delete} successfully deleted.")
except Exception as e:
    print(f"Error deleting email: {e}")

# Logout from the IMAP server
imapObj.logout()
