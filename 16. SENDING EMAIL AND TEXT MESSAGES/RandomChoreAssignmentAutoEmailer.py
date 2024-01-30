import smtplib
import random
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace with your email credentials and SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "my_email_address@gmail.com"
smtp_password = "APP Password"

# Dictionary to keep track of each person's previously assigned chores
previous_assignments = {}

def send_email(to_email, subject, body):
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

    # Assign each person a chore, avoiding the previously assigned one
    for email in emails:
        available_chores = [chore for chore in chores if chore != previous_assignments.get(email)]
        if not available_chores:
            # If all chores are assigned, reset the previous assignment
            previous_assignments[email] = None
        else:
            chore_assigned = random.choice(available_chores)
            previous_assignments[email] = chore_assigned

            subject = "Chore Assignment"
            body = f"Dear {email},\n\nYou have been assigned the chore: {chore_assigned}.\n\nBest regards,\nThe Chore Assignment Bot"
            send_email(email, subject, body)
            print(f"Chore assignment email sent to {email}")

def job():
    # Replace with your list of email addresses and chores
    email_list = ["person1@example.com", "person2@example.com", "person3@example.com"]
    chore_list = ["Dishwashing", "Vacuuming", "Laundry", "Grocery shopping"]

    assign_chores(email_list, chore_list)

# Schedule the job to run every 30 seconds
schedule.every(30).seconds.do(job)

# Schedule the job to run every hour
#schedule.every().hour.do(job)

# Schedule the job to run every day at a specific time (e.g., 2:30 PM)
#schedule.every().day.at("14:30").do(job)

# Schedule the job to run every month on the 15th at 5:00 AM
#schedule.every().month.day.at("05:00").do(job)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
