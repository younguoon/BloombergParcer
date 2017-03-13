#coding: utf-8
'''
Created on 2017. 2. 21.

@author: DELL
'''

import win32com 
import win32com.client 
import pythoncom 

server="demo.etrade.co.kr" 
port = 20001 

user="" 
password="" 
certpasswd = "" 
servertype = 1 
showcerterror = 1 

base_directory = "c:/xing/" 
res_directory = base_directory + "res/" 

class XASessionEvents: 
    def OnLogin(self, *args): 
        print "OnLogin", args 

 def OnLogout(self, *args): 
 print "OnLogout", args 

 def OnDisconnect(self, *args): 
 print "OnDisconnect", args 

XASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEvents) 
XASession.ConnectServer(server, port) 
XASession.Login(user, password, certpasswd, servertype, showcerterror) 
