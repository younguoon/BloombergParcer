# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YesCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code       = scrapy.Field()
    Year_Month = scrapy.Field()
    
    profit_06Y = scrapy.Field()
    profit_07Y = scrapy.Field()
    profit_08Y = scrapy.Field()
    profit_09Y = scrapy.Field()
    profit_10Y = scrapy.Field()
    profit_11Y = scrapy.Field()
    profit_12Y = scrapy.Field()
    profit_13Y = scrapy.Field()
    profit_14Y = scrapy.Field()
    profit_15Y = scrapy.Field()
    
    asset_06Y = scrapy.Field()
    asset_07Y = scrapy.Field()
    asset_08Y = scrapy.Field()
    asset_09Y = scrapy.Field()
    asset_10Y = scrapy.Field()
    asset_11Y = scrapy.Field()
    asset_12Y = scrapy.Field()
    asset_13Y = scrapy.Field()
    asset_14Y = scrapy.Field()
    asset_15Y = scrapy.Field()
    
#     entname = scrapy.Field()
    #title = scrapy.Field()
    #author = scrapy.Field()
    #date = scrapy.Field()
    
