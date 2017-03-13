#-*- coding: utf-8 -*-

'''
Created on 2017. 2. 21.

@author: User
'''


import sys 
from time import sleep 

from bs4 import BeautifulSoup 
import requests 

# sys.stdout = open("C:\daumTest", "w") 
# 종목 종가 
url_daumFinance = "http://finance.daum.net/item/quote_yyyymmdd_sub.daum?code=000660&stype=1&yyyymmdd=20170221&seqno=660001&btime=1018&modify=0"
StockInfo = requests.get(url_daumFinance) 
# sleep(10) 
soup_StockInfo = BeautifulSoup(StockInfo.content, "html.parser")
#날짜
links_soup_StockInfo_date = soup_StockInfo.find_all("td",{"class","datetime2"})[0].text
#시가
links_soup_StockInfo_start = soup_StockInfo.find_all("td",{"class","num"})[0].text
#고가
links_soup_StockInfo_top = soup_StockInfo.find_all("td",{"class","num"})[1].text
#저가
links_soup_StockInfo_bottom = soup_StockInfo.find_all("td",{"class","num"})[2].text
#종가
links_soup_StockInfo_close = soup_StockInfo.find_all("td",{"class","num"})[3].text
#전일비
links_soup_StockInfo_ratio = soup_StockInfo.find_all("td",{"class","num"})[4].text
#등락률
links_soup_StockInfo_rate = soup_StockInfo.find_all("td",{"class","num"})[5].text
#거래량
links_soup_StockInfo_volume = soup_StockInfo.find_all("td",{"class","num"})[6].text

#페이지 전체
# print soup_StockInfo

print "일자, 시가, 고가, 저가, 종가, 전일비, 등락률, 거래량 "
#일자
print "일자 : " + links_soup_StockInfo_date.encode('utf-8')
#시가, 고가, 저가, 종가, 전일비, 등락률, 거래량
print "시가 : " + links_soup_StockInfo_start.encode('utf-8')
print "고가 : " + links_soup_StockInfo_top.encode('utf-8')
print "저가 : " + links_soup_StockInfo_bottom.encode('utf-8')
print "종가 : " + links_soup_StockInfo_close.encode('utf-8')
print "전일비 : " + links_soup_StockInfo_ratio.encode('utf-8')
print "등락률 : " + links_soup_StockInfo_rate.strip().encode('utf-8')
print "거래량 : " + links_soup_StockInfo_volume.encode('utf-8')



