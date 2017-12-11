#! /usr/bin/env python

import urllib2
from email.mime.text import MIMEText
import smtplib
import time

EmailAddr="YouEmailAddress"
SMTPPassword="YouPasswordForYourEmailAccount"

SMTPServer = "smtp.163.com"
SMTPPort   =  25

CurrentIP = ''

HTTP_TIMEOUT=38

AgentList=['Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"]

#it seems 'http://www.iplocation.net/' couldn't work
IPReportWebList=['http://www.infosniper.net/', 'http://2017.ip138.com/ic.asp','http://www.iplocation.net/']


def getURL(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', AgentList[1])]
    text = ""
    try:
        openerConnection = opener.open(url, timeout=HTTP_TIMEOUT)
        text = openerConnection.read()
    except Exception as e:
        print e
        return ""
    return text

def getIPFromIP138():
    url = IPReportWebList[1]
    htmlCont= getURL(url)
    while htmlCont == "":
        time.sleep(3)
        print "failed to get IP, try again"
        htmlCont = getURL(url)
    startChar = '['
    endChar   = ']'
    startIndex = htmlCont.index(startChar)+len(startChar)
    endIndex   = htmlCont.index(endChar)
    return htmlCont[startIndex:endIndex]


def sendEmail(emailAddr, password, mesgContent, smtpServer=SMTPServer, smtpPort=SMTPPort):
    you = emailAddr
    me = emailAddr
    msg = MIMEText(mesgContent)
    msg['Subject'] = "Your IP Address"
    msg['From'] = me
    msg['To'] = you
    s = smtplib.SMTP(smtpServer, smtpPort)
    s.login(me, password)
    s.sendmail(me, [you], msg.as_string())

def notifyIP(emailAddr, password, smtpServer=SMTPServer, smtpPort=SMTPPort):
    global CurrentIP
    newIP = getIPFromIP138()
    if newIP != CurrentIP:
        sendEmail(emailAddr, password, newIP, , smtpServer, smtpPort)
        CurrentIP = newIP
    else:
        print "CurrentIP is not changed"
