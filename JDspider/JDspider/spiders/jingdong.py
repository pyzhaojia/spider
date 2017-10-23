# -*- coding: utf-8 -*-
import json
from JDspider.items import JdspiderItem
import scrapy
import re


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    # allowed_domains = ['jd.com']
    # 找到商品分类json链接
    start_urls = ['https://dc.3.cn/category/get']

    def parse(self, response):
        # 将json数据转化为字典
        result = json.loads(response.body.decode('gbk'))
        # 在字典中提取商品类别及链接
        for i in result['data']:
            for j in i['s']:
                for k in j['s']:
                    for m in k['s']:
                        # 提取类别名称
                        pattern1 = re.compile(r'\|(.*?)\|')
                        typename = pattern1.search(m['n']).group(0).replace('|', '')
                        # 提取类别链接
                        pattern2 = re.compile(r'(.*?)\|')
                        typeurl = 'https://' + pattern2.search(m['n']).group(0).replace('|', '')
                        yield scrapy.Request(url=typeurl, callback=self.parse_good_list, meta={'typename': typename})

    def parse_good_list(self, response):
        item = JdspiderItem()
        item['typename'] = response.meta['typename']
        item['goodslist'] =[]
        # 获取商品列表
        good_list = response.xpath('//*[@id="plist"]/ul/li/div/div[3]/a')


        id_list = []
        for good in good_list:
            i = {}
            good_url = 'https:' + good.xpath('./@href').extract_first()
            item['goodurl'] = good_url
            i['goodname'] = good.xpath('./em/text()').extract_first().replace('\n', '').strip()
            # print(i, '********************************************')
            id = re.findall(r'\d+', good_url)[0]
            good_id = 'J_' + str(id)
            id_list.append(good_id)

            yield scrapy.Request(url=good_url, callback=self.parse_detail, meta={'item': item, 'id_list': id_list, 'i': i})

    def parse_price(self, response):
        item = response.meta['item']
        result = json.loads(response.body.decode('gbk'))
        # 提取价格并添加到item中
        for i, k in zip(item['goodslist'], result):
            i['goodprice'] = k['p']

        print(item)
        yield item

    def parse_detail(self, response):
        item = response.meta['item']
        id_list = response.meta['id_list']
        i = response.meta['i']
        # 提取详细页商品介绍
        detail = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li/text()').extract()
        i['detail'] = detail
        item['goodslist'].append(i)
        # 找到价格所在json的链接
        url = 'http://p.3.cn/prices/mgets?ext=11000000&pin=&type=1&area=1_72_2799_0&skuIds={}&pdbp=0&pdtk=&pdpin=&pduid=559210059&source=list_pc_front'
        id_str = ','.join(id_list)
        yield scrapy.Request(url=url.format(id_str), callback=self.parse_price, meta={'item': item})