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

    def parse(self, response):
      movies = []
      for sel in response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/ul[@class='list-view']/li/div[@class='item-show']/div[@class='title']"):
        movie = DoubanMovieItem()
        title = sel.xpath('a/text()').extract()[0]
        link  = sel.xpath('a/@href').extract()[0]
        title_arr = title.split('/')
        movie['title_cn'] = title_arr[0].strip()
        movie['link'] = link.strip()
        # if len(title_arr) > 1:
        #   movie['title_en'] = title_arr[1].strip()
        # else:
        #   movie['title_en'] = movie['title_cn']
        movies.append(movie)

      for movie in movies:
        yield Request(movie['link'], meta={'movie':movie}, callback=self.parse_detail)

      try:
          next_url = response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/div[@class='paginator']/span[@class='next']/a/@href").extract()[0]
      except:
         raise StopIteration
      yield Request(next_url, callback=self.parse)

    def parse_detail(self, response):
      movie = response.meta["movie"]
      title_cn_original = response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/h1/span[1]/text()").extract()[0]
      movie['title_original'] = title_cn_original.replace(movie["title_cn"], "").strip()

      # movie_detail_span = response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/div[@class='indent clearfix']/div[@class='subjectwrap clearfix']/div[@class='subject clearfix']/div[@id='info']/span[@class='pl']")
      # for span in movie_detail_span:
      #   print span.xpath('/text()').extract()

      # movie['board'] =parseTuple[1]
      # movie['time'] = parseTuple[2]
      # movie['content'] = parseTuple[3]
      yield movie
