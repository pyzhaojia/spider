# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdspiderPipeline(object):
    def process_item(self, item, spider):
        item = str(item)
        with open('22.txt', 'a') as f:
            f.write(item)
        return item