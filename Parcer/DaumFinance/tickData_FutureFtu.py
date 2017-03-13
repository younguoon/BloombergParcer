#-*- coding: utf-8 -*-
'''
Created on 2017. 2. 21.

@author: User
'''
import win32com.client


inStockCode = win32com.client.Dispatch("dscbo1.FutureFtu")

# for i in range(0,100):
#     print(inStockCode.GetData(1,i))

numStocks = inStockCode.GetCount()
for i in range(0,numStocks):
    if "NAVER" in inStockCode.GetData(1,i):
      print (i,inStockCode.getData(1,i))  
      
        
        