# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field


class StackItem(scrapy.Item):
    title = Field()
    url = Field()
