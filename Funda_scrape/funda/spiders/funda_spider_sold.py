# -*- coding: utf-8 -*-
import scrapy


class FundaSpiderSoldSpider(scrapy.Spider):
    name = 'funda_spider_sold'
    allowed_domains = ['http://www.funda.nl/koop/verkocht/']
    start_urls = ['http://http://www.funda.nl/koop/verkocht//']

    def parse(self, response):
        pass
