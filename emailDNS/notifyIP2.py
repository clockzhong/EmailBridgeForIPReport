#! /usr/bin/env python

import sys
import urllib.request, urllib.error, urllib.parse
from email.mime.text import MIMEText
import smtplib
import time
from . import Utilities
import random
import platform

if len(sys.argv)!=4 :
    print("notifyIP.py YouEmailAddress YouPasswordForYourEmailAccount receiverEmailAddr")
    sys.exit(1)

myEmailAddr = sys.argv[1]
password = sys.argv[2]
otherEmailAddr = sys.argv[3]

print((myEmailAddr, password, otherEmailAddr))

MinimumPauseTime = 50
MaximumPauseTime = 60*15

MinimumPauseTime = 50/25
MaximumPauseTime = 60*15/60

hostName = platform.node()
msg = " from "+hostName
print(msg)
#quit()

while True:
    print("check the IP")
    Utilities.notifyIP2(myEmailAddr, otherEmailAddr, password, msg)
    pauseTime = random.randint(MinimumPauseTime, MaximumPauseTime)
    print("wait for ",pauseTime, " seconds")
    time.sleep(pauseTime)
