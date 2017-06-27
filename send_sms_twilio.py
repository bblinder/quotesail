#!/usr/bin/env python

import random
import sys
try:
    from twilio.rest import Client
except ImportError:
    print "Can't import Twilio -- check that it's installed"
    print "Example: 'pip -u install twilio'"
    sys.exit(1)

# assumes you have a 'quotes.txt' file living in your directory
def random_quote():
    random_quote = (random.choice(list(open('quotes.txt'))))
    return random_quote

result = random_quote() 

# these are found in the Twilio dashboard
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

client.messages.create(to="",
        from_="",
        body=result)

