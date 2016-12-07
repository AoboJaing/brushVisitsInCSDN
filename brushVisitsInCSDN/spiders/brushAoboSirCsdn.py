# -*- coding: utf-8 -*-
import scrapy


class BrushaobosircsdnSpider(scrapy.Spider):
    name = "brushAoboSirCsdn"
    allowed_domains = ["blog.csdn.net"]
    start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        pass
