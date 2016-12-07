# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re

class BrushaobosircsdnSpider(scrapy.Spider):
    name = "brushAoboSirCsdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        url = 'http://blog.csdn.net/github_35160620/'
        yield Request(url=url, callback=self.blogerHome)

    def blogerHome(self, response):
        extract_page_num = response.xpath("//div[@id='papelist']/span/text()").extract()
        # print(type(extract_page_num))
        # print(extract_page_num)
        pattam_page_num = '共(.*?)页'
        # print(type(pattam_page_num))
        # print(pattam_page_num)
        page_num = re.compile(pattam_page_num).findall(extract_page_num[0])[0]
        # print(page_num)
        # print(type(page_num))
        for i in range(1, int(page_num)+1):
            page_url = 'http://blog.csdn.net/github_35160620/article/list/' + str(i)
            # print(page_url)
            yield Request(url=page_url, callback=self.blog)
        pass

    def blog(self, response):
        url = response.xpath("//h3[@class='list_c_t']/a/@href").extract()
        # print(len(url))
        # print(url)
        for i in range(len(url)):
            this_url = 'http://blog.csdn.net' + url[i]
            yield Request(url=this_url, callback=self.next)
        pass


    def next(self, response):
        pattam_visits = '<dt class="item">(.*?)</dt>\r\n            <dd class="item_name">访问'
        # print('response.body type is ', type(response.body))
        # print('response.body.decode type is ', type(response.body.decode('utf-8', 'ignore')))

        body_data = response.body.decode('utf-8', 'ignore') # .replace(u'\xa9', u'')
        visits = re.compile(pattam_visits).findall(body_data)[0]
        print('当前访问量为：', visits)
        print('-------------------')
        import time
        time.sleep(1.0)
        pass
