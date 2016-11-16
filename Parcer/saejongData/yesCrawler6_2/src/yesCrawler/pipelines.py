# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class YesCrawlerPipeline(object):
#     def __init__(self):    
#         self.file = codecs.open("items_06_07Y(no dict)(2).csv", "wb", encoding="utf-8")


    def process_item(self, item, spider):
        return item

