# -*- coding: utf-8 -*-
import scrapy


class FundaSpiderSpider(scrapy.Spider):
    name = 'funda_spider'
    allowed_domains = ['http://www.funda.nl/koop/amsterdam/']
    start_urls = ['http://http://www.funda.nl/koop/amsterdam//']

    def parse(self, response):
        pass
