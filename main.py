# -*- coding:utf-8 -*-
from scrapy import cmdline
# cmdline.execute('scrapy crawl nbnews'.split())

cmdline.execute('scrapy crawl nbnews -o nbnews.json'.split())