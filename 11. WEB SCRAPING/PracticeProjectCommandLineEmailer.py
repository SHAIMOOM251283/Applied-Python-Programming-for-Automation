#import yagmail
#recipient_email = "email@example.com"  # Hardcoded recipient email
#email_body = "This is a test email."   # Hardcoded email body
#yag = yagmail.SMTP("you_email@gmail.com", "your_password")
#yag.send(recipient_email, "Email Subject", email_body)

#import yagmail
#import sys
#recipient_email = sys.argv[1]  # Get email address from command line
#email_body = sys.argv[2]      # Get email body from command line
#yag = yagmail.SMTP("your_email@gmail.com", "your_password")
#yag.send(recipient_email, "Email Subject", email_body)

#import yagmail
#import sys
#if len(sys.argv) < 3:
#    print("Usage: python script_name.py <recipient_email> <email_body>")
#    sys.exit(1)
#recipient_email = sys.argv[1]  # Get email address from command line
#email_body = sys.argv[2]      # Get email body from command line
# Your email sending code
#yag = yagmail.SMTP("your_email@gmail.com", "your_password")
#yag.send(recipient_email, "Email Subject", email_body)

