#! /usr/bin/env python

import sys
import urllib2
from email.mime.text import MIMEText
import smtplib
import time
import Utilities
import random

if len(sys.argv)!=3 and len(sys.argv)!=5:
    print "notifyIP.py YouEmailAddress YouPasswordForYourEmailAccount"
    print "or "
    print "notifyIP.py YouEmailAddress YouPasswordForYourEmailAccount YouSMTPServer YouSMTPPort"
    sys.exit(1)
elif len(sys.argv)==3:
    smtpServer=Utilities.SMTPServer
    smtpPort=Utilities.SMTPPort
elif len(sys.argv)==5:
    smtpServer=sys.argv[3]
    smtpPort=int(sys.argv[4])

emailAddr = sys.argv[1]
password = sys.argv[2]

print (emailAddr, password, smtpServer, smtpPort)

MinimumPauseTime = 50
MaximumPauseTime = 60*15

while True:
    print "check the IP"
    Utilities.notifyIP(emailAddr, password, smtpServer, smtpPort)
    pauseTime = random.randint(MinimumPauseTime, MaximumPauseTime)
    print "wait for ",pauseTime, " seconds"
    time.sleep(pauseTime)
