# -*- coding: utf-8 -*-
import scrapy

from douban_movie.items import DoubanMovieItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/people/2128762/wish?sort=time&amp;start=0&amp;filter=all&amp;mode=list&amp;tags_sort=count',
    )

    def parse(self, response):
      for sel in response.xpath("/html/body/div[@id='wrapper']/div[@id='content']/div/div[@class='article']/ul[@class='list-view']/li[@class='item']/div[@class='item-show']/div[@class='title']"):
        movie = DoubanMovieItem()
        title = sel.xpath('a/text()').extract()
        # print title
        # link  = sel.xpath('a/@href').extract()
        title_arr = title[0].split('/')
        # movie.title_cn = title_arr[0].strip()
        # movie.title_en = title_arr[1].strip()
        print title_arr[0].strip(), title_arr[1].strip()
