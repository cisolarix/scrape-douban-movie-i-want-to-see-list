# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DoubanMovieItem(Item):
    title_cn       = Field()
    title_original = Field()
    title_alias    = Field()
    link           = Field()