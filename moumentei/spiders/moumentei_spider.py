__author__ = 'peter'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from moumentei.items import MoumenteiItem

def urls():
    # for a in range(841810, 2491107):
    for a in range(2491107, 2491109):
        yield 'http://mimi.me/comments/{0}/list'.format(a)


class MoumenteiSpider(BaseSpider):
    name = "moumentei"
    allowed_domains = ["mimi.me"]
    start_urls = urls()

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items=[]
        item= MoumenteiItem()
        item['url'] = response.url
        item['author'] = hxs.select('//li[@class="fl"]/text()').extract()[0]
        item['published_at'] = hxs.select('//li[@class="fr"]/text()').extract()[0]
        item['content'] = hxs.select('//div[@class="contentBox"]/p/text()').extract()[0]
        item['like'] = hxs.select('//li[@class="con_like"]/a/text()').extract()[0]
        item['dislike'] = hxs.select('//li[@class="con_unlike"]/a/text()').extract()[0]
        items.append(item)
        return items
