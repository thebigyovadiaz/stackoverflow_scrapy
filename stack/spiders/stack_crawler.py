# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'http://stackoverflow.com/questions?pagesize=50&sort=newest'
    ]

    rules = (
        Rule(
            LinkExtractor(allow=r'questions\?page=[0-9]&sort=newest'),
            callback='parse_item',
            follow=True
        ),
    )

    def parse_item(self, response):
        item = StackItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
