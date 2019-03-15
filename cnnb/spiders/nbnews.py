# -*- coding: utf-8 -*-
import scrapy
import newspaper
from time import sleep
from items import CnnbItem


class NbnewsSpider(scrapy.Spider):
    name = 'nbnews'
    allowed_domains = ['cnnb.com.cn']
    start_urls = ['http://nbnews.cnnb.com.cn/sz/', 'http://nbnews.cnnb.com.cn/cj/', 'http://nbnews.cnnb.com.cn/sh/',
                  'http://nbnews.cnnb.com.cn/kjw/', 'http://nbnews.cnnb.com.cn/wt/']

    def parse(self, response):
        if 'sz' in response.url:
            category = "时政经济"
        elif 'cj' in response.url:
            category = "民生城事"
        elif 'sh' in response.url:
            category = "突发现场"
        elif 'kjw' in response.url:
            category = "科教卫生"
        else:
            category = "文化体育"
        news_list = response.xpath('//div[@class="articleList"]//ul[@class="fiveBox"]//li//a//@href').extract()
        for item in news_list:
            news = CnnbItem()
            timeT = item.split("/")[-4:-1]
            news["time"] = "-".join(timeT)
            news["category"] = category
            article = newspaper.Article(item, language='zh')
            try:
                article.download()
                article.parse()
            except Exception as e:
                print(e.args)
            finally:
                news["title"] = article.title.split("-新闻中心")[0]
                news["text"] = article.text
            sleep(1)
            yield news
