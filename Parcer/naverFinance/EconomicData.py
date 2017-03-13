# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 21.

@author: Young
'''
# -*- coding: utf-8 -*-
# from selenium.selenium import selenium

'''
Created on 2016. 8. 21.

@author: Young
'''

import os
import sys
import sys
from time import sleep

from bs4 import BeautifulSoup
from pygments.lexers import css
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import selenium.webdriver.support.ui as ui


# movetoelement=css(".content")


# sys.stdout = open("C:\Bloomberg_DATA_MadeByYounguoon.txt", "w")
#Currency, krwjpy
# 기존 코드(Javascript 동적 파싱)
url = "http://info.finance.naver.com/marketindex/"
driver = webdriver.PhantomJS('c:/phantomjs-2.1.1-windows/bin/phantomjs')
# action = ActionChains
driver.get(url)
# driver.find_elements_by_class_name("time-frame__choice")[1].click()
# selenium.set_cursor_position(self, locator, position)
# action.move_to_element(movetoelement)
# action.perform()

# sleep(5)
html = driver.page_source

soup_Currency_Krwjpy = BeautifulSoup(html, "html.parser")
# links_Currency_Krwjpy_Today = soup_Currency_Krwjpy.find_all("text",{"class":"panel__hover-value"})[0]

print soup_Currency_Krwjpy
driver.close()



# print '- 엔/달러 :', links_Currency_Krwjpy_Today.find_all("text",{"x":"692"})[0].text.strip(),  '(하루전)'
# print '- 엔/달러 :', links_Currency_Krwjpy_Today.find_all("text",{"x":"669.0667"})[0].text.strip(),  '(이틀전)'
#                                                                     669.8065
#                                                                     669.0667
#                                                                     668.2759
# print '- 엔/달러 :', links_Currency_Krwjpy_Today.find_all("text",{"x":"646.1334"})[0].text.strip(),  '(삼일전)'
#                                                                     647.6129
#                                                                     646.1334
#                                                                     644.5517








# #Currency, DollerIndex
# url_DollerIndex = "http://www.bloomberg.com/quote/DXY:CUR"
# DollerIndex = requests.get(url_DollerIndex)
# soup_DollerIndex = BeautifulSoup(DollerIndex.content, "html.parser")    
# links_DollerIndex_Value = soup_DollerIndex.find_all("div", {"data-view-uid":"1|0_6_1"})[0]
# links_DollerIndex_NetChange = soup_DollerIndex.find_all("div", {"class":"change-container"})[0]
# 
# print '- 달러인덱스 :', links_DollerIndex_Value.find_all("div",{"class":"price"})[0].text.strip(),  '(',links_DollerIndex_NetChange.find_all("div")[1].text.strip(),')'
# 
# #Currency, Usdkrw
# url_Usdkrw = "http://www.bloomberg.com/quote/USDKRW:CUR"
# Usdkrw = requests.get(url_Usdkrw)
# soup_DollerIndex = BeautifulSoup(Usdkrw.content, "html.parser")    
# links_Usdkrw_Value = soup_DollerIndex.find_all("div", {"data-view-uid":"1|0_6_1"})[0]
# links_Usdkrw_NetChange = soup_DollerIndex.find_all("div", {"class":"change-container"})[0]
# 
# print '- 원/달러 :', links_Usdkrw_Value.find_all("div",{"class":"price"})[0].text.strip(),  '(',links_Usdkrw_NetChange.find_all("div")[1].text.strip(),')'
# 
# #Currency, Usdjpy
# url_Currency_Usdjpy = "http://www.bloomberg.com/quote/KRWJPY:CUR"
# Currency_Usdjpy = requests.get(url_Currency_Usdjpy)
# soup_Currency_Usdjpy = BeautifulSoup(Currency_Usdjpy.content, "html.parser")    
# links_Currency_Usdjpy_Value = soup_Currency_Usdjpy.find_all("div", {"class":"basic-quote"})[0]
# links_Currency_Usdjpy_NetChange = soup_Currency_Usdjpy.find_all("div", {"class":"change-container"})[0]
# 
# #Currency, krwjpy
# url_Currency_Krwjpy = "http://www.bloomberg.com/quote/KRWJPY:CUR"
# Currency_Krwjpy = requests.get(url_Currency_Krwjpy)
# soup_Currency_Krwjpy = BeautifulSoup(Currency_Krwjpy.content, "html.parser")    
# links_Currency_Krwjpy_Value = soup_Currency_Krwjpy.find_all("div", {"class":"basic-quote"})[0]
# links_Currency_Krwjpy_NetChange = soup_Currency_Krwjpy.find_all("div", {"class":"change-container"})[0]
#  
# #Currency, Eurusd
# url_Currency_Eurusd = "http://www.bloomberg.com/quote/EURUSD:CUR"
# Currency_Eurusd = requests.get(url_Currency_Eurusd)
# soup_Currency_Eurusd = BeautifulSoup(Currency_Eurusd.content, "html.parser")    
# links_Currency_Eurusd_Value = soup_Currency_Eurusd.find_all("div", {"class":"basic-quote"})[0]
# links_Currency_Eurusd_NetChange = soup_Currency_Eurusd.find_all("div", {"class":"change-container"})[0]
# 
# #Currency, Gbpeur
# url_Currency_Gbpeur = "http://www.bloomberg.com/quote/GBPEUR:CUR"
# Currency_Gbpeur = requests.get(url_Currency_Gbpeur)
# soup_Currency_Gbpeur = BeautifulSoup(Currency_Gbpeur.content, "html.parser")    
# links_Currency_Gbpeur_Value = soup_Currency_Gbpeur.find_all("div", {"class":"basic-quote"})[0]
# links_Currency_Gbpeur_NetChange = soup_Currency_Gbpeur.find_all("div", {"class":"change-container"})[0]
# 
# #Currency, Usdcny
# url_Currency_Usdcny = "http://www.bloomberg.com/quote/USDCNY:CUR"
# Currency_Usdcny = requests.get(url_Currency_Usdcny)
# soup_Currency_Usdcny = BeautifulSoup(Currency_Usdcny.content, "html.parser")    
# links_Currency_Usdcny_Value = soup_Currency_Usdcny.find_all("div", {"class":"basic-quote"})[0]
# links_Currency_Usdcny_NetChange = soup_Currency_Usdcny.find_all("div", {"class":"change-container"})[0]
# 
# #Currency, Brl
# url_Currency_Brl = "http://www.bloomberg.com/quote/USDBRL:CUR"
# Currency_Brl = requests.get(url_Currency_Brl)
# soup_Currency_Brl = BeautifulSoup(Currency_Brl.content, "html.parser")    
# links_Currency_Brl_Value = soup_Currency_Brl.find_all("div", {"data-view-uid":"1|0_6_1"})[0]
# links_Currency_Brl_NetChange = soup_Currency_Brl.find_all("div", {"class":"change-container"})[0]




# #Currency
# url_Currency = "http://www.bloomberg.com/markets/currencies/"
# Currency = requests.get(url_Currency)
# soup_Currency = BeautifulSoup(Currency.content, "html.parser")
# links_Currency = soup_Currency.find_all("tbody")
#  
# #Currency, China
# url_Currency_Asia = "http://www.bloomberg.com/markets/currencies/asia-pacific"
# currency_Asia = requests.get(url_Currency_Asia)
# soup_currency_Asia = BeautifulSoup(currency_Asia.content, "html.parser")    
# links_Currency_Asia = soup_currency_Asia.find_all("tbody")  
# 

# #Comodities 
# url_Comodities = "http://www.bloomberg.com/markets/commodities"
# Comodities = requests.get(url_Comodities)
# soup_Comodities = BeautifulSoup(Comodities.content, "html.parser") 
# links_Comodities_Energy = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[1]
# links_PreciousAndIndustrialMetals = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[2]
# links_Agriculture = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[3]
# 
# #Comodities_Agriculture
# url_Comodities_Agriculture = "http://www.bloomberg.com/markets/commodities/futures/agriculture"
# Comodities_Agriculture = requests.get(url_Comodities)
# soup_Comodities_Agriculture = BeautifulSoup(Comodities.content, "html.parser") 
# links_Comodities_Agriculture_Soybean = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[1]

# #대두
# print '- 대두 : ', links_Agriculture.find_all("td")[35].text.strip(),  '(',links_Agriculture.find_all("td")[37].text.strip(),')', '/ 밀 : ', links_Agriculture.find_all("td")[10].text.strip(),  '(',links_Agriculture.find_all("td")[12].text.strip(),')'


# #Metals
# url_Metals = "http://www.bloomberg.com/markets/commodities/futures/metals"
# Metals = requests.get(url_Metals)
# soup_Metals = BeautifulSoup(Metals.content, "html.parser") 
# links_Metals = soup_Metals.find_all("tbody", {"class":"price-container up"})[3]

#Energy
# print ''
# print '- WTI : ', links_Comodities_Energy.find_all("td")[2].text.strip(),  '(',links_Comodities_Energy.find_all("td")[4].text.strip(),')'
# print ''    
# print '- 금 : ', links_PreciousAndIndustrialMetals.find_all("td")[2].text.strip(),  '(',links_PreciousAndIndustrialMetals.find_all("td")[4].text.strip(),')', '/ 은 : ', links_PreciousAndIndustrialMetals.find_all("td")[18].text.strip(),  '(',links_PreciousAndIndustrialMetals.find_all("td")[20].text.strip(),')'
# print ''
# print '- 구리 : ', links_PreciousAndIndustrialMetals.find_all("td")[26].text.strip(),  '(',links_PreciousAndIndustrialMetals.find_all("td")[28].text.strip(),')', '/ 알루미늄 : ', links_Metals.find_all("td")[19].text.strip(),  '(',links_Metals.find_all("td")[20].text.strip(),')'
# print ''
# print '- 옥수수 : ', links_Agriculture.find_all("td")[2].text.strip(),  '(',links_Agriculture.find_all("td")[4].text.strip(),')', '/ 밀 : ', links_Agriculture.find_all("td")[10].text.strip(),  '(',links_Agriculture.find_all("td")[12].text.strip(),')'
# print ''

#커피
#설탕
#원단

# #Currencies
# for item1 in links_Currency :
#     #달러인덱스
#     print '- 달러인덱스 :', links_DollerIndex_Value.find_all("div",{"class":"price"})[0].text.strip(),  '(',links_DollerIndex_NetChange.find_all("div")[1].text.strip(),')',             '/ 원/달러 :', item1.find_all("td", {"class":"data-table__row__cell"})[61].text.strip(),  '(',item1.find_all("td", {"class":"data-table__row__cell"})[63].text.strip(),')'
#     print '- 엔/달러 :', item1.find_all("td", {"class":"data-table__row__cell"})[7].text.strip(),  '(',item1.find_all("td", {"class":"data-table__row__cell"})[9].text.strip(),')',     '/ 원/엔 :', links_Currency_Krwjpy_Value.find_all("div",{"class":"price"})[0].text.strip(),  '(',links_Currency_Krwjpy_NetChange.find_all("div")[1].text.strip(),')'
#     print '- 달러/유로 :', item1.find_all("td", {"class":"data-table__row__cell"})[1].text.strip(),  '(',item1.find_all("td", {"class":"data-table__row__cell"})[3].text.strip(),')',    '/ 파운드/유로 :', item1.find_all("td", {"class":"data-table__row__cell"})[1].text.strip(),  '(',item1.find_all("td", {"class":"data-table__row__cell"})[3].text.strip(),')'
# for item2 in links_Currency_Asia :
#     print '- 위안/달러 :', item2.find_all("td", {"class":"data-table__row__cell"})[79].text.strip(),  '(',item2.find_all("td", {"class":"data-table__row__cell"})[81].text.strip(),')',  '/ 헤알/달러 :', links_Currency_Brl_Value.find_all("div",{"class":"price"})[0].text.strip(),  '(',links_Currency_Brl_NetChange.find_all("div")[1].text.strip(),')'






#     print '- 엔/달러 : ', item1.find_all("td", {"class":"data-table__row__cell"})[7].text.strip(),  '(',item1.find_all("td", {"class":"data-table__row__cell"})[9].text.strip(),')'
    
#     print '유로/달러'
#     print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[0].text.strip(), '(€)'
#     print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[1].text.strip(), '€'
#     print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[2].text.strip(), '€'
#     print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[3].text.strip()
#     print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[4].text.strip()
#     print ''
#        
#     print "엔/달러"
#     print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[6].text.strip(), '(¥)'
#     print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[7].text.strip(), '¥'
#     print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[8].text.strip(), '¥'
#     print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[9].text.strip()
#     print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[10].text.strip()
#     print ''
#        
#     print "원/달러"
#     print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[60].text.strip(),'(₩)'
#     print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[61].text.strip(),'₩'
#     print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[62].text.strip(),'₩'
#     print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[63].text.strip()
#     print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[64].text.strip()
#     print ''
  
    
#     print "위안/달러"
#     print 'Currency : ', item2.find_all("td", {"class":"data-table__row__cell"})[78].text.strip(),'(¥)'
#     print 'Value :',  item2.find_all("td", {"class":"data-table__row__cell"})[79].text.strip(),'¥'
#     print 'Change :',  item2.find_all("td", {"class":"data-table__row__cell"})[80].text.strip(),'¥'
#     print 'netChange :',  item2.find_all("td", {"class":"data-table__row__cell"})[81].text.strip()
#     print 'Time :',  item2.find_all("td", {"class":"data-table__row__cell"})[82].text.strip()
#     print ''


#Energy
#WTI
# print links_Comodities_Energy.find_all("div", {"data-type":"full"})[0].text.strip()
# print 'units : ', links_Comodities_Energy.find_all("td")[1].text.strip()
# print 'Price : ', links_Comodities_Energy.find_all("td")[2].text.strip()
# print 'Change : ', links_Comodities_Energy.find_all("td")[3].text.strip()
# print 'NetChange : ', links_Comodities_Energy.find_all("td")[4].text.strip()
# print 'Contract : ', links_Comodities_Energy.find_all("td")[5].text.strip()
# print 'Time : ', links_Comodities_Energy.find_all("td")[6].text.strip()    
# print ''
 
#Brant Oil
# print '- Brant Oil : ', links_Comodities_Energy.find_all("td")[10].text.strip(),  '(',links_Comodities_Energy.find_all("td")[12].text.strip(),')'
# print ''
# print links_Comodities_Energy.find_all("div", {"data-type":"full"})[1].text.strip()
# print 'units : ', links_Comodities_Energy.find_all("td")[9].text.strip()
# print 'Price : ', links_Comodities_Energy.find_all("td")[10].text.strip()
# print 'Change : ', links_Comodities_Energy.find_all("td")[11].text.strip()
# print 'NetChange : ', links_Comodities_Energy.find_all("td")[12].text.strip()
# print 'Contract : ', links_Comodities_Energy.find_all("td")[13].text.strip()
# print 'Time : ', links_Comodities_Energy.find_all("td")[14].text.strip()    
# print ''
 
#Precious and Industrial Metals
#Gold
# print links_PreciousAndIndustrialMetals.find_all("div", {"data-type":"full"})[0].text.strip()
# print 'units : ', links_PreciousAndIndustrialMetals.find_all("td")[1].text.strip()
# print 'Price : ', links_PreciousAndIndustrialMetals.find_all("td")[2].text.strip()
# print 'Change : ', links_PreciousAndIndustrialMetals.find_all("td")[3].text.strip()
# print 'NetChange : ', links_PreciousAndIndustrialMetals.find_all("td")[4].text.strip()
# print 'Contract : ', links_PreciousAndIndustrialMetals.find_all("td")[5].text.strip()
# print 'Time : ', links_PreciousAndIndustrialMetals.find_all("td")[6].text.strip()    
# print ''
  
#Copper
# print links_PreciousAndIndustrialMetals.find_all("div", {"data-type":"full"})[3].text.strip()
# print 'units : ', links_PreciousAndIndustrialMetals.find_all("td")[25].text.strip()
# print 'Price : ', links_PreciousAndIndustrialMetals.find_all("td")[26].text.strip()
# print 'Change : ', links_PreciousAndIndustrialMetals.find_all("td")[27].text.strip()
# print 'NetChange : ', links_PreciousAndIndustrialMetals.find_all("td")[28].text.strip()
# print 'Contract : ', links_PreciousAndIndustrialMetals.find_all("td")[29].text.strip()
# print 'Time : ', links_PreciousAndIndustrialMetals.find_all("td")[30].text.strip()    
# print ''
 
#Agreculture
#Corn
# print links_Agriculture.find_all("div", {"data-type":"full"})[0].text.strip()
# print 'units : ', links_Agriculture.find_all("td")[1].text.strip()
# print 'Price : ', links_Agriculture.find_all("td")[2].text.strip()
# print 'Change : ', links_Agriculture.find_all("td")[3].text.strip()
# print 'NetChange : ', links_Agriculture.find_all("td")[4].text.strip()
# print 'Contract : ', links_Agriculture.find_all("td")[5].text.strip()
# print 'Time : ', links_Agriculture.find_all("td")[6].text.strip()    
# print ''
 
#Wheat
# print links_Agriculture.find_all("div", {"data-type":"full"})[1].text.strip()
# print 'units : ', links_Agriculture.find_all("td")[9].text.strip()
# print 'Price : ', links_Agriculture.find_all("td")[10].text.strip()
# print 'Change : ', links_Agriculture.find_all("td")[11].text.strip()
# print 'NetChange : ', links_Agriculture.find_all("td")[12].text.strip()
# print 'Contract : ', links_Agriculture.find_all("td")[13].text.strip()
# print 'Time : ', links_Agriculture.find_all("td")[14].text.strip()    
# print ''


