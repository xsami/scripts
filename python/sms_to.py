'''
    Description:
    The purpose of this script is to send a sms message 
    to someone.

    Notes:
    This app uses twilio api to perform message sending.
    For more documentation visit: https://www.twilio.com/docs/libraries/python
'''
#!/bin/bash

from utilities import sys_validation
from twilio.rest import Client

def main():
    FROM = '+xxxxxxxxxx'  # PHONE NUMBER WHERE THE MESSAGE WAS SENT
    TO = '+xxxxxxxxxx'  # PHONE NUMBER TO SEND MESSAGE
    MSG = 'SAMPLE MESSAGE'  # MESSAGE TO SEND
    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # ACCOUNT SID
    AUTH_TOKEN = 'your_auth_token' # AUTHENTICATION TOKEN

    send_sms(FROM, TO, MSG, ACCOUNT_SID, AUTH_TOKEN)

'''
    This method calls twilio api to send a sms message
'''
def send_sms(from_, to, msg, account_sid, auth_token):
    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
        to,
        from_,
        msg)

    return True

if __name__ == "__main__":
    main()
