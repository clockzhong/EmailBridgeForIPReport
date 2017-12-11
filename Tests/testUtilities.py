#! /usr/bin/env python
import os
import sys
sys.path.append('..')
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
        ipAddr=Utilities.getIPFromIP138()
        print "Your IP is:", ipAddr

    def testSendEmail(self):
#        emailAddr , password, smtpServer, smtpPort, mesgContent
        pass

if __name__ == '__main__':
	unittest.main()
