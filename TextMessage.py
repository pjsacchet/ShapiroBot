# Purpose of this script is to implement text message functionailty
# Import core libraries
import os
import logging

# Import Twilio library for sending messages
from twilio.rest import Client

class TextMessage:

    # Will by default initiate with my number as recipient and twilio number as sender (to be changed later to Adam's number)
    __init__():
        # Message content will be determined by Tweeter module, we can input all our other info now
        self.content = "Message here"
        self.sender = os.environ['TWILIO_NUMBER']
        self.recipient = os.environ['PATRICK_NUMBER']
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.sender = self.sender.strip()
        self.recipient = self.recipient.strip()
        self.account_sid = self.account_sid.strip()
        self.auth_token = self.auth_token.strip()

    # Send our message to our recipient
    def SendMessage():
        # Log these instead
        print ("Account SID is: " + account_sid)
        print ("Authentication token is: " + auth_token)

        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                 body=self.content,
                 from_=self.sender,
                 to=self.recipient
             )

        print(message.sid)
