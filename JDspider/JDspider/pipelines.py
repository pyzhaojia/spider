# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class JdspiderPipeline(object):
    def process_item(self, item, spider):
        # item = str(item)
        # with open('22.txt', 'a') as f:
        #     f.write(item)
        # 链接数据库
        item = dict(item)
        print('1111111111111111')
        cli = MongoClient('127.0.0.1', 27017)
        db = cli['JD']
        col = db['jd']
        col.insert_one(item)
        print('插入成功')
        return item
