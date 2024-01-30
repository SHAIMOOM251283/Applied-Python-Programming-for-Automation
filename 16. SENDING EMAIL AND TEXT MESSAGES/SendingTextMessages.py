#from twilio.rest import TwilioRestClient
#accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#twilioCli = TwilioRestClient(accountSID, authToken)
#myTwilioNumber = '+14955551234'
#myCellPhone = '+14955558888'
#message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)

from twilio.rest import Client

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

twilioCli = Client(accountSID, authToken)

myTwilioNumber = '+14955551234'
myCellPhone = '+14955558888'

message = twilioCli.messages.create(
    body='Mr. Watson - Come here - I want to see you.',
    from_=myTwilioNumber,
    to=myCellPhone
)

# Print relevant information
print("To:", message.to)
print("From:", message.from_)
print("Body:", message.body)
print("Status:", message.status)
print("Date Created:", message.date_created)
print("Date Sent:", message.date_sent)  # This might be None initially
print("SID:", message.sid)

# Retrieve and print updated information
print("\nUpdated Status:", message.status)
print("Updated Date Sent:", message.date_sent)