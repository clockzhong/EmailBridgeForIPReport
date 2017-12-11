#! /usr/bin/env python

import urllib2


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
        return text
    return text

def getIPFromIP138():
    url = IPReportWebList[1]
    htmlCont= getURL(url)
    startChar = '['
    endChar   = ']'
    startIndex = htmlCont.index(startChar)+len(startChar)
    endIndex   = htmlCont.index(endChar)
    return htmlCont[startIndex:endIndex]
