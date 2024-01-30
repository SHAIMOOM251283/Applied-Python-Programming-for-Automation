#! python3
# textMyself.py - Defines the textmyself() function that texts a message 
# passed to it as a string.

# Preset values:
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+14955558888'
twilioNumber = '+14955551234'

from twilio.rest import Client

#def textmyself(message):
#    twilioCli = Client(accountSID, authToken)
#    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    
    try:
        twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
        print("Message successfully sent!")
    except Exception as e:
        print(f"Error sending message: {e}")