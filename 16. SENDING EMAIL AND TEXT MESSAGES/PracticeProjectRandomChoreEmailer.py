#import smtplib
#import random
#from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart
#def send_email(to_email, subject, body):
    # Replace with your email credentials and SMTP server details
#    smtp_server = "smtp.gmail.com"
#    smtp_port = 587
#    smtp_username = "my_email_address@gmail.com"
#    smtp_password = "APP Password"
    # Create the email message
#    message = MIMEMultipart()
#    message['From'] = smtp_username
#    message['To'] = to_email
#    message['Subject'] = subject
#    message.attach(MIMEText(body, 'plain'))
    # Connect to the SMTP server and send the email
#    with smtplib.SMTP(smtp_server, smtp_port) as server:
#        server.starttls()
#        server.login(smtp_username, smtp_password)
#        server.sendmail(smtp_username, to_email, message.as_string())
#def assign_chores(emails, chores):
    # Shuffle the chores randomly
#    random.shuffle(chores)
    # Assign each chore to a person and send email
#    for i, email in enumerate(emails):
#        chore_assigned = chores[i % len(chores)]
#        subject = "Chore Assignment"
#        body = f"Dear {email},\n\nYou have been assigned the chore: {chore_assigned}.\n\nBest regards,\nThe Chore Assignment Bot"
#        send_email(email, subject, body)
#if __name__ == "__main__":
    # Replace with your list of email addresses and chores
#    email_list = ["person1@example.com", "person2@example.com", "person3@example.com"]
#    chore_list = ["Dishwashing", "Vacuuming", "Laundry", "Grocery shopping"]
#    assign_chores(email_list, chore_list)

import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    # Replace with your email credentials and SMTP server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "my_email_address@gmail.com"
    smtp_password = "APP Password"

    # Create the email message
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, message.as_string())

def assign_chores(emails, chores):
    # Shuffle the chores randomly
    random.shuffle(chores)

    # Assign each chore to a person and send email
    for i, email in enumerate(emails):
        chore_assigned = chores[i % len(chores)]
        subject = "Chore Assignment"
        body = f"Dear {email},\n\nYou have been assigned the chore: {chore_assigned}.\n\nBest regards,\nThe Chore Assignment Bot"
        send_email(email, subject, body)
        print(f"Chore assignment email sent to {email}")

if __name__ == "__main__":
    # Replace with your list of email addresses and chores
    email_list = ["person1@example.com", "person2@example.com", "person3@example.com"]
    chore_list = ["Dishwashing", "Vacuuming", "Laundry", "Grocery shopping"]

    try:
        assign_chores(email_list, chore_list)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script execution completed. Closing SMTP connection.")


