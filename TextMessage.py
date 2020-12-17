# Purpose of this script is to create and send text messages to my groupmembers
# Import core libraries
import os
import logging

# Import Twilio library for sending messages
from twilio.rest import Client




# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Exporting environment variables messes with our strings so let's clean them otherwise bad things happen
account_sid = account_sid.strip()
auth_token = auth_token.strip()

# Log these instead
print ("Account SID is: " + account_sid)
print ("Authentication token is: " + auth_token)

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Message here',
         from_='+18437907042',
         to='+12405201974'
     )

print(message.sid)
