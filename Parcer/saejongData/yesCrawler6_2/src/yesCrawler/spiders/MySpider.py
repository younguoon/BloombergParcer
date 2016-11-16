#-*coding:utf-8 -*-
#scrapy crawl yes

'''
Created on 2016. 7. 11.

@author: kitri
'''

import json
import logging

from scrapy import Selector
from scrapy.http.request import Request
from scrapy.spiders import Spider

from saejongData.yesCrawler6_2.src.yesCrawler.items import YesCrawlerItem


start_page = 20
end_page = 124000
next_page= '000020'

class MySpider(Spider):
    
    name ="yes" #내가 작성한 스파이더의 이름 -나중에 이 이름을 이용해서 실행
    allowed_domains=["http://sejongdata.co.kr/"] #크롤링할 최상위 도메인 - 어디에서 가져올것인지

    #실제 크롤링할 주소
    start_urls = ["http://www.sejongdata.com/business_include_fr/table_main0_bus_01.html?&no=0000"+str(start_page)]
        
    def parse(self,response): 
        global start_page, end_page, next_page
        #정의한 주소에서 전체 소스코드를 가져올 객체
        myselector = Selector(response)
        logging.info(response)
        
        #xpath문법을 이용해서 필요한 영역을 잘라서 contents에 저장
#         contents = myselector.xpath('//table[35]//tr[2]//td[1]//table[1]')
#         contents = myselector.xpath('//table[52]//tr[2]//td[1]//table')
        contents = myselector.xpath('//table[2]')
        
        #데이터를 DaumcrawlerItem별로 구분해서 담을 리스트를 선언
        items =[]
        for content in contents:
            item = YesCrawlerItem() #데이터를 담기위한 item객체를 생성 -dto동일
            
            #contents에서 필요한 정보만 추출해서 item의 field에 담기
            #dl태그아래 dt태그안에 정의된 a태그의 값을 추출
            
            item['code']= next_page #종목코드
            item['Year_Month'] = content.xpath("tr[1]/td[2]/text()").extract()[0].strip() #년도,분기
            if item['Year_Month'] == '2007.03' or item['Year_Month'] == '2007.06' or item['Year_Month'] == '2007.09' or item['Year_Month'] == '2007.12' : 
                
                item['profit_06Y'] = None #순이익
                item['profit_07Y'] = content.xpath("tr[4]/td[2]/text()").extract() #순이익
                item['profit_08Y'] = content.xpath("tr[4]/td[3]/text()").extract() #순이익
                item['profit_09Y'] = content.xpath("tr[4]/td[4]/text()").extract() #순이익
                item['profit_10Y'] = content.xpath("tr[4]/td[5]/text()").extract() #순이익
                item['profit_11Y'] = content.xpath("tr[4]/td[6]/text()").extract() #순이익
                item['profit_12Y'] = content.xpath("tr[4]/td[7]/text()").extract() #순이익
                item['profit_13Y'] = content.xpath("tr[4]/td[8]/text()").extract() #순이익
                item['profit_14Y'] = content.xpath("tr[4]/td[9]/text()").extract() #순이익
                item['profit_15Y'] = content.xpath("tr[4]/td[10]/text()").extract() #순이익
                
                item['asset_06Y'] = None #자산
                item['asset_07Y'] = content.xpath("tr[6]/td[2]/text()").extract() #자산
                item['asset_08Y'] = content.xpath("tr[6]/td[3]/text()").extract() #자산
                item['asset_09Y'] = content.xpath("tr[6]/td[4]/text()").extract() #자산
                item['asset_10Y'] = content.xpath("tr[6]/td[5]/text()").extract() #자산
                item['asset_11Y'] = content.xpath("tr[6]/td[6]/text()").extract() #자산
                item['asset_12Y'] = content.xpath("tr[6]/td[7]/text()").extract() #자산
                item['asset_13Y'] = content.xpath("tr[6]/td[8]/text()").extract() #자산
                item['asset_14Y'] = content.xpath("tr[6]/td[9]/text()").extract() #자산
                item['asset_15Y'] = content.xpath("tr[6]/td[10]/text()").extract() #자산
                
                if (
                    len(item['profit_07Y'])==0 or 
                    len(item['profit_08Y'])==0 or
                    len(item['profit_09Y'])==0 or 
                    len(item['profit_10Y'])==0 or 
                    len(item['profit_11Y'])==0 or 
                    len(item['profit_12Y'])==0 or
                    len(item['profit_13Y'])==0 or 
                    len(item['profit_14Y'])==0 or 
                    len(item['profit_15Y'])==0 or 
                     
                    len(item['asset_07Y'])==0 or 
                    len(item['asset_08Y'])==0 or
                    len(item['asset_09Y'])==0 or 
                    len(item['asset_10Y'])==0 or 
                    len(item['asset_11Y'])==0 or 
                    len(item['asset_12Y'])==0 or
                    len(item['asset_13Y'])==0 or 
                    len(item['asset_14Y'])==0 or 
                    len(item['asset_15Y'])==0 ):
                    print "******************No Data******************"
                else :
                    yield item
                    print item
            else :
                print "******************No 07Y Data******************"
            if start_page <= end_page :
                start_page = start_page+10
                if(start_page<100):
                    next_page = "0000"+str(start_page)
                elif (start_page<1000):
                    next_page = "000"+str(start_page)
                elif(start_page<10000):
                    next_page="00"+str(start_page)
                elif(start_page<100000):
                    next_page="0"+str(start_page)
                elif(start_page<1000000):
                    next_page=str(start_page)
                
                
                next_page1 = ["http://www.sejongdata.com/business_include_fr/table_main0_bus_01.html?&no="+str(next_page)]
                yield Request(next_page1[0],self.parse,dont_filter=True)




