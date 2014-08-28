# -*- coding: utf-8 -*-

# Scrapy settings for douban_movie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douban_movie'

SPIDER_MODULES = ['douban_movie.spiders']
NEWSPIDER_MODULE = 'douban_movie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_movie (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['douban_movie.pipelines.DoubanMoviePipeline']

DATABASE = {
  'drivername': 'mysql',
  'host'      : 'localhost',
  'port'      : '3306',
  'username'  : 'root',
  'password'  : 'root',
  'database'  : 'douban_movie'
}

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'