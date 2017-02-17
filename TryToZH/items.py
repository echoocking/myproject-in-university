# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TrytozhItem(scrapy.Item):
    # define the fields for your item here like:
    # try to save the items which been  cralwed from website, and try to get the datas easily
    # need to be stored
    URL = scrapy.Field()
    question = scrapy.Field()
    answer0 = scrapy.Field()
    answer1 = scrapy.Field()
    answer2 = scrapy.Field()
    answer3 = scrapy.Field()
    answer4 = scrapy.Field()
