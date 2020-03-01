#! /usr/bin/env python
import os
import sys
sys.path.insert(0, '..')
import Utilities
import unittest

class testUtilities(unittest.TestCase):
    def testGetURL(self):
        url = "http://www.baidu.com"
        htmlCont=Utilities.getURL(url)
        #print htmlCont
        #Baidu's webpage content should be bigger than 100 bytes
        self.assertGreater(len(htmlCont), 100)

        url = Utilities.IPReportWebList[0]
        htmlCont = Utilities.getURL(url)
        self.assertGreater(len(htmlCont), 100)
        #print htmlCont

        url = Utilities.IPReportWebList[1]
        htmlCont = Utilities.getURL(url)
        self.assertGreater(len(htmlCont), 100)
        #print htmlCont

    def testGetIP(self):
        #print(dir(Utilities))
        ipAddr=Utilities.getIPFromIP138()
        print "Your IP is:", ipAddr,type(ipAddr)

    def testGetIPFromDIG(self):
        ipAddr=Utilities.getIPFromDIG()
        print "Your IP is:", ipAddr, type(ipAddr)


    def ttestSendEmail(self):
        emailAddr = "youEmail"
        password  = "youPassword"
        mesgContent = "test Content"

        Utilities.sendEmail(emailAddr, password, mesgContent)

    def ttestSendEmail2(self):
        senderEmailAddr = "myEmil"
        receiverEmailAddr="youEmail"
        password  = "myEmailPassword"
        mesgContent = "test Content"

        senderEmailAddr = "myEmail"
        receiverEmailAddr="youEmail"

        Utilities.sendEmail2(senderEmailAddr, receiverEmailAddr, password, mesgContent)

    def ttestNotifyIP(self):
        emailAddr = "youEmail"
        password  = "youPassword"

        Utilities.notifyIP(emailAddr, password)
        Utilities.notifyIP(emailAddr, password)
        Utilities.notifyIP(emailAddr, password)
        Utilities.notifyIP(emailAddr, password)
        #you should only get one email, because you IP is not changed

    def testGetIFList(self):
        myList = Utilities.getIFList()
        print myList



if __name__ == '__main__':
	unittest.main()
