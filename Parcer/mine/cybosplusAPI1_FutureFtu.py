# -*- coding: utf-8 -*-
'''
Created on 2017. 2. 21.

@author: User
'''

import win32com.client

# instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
# instMarketEye = win32com.client.Dispatch("cpsysdib.MarketEye")
instFutureFtu = win32com.client.Dispatch("dscbo1.FutureFtu")

instFutureFtu.SetInputValue(0, '201M3272')
instFutureFtu.SetInputValue(1, 'T')
instFutureFtu.SetInputValue(2, 120)
instFutureFtu.SetInputValue(3, 100)
instFutureFtu.SetInputValue(4, '0')
instFutureFtu.SetInputValue(5, '0')

instFutureFtu.Received
instFutureFtu.Request()

tickDate = instFutureFtu.GetHeaderValue(0)
tickTime = instFutureFtu.GetHeaderValue(1)

# tickDataDate = instFutureFtu.getDataValue(0)

print "date,    time"
print tickDate,  tickTime


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

