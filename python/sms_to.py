#!/bin/bash
from utilities import sys_validation

'''
    Description:
    The purpose of this script is to send a sms message 
    to someone by changing configuration of initials parameters. 
'''

def main():
    FROM = 'xxx-xxx-xxxx'  # PHONE NUMBER WHERE THE MESSAGE WAS SENT
    TO = 'xxx-xxx-xxxx'  # PHONE NUMBER TO SEND MESSAGE
    MSG = 'SAMPLE MESSAGE'  # MESSAGE TO SEND

    if send_sms(FROM, TO, MSG):
        print('SUCCESS: The sms message was sent correctly!')
    else:
        print('ERROR: There was an issue trying to send the message!')


def send_sms(frm, to, msg):
    return True

if __name__ == "__main__":
    main()
