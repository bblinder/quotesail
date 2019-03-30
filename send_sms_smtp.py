#!/usr/bin/env python

import random
import smtplib
import time
from datetime import datetime, timedelta, date
import logging
#from time import gmtime, strftime, localtime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('quotesail.log')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.info("[{}] - quotesail was run".format(datetime.now()))

# Credentials (if needed)
# A new gmail account is recommended for this
username = '[your username]'
password = '******'
fromaddr = '[your username]@gmail.com'
toaddrs  = 'yournumber@yoursmsgateway'

# Picking a random line from 'quotes.txt', assuming it exists
def random_quote():
    random_quote = (random.choice(list(open('quotes.txt'))))
    return random_quote

message = 'Subject: A little something \n\n%' % random_quote()

# The actual mail send
if __name__ == '__main__':
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
