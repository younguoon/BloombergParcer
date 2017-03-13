# -*- coding: utf-8 -*-
'''
Created on 2017. 2. 21.

@author: User
'''

import win32com.client

# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# instMarketEye = win32com.client.Dispatch("cpsysdib.MarketEye")
instFutureFtu = win32com.client.Dispatch("cpsysdib.FutOptChart")

instFutureFtu.SetInputValue(0, '201M3272')
instFutureFtu.SetInputValue(1, '1')
instFutureFtu.SetInputValue(2, 20170110)
instFutureFtu.SetInputValue(3, 20170101)
instFutureFtu.SetInputValue(4, 1000)
instFutureFtu.SetInputValue(5, [0,1,2,3,4,5,6,7,8,9])
instFutureFtu.SetInputValue(6, 'D')
instFutureFtu.SetInputValue(7, 10)
instFutureFtu.SetInputValue(8, '0')
instFutureFtu.SetInputValue(9, '0')
# instFutureFtu.request()
instFutureFtu.BlockRequest()

tickCode = instFutureFtu.getHeaderValue(0)
tickTotal = instFutureFtu.getHeaderValue(1)
tickName = instFutureFtu.getHeaderValue(2)
tickVolume = instFutureFtu.getHeaderValue(9)


print "code,    name,    total,    volume"
print tickCode,  tickName, tickTotal, tickVolume



# codeList = instCpCodeMgr.GetStockListByMarket(1)
# codeList = codeList + instCpCodeMgr.GetStockListByMarket(2)
# 
# instMarketEye.SetInputValue(0,[20])
# 
# print "code", "," ,
# print "name", "," ,
# print "totalStrock"
# 
# for i, code in enumerate(codeList):
#     secondCode = instCpCodeMgr.GetStockSectionKind(code)
#     name = instCpCodeMgr.CodeToName(code)
#     marketCode = instCpCodeMgr.GetStockMarketKind(code)
# 
#     instMarketEye.SetInputValue(1, [code])
#     instMarketEye.BlockRequest()
#     totalStock = instMarketEye.GetDataValue(0,0)
# 
#     if len(name)!=0 and secondCode==1:
#         #print i, "," , code ,"," , secondCode,",", name, ",", marketCode
#         #print i     , "," ,
#         print code[1:]    , "," , #218150, secondCode,",", name, ",", marketCode
#         print name.encode('utf-8') , "," ,
#         print totalStock

