#! /usr/bin/env python3

import urllib.request, urllib.error, urllib.parse
from email.mime.text import MIMEText
import smtplib
import time
import socket
import fcntl
import struct
import array
import os

#########################################################################################################
#The following code section is from https://gist.github.com/pklaus/289646  with my partial modification
#########################################################################################################
def all_interfaces():
    max_possible = 128  # arbitrary. raise if needed.
    bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', [0] * bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', bytes, names.buffer_info()[0])
    ))[0]
    s.close()
    namestr = names.tostring()
    namestr = str(namestr)
    #print(type(namestr))
    lst = []
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split('\0', 1)[0]
        ip   = namestr[i+20:i+24]
        lst.append((name, ip))
    return lst

def format_ip(addr):
    return str(ord(addr[0])) + '.' + \
           str(ord(addr[1])) + '.' + \
           str(ord(addr[2])) + '.' + \
           str(ord(addr[3]))

def getIFList():
    ifs = all_interfaces()
    myStrng = ""
    for i in ifs:
        myStrng+="%s  : %s\n" % (i[0], format_ip(i[1]))
    return myStrng

#########################################################################################################
#The code section from https://gist.github.com/pklaus/289646  ends here
#########################################################################################################



EmailAddr="YouEmailAddress"
SMTPPassword="YouPasswordForYourEmailAccount"

SMTPServer_163_com = "smtp.163.com"
SMTPPort_163_com   =  25
SMTPServer_outlook_com="smtp.office365.com"
SMTPPort_outlook_com=587

CurrentIP = ''
CurrentLocalIPs = ''

HTTP_TIMEOUT=38

AgentList=['Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"]

#it seems 'http://www.iplocation.net/' couldn't work
IPReportWebList=['http://www.infosniper.net/', 'http://2020.ip138.com/','http://www.iplocation.net/']


def getURL(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', AgentList[1])]
    text = ""
    try:
        openerConnection = opener.open(url, timeout=HTTP_TIMEOUT)
        text = openerConnection.read()
    except Exception as e:
        print(e)
        return ""
    return text

def getIPFromIP138():
    url = IPReportWebList[1]
    htmlCont = ""
    while True:
        while True:
            try :
                htmlCont= getURL(url)
                if htmlCont != "":
                    #print "got IP:", htmlCont
                    break
            except Exception as e:
                print("try again because getting errors:", e)
        startChar = '['
        endChar   = ']'
        startIndex = htmlCont.index(startChar)+len(startChar)
        endIndex   = htmlCont.index(endChar)
        ipStr= htmlCont[startIndex:endIndex]
        #if len(ipStr) is 0, done't return, try the above code again
        if len(ipStr)!=0:
            return ipStr
        else:
            print("try again because geting wrong IP", ipStr)

def getIPFromDIG():
    """Use "dig +short myip.opendns.com @resolver1.opendns.com" to get the public address """
    lines = os.popen('dig +short myip.opendns.com @resolver1.opendns.com').readlines(-1)
    #print lines
    #print len(lines)
    if len(lines)!=0:
        ipStr = lines[0].strip()
    else:
        ipStr = "10.0.0.1"
    #print ipStr
    return ipStr


smtpDict={
    "163.com": (SMTPServer_163_com, SMTPPort_163_com),
    "outlook.com": (SMTPServer_outlook_com, SMTPPort_outlook_com)
}

def getSMTPInfo(domainName):
    if domainName in smtpDict:
        return smtpDict[domainName]
    else:
        print("Something wrong in your email domain, we use 163.com SMTP server")
        return smtpDict["163.com"]

def sendEmail(emailAddr, password, mesgContent, extraComment=""):
    partsArr=emailAddr.split("@")
    #print(partsArr)
    account = partsArr[0]
    domainName=partsArr[1]
    smtpServer, smtpPort = getSMTPInfo(domainName)
    #print smtpServer, smtpPort
    #return
    you = emailAddr
    me = emailAddr
    msg = MIMEText(mesgContent)
    msg['Subject'] = "Your IP Address"+" "+ extraComment
    msg['From'] = me
    msg['To'] = you
    print("connect the smtpServer!")

    s = smtplib.SMTP(smtpServer, smtpPort, timeout=15)
    if smtpServer==SMTPServer_outlook_com:
        s.starttls()
    print((me, password))
    s.login(me, password)
    print("sending email!")
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def sendEmail2(senderEmailAddr, receiverEmailAddr, password, mesgContent, extraComment=""):
    partsArr=senderEmailAddr.split("@")
    #print(partsArr)
    account = partsArr[0]
    domainName=partsArr[1]
    smtpServer, smtpPort = getSMTPInfo(domainName)
    #print smtpServer, smtpPort
    #return
    you = receiverEmailAddr
    me = senderEmailAddr
    msg = MIMEText(mesgContent)
    msg['Subject'] = "Your IP Address"+" "+ extraComment
    msg['From'] = me
    msg['To'] = you
    print("connect the smtpServer!")

    s = smtplib.SMTP(smtpServer, smtpPort, timeout=15)
    if smtpServer==SMTPServer_outlook_com:
        s.starttls()
    print((me, password))
    s.login(me, password)
    print("sending email!")
    s.sendmail(me, [you], msg.as_string())
    s.quit()

def notifyIP(emailAddr, password, extraComment=""):
    global CurrentIP
    global CurrentLocalIPs
    #newIP = getIPFromIP138()
    newIP = getIPFromDIG()
    newLocalIPs = getIFList()
    print(newIP, CurrentIP, newLocalIPs, CurrentLocalIPs)
    if newIP != CurrentIP or newLocalIPs!=CurrentLocalIPs:
        messageContent = "extra IP:"+newIP+"\n"
        messageContent+= "local IPs:\n"+newLocalIPs
        print(newIP, "!!!!!!!!!!!!!!!!!!!!!!!!")
        if newIP!="10.0.0.1":
            while True:
                try:
                    sendEmail(emailAddr, password, messageContent, extraComment)
                    break
                except Exception as e:
                    print("try again because getting errors:", e)


        CurrentIP = newIP
        CurrentLocalIPs = newLocalIPs
    else:
        print("CurrentIP and CurrentLocalIPs not changed")

def notifyIP2(senderEmailAddr, receiverEmailAddr, password, extraComment=""):
    global CurrentIP
    global CurrentLocalIPs
    #newIP = getIPFromIP138()
    newIP = getIPFromDIG()
    newLocalIPs = getIFList()
    print(newIP, CurrentIP, newLocalIPs, CurrentLocalIPs)
    if newIP != CurrentIP or newLocalIPs!=CurrentLocalIPs:
        messageContent = "extra IP:"+newIP+"\n"
        messageContent+= "local IPs:\n"+newLocalIPs
        print(newIP, "!!!!!!!!!!!!!!!!!!!!!!!!")
        if newIP!="10.0.0.1":
            while True:
                try:
                    sendEmail2(senderEmailAddr, receiverEmailAddr, password, messageContent, extraComment)
                    break
                except Exception as e:
                    print("try again because getting errors:", e)


        CurrentIP = newIP
        CurrentLocalIPs = newLocalIPs
    else:
        print("CurrentIP and CurrentLocalIPs not changed")
