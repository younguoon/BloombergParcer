# -*- coding: utf-8 -*-

'''
Created on 2017. 1. 24.

@author: Young
'''
import sys

from bs4 import BeautifulSoup
import requests


# sys.stdout = open("C:\NaverFinance.txt", "w")

#Currency
url_Currency = "http://info.finance.naver.com/marketindex/?tabSel=worldExchange#tab_section"
Currency = requests.get(url_Currency)
soup_Currency = BeautifulSoup(Currency.content, "html.parser")
links_Currency = soup_Currency.find_all("tbody")
 
for item1 in links_Currency :
    print '달러/영국 파운드'
    print 'Currency : ', item1.find_all("tr", {"class":"data-table__row__cell"})[0].text.strip()
#     print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[1].text.strip(), '€'
#     print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[2].text.strip(), '€'
#     print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[3].text.strip()
#     print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[4].text.strip()
#     print ''