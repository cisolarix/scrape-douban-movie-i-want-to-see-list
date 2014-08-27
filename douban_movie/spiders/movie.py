# -*- coding: utf-8 -*-

import scrapy

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.http import Request

from douban_movie.items import DoubanMovieItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/people/2128762/wish?sort=time&amp;start=0&amp;filter=all&amp;mode=list&amp;tags_sort=count',
    )
    # download_delay = 1

    def parse(self, response):
      for sel in response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/ul[@class='list-view']/li/div[@class='item-show']/div[@class='title']"):
        movie = DoubanMovieItem()
        title = sel.xpath('a/text()').extract()
        # link  = sel.xpath('a/@href').extract()
        title_arr = title[0].split('/')
        movie['title_cn'] = title_arr[0].strip()
        if len(title_arr) > 1:
          movie['title_en'] = title_arr[1].strip()
        else:
          movie['title_en'] = movie['title_cn']
        yield movie

      try:
          next_url = response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/div[@class='paginator']/span[@class='next']/a/@href").extract()[0]
      except:
         raise StopIteration
      yield Request(next_url, callback=self.parse)