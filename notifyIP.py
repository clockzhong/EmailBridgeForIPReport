#! /usr/bin/env python

import urllib2
from email.mime.text import MIMEText
import smtplib
import time
import Utilities
import random


emailAddr = "YouEmailAddress"
password  = "YouPasswordForYourEmailAccount"

MinimumPauseTime = 50
MaximumPauseTime = 60*15

while True:
    print "check the IP"
    Utilities.notifyIP(emailAddr, password)
    pauseTime = random.randint(MinimumPauseTime, MaximumPauseTime)
    print "wait for ",pauseTime, " seconds"
    time.sleep(pauseTime)
