# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanGroupItem(scrapy.Item):
    group_title = scrapy.Field();
    group_url = scrapy.Field();
    group_desc = scrapy.Field();
    group_replys = scrapy.Field();
