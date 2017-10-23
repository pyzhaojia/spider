# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 类别名称
    typename = scrapy.Field()
    # 类别链接
    typeurl = scrapy.Field()
    # 商品名称
    goodslist = scrapy.Field()
    # 商品url
    goodurl = scrapy.Field()
    # 商品价格
    goodprice = scrapy.Field()
    # 商品评价量
    evaluate = scrapy.Field()
