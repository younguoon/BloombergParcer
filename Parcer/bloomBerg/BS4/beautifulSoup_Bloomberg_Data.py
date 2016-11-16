# -*- coding: utf-8 -*-
'''
Created on 2016. 8. 21.

@author: Young
'''
import sys

from bs4 import BeautifulSoup
import requests


sys.stdout = open("C:\Bloomberg_DATA.txt", "w")

#Currency
url_Currency = "http://www.bloomberg.com/markets/currencies/"
Currency = requests.get(url_Currency)
soup_Currency = BeautifulSoup(Currency.content, "html.parser")
links_Currency = soup_Currency.find_all("tbody")
 
#Currency, China(Overview에 없음)
url_Currency_Asia = "http://www.bloomberg.com/markets/currencies/asia-pacific"
currency_Asia = requests.get(url_Currency_Asia)
soup_currency_Asia = BeautifulSoup(currency_Asia.content, "html.parser")    
links_Currency_Asia = soup_currency_Asia.find_all("tbody")  

#Comodities 
url_Comodities = "http://www.bloomberg.com/markets/commodities"
Comodities = requests.get(url_Comodities)
soup_Comodities = BeautifulSoup(Comodities.content, "html.parser") 
links_Comodities_Energy = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[1]
links_PreciousAndIndustrialMetals = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[2]
links_Agriculture = soup_Comodities.find_all("tbody", {"class":"data-table__body"})[3]


#Currencies
for item1 in links_Currency :
    print '유로/달러'
    print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[0].text.strip(), '(€)'
    print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[1].text.strip(), '€'
    print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[2].text.strip(), '€'
    print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[3].text.strip()
    print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[4].text.strip()
    print ''
       
    print "엔/달러"
    print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[6].text.strip(), '(¥)'
    print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[7].text.strip(), '¥'
    print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[8].text.strip(), '¥'
    print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[9].text.strip()
    print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[10].text.strip()
    print ''
       
    print "원/달러"
    print 'Currency : ', item1.find_all("td", {"class":"data-table__row__cell"})[60].text.strip(),'(₩)'
    print 'Value :',  item1.find_all("td", {"class":"data-table__row__cell"})[61].text.strip(),'₩'
    print 'Change :',  item1.find_all("td", {"class":"data-table__row__cell"})[62].text.strip(),'₩'
    print 'netChange :',  item1.find_all("td", {"class":"data-table__row__cell"})[63].text.strip()
    print 'Time :',  item1.find_all("td", {"class":"data-table__row__cell"})[64].text.strip()
    print ''
  
for item2 in links_Currency_Asia :
    print "위안/달러"
    print 'Currency : ', item2.find_all("td", {"class":"data-table__row__cell"})[78].text.strip(),'(¥)'
    print 'Value :',  item2.find_all("td", {"class":"data-table__row__cell"})[79].text.strip(),'¥'
    print 'Change :',  item2.find_all("td", {"class":"data-table__row__cell"})[80].text.strip(),'¥'
    print 'netChange :',  item2.find_all("td", {"class":"data-table__row__cell"})[81].text.strip()
    print 'Time :',  item2.find_all("td", {"class":"data-table__row__cell"})[82].text.strip()
    print ''
 

#Energy
#WTI
print links_Comodities_Energy.find_all("div", {"data-type":"full"})[0].text.strip()
print 'units : ', links_Comodities_Energy.find_all("td")[1].text.strip()
print 'Price : ', links_Comodities_Energy.find_all("td")[2].text.strip()
print 'Change : ', links_Comodities_Energy.find_all("td")[3].text.strip()
print 'NetChange : ', links_Comodities_Energy.find_all("td")[4].text.strip()
print 'Contract : ', links_Comodities_Energy.find_all("td")[5].text.strip()
print 'Time : ', links_Comodities_Energy.find_all("td")[6].text.strip()    
print ''
 
#Brant Oil
print links_Comodities_Energy.find_all("div", {"data-type":"full"})[1].text.strip()
print 'units : ', links_Comodities_Energy.find_all("td")[9].text.strip()
print 'Price : ', links_Comodities_Energy.find_all("td")[10].text.strip()
print 'Change : ', links_Comodities_Energy.find_all("td")[11].text.strip()
print 'NetChange : ', links_Comodities_Energy.find_all("td")[12].text.strip()
print 'Contract : ', links_Comodities_Energy.find_all("td")[13].text.strip()
print 'Time : ', links_Comodities_Energy.find_all("td")[14].text.strip()    
print ''
 
#Precious and Industrial Metals
#Gold
print links_PreciousAndIndustrialMetals.find_all("div", {"data-type":"full"})[0].text.strip()
print 'units : ', links_PreciousAndIndustrialMetals.find_all("td")[1].text.strip()
print 'Price : ', links_PreciousAndIndustrialMetals.find_all("td")[2].text.strip()
print 'Change : ', links_PreciousAndIndustrialMetals.find_all("td")[3].text.strip()
print 'NetChange : ', links_PreciousAndIndustrialMetals.find_all("td")[4].text.strip()
print 'Contract : ', links_PreciousAndIndustrialMetals.find_all("td")[5].text.strip()
print 'Time : ', links_PreciousAndIndustrialMetals.find_all("td")[6].text.strip()    
print ''
  
#Copper
print links_PreciousAndIndustrialMetals.find_all("div", {"data-type":"full"})[3].text.strip()
print 'units : ', links_PreciousAndIndustrialMetals.find_all("td")[25].text.strip()
print 'Price : ', links_PreciousAndIndustrialMetals.find_all("td")[26].text.strip()
print 'Change : ', links_PreciousAndIndustrialMetals.find_all("td")[27].text.strip()
print 'NetChange : ', links_PreciousAndIndustrialMetals.find_all("td")[28].text.strip()
print 'Contract : ', links_PreciousAndIndustrialMetals.find_all("td")[29].text.strip()
print 'Time : ', links_PreciousAndIndustrialMetals.find_all("td")[30].text.strip()    
print ''
 
#Agreculture
#Corn
print links_Agriculture.find_all("div", {"data-type":"full"})[0].text.strip()
print 'units : ', links_Agriculture.find_all("td")[1].text.strip()
print 'Price : ', links_Agriculture.find_all("td")[2].text.strip()
print 'Change : ', links_Agriculture.find_all("td")[3].text.strip()
print 'NetChange : ', links_Agriculture.find_all("td")[4].text.strip()
print 'Contract : ', links_Agriculture.find_all("td")[5].text.strip()
print 'Time : ', links_Agriculture.find_all("td")[6].text.strip()    
print ''
 
#Wheat
print links_Agriculture.find_all("div", {"data-type":"full"})[1].text.strip()
print 'units : ', links_Agriculture.find_all("td")[9].text.strip()
print 'Price : ', links_Agriculture.find_all("td")[10].text.strip()
print 'Change : ', links_Agriculture.find_all("td")[11].text.strip()
print 'NetChange : ', links_Agriculture.find_all("td")[12].text.strip()
print 'Contract : ', links_Agriculture.find_all("td")[13].text.strip()
print 'Time : ', links_Agriculture.find_all("td")[14].text.strip()    
print ''


