import scrapy
import numpy as np

from douban.items import DoubanGroupItem

class DoubanGroupSpider(scrapy.Spider):

    name = "doubangroup"

    allowed_domains = ["douban.com"]

    start_urls = []
    for i in range(30):
        start_urls.append("https://www.douban.com/group/beijingzufang/discussion?start=%s"%(i*25))

    for i in range(30):
        start_urls.append("https://www.douban.com/group/zhufang/discussion?start=%s"%(i*25))

    for i in range(30):
        start_urls.append("https://www.douban.com/group/26926/discussion?start=%s"%(i*25))

    def parse(self, response):

        for t in response.xpath("//table[@class='olt']//td[@class='title']"):
            item = DoubanGroupItem()

            item['group_title'] = t.xpath('a/text()').extract()[0]
            item['group_url'] = t.xpath('a/@href').extract()[0]

            print item['group_url']
            request = scrapy.Request(item['group_url'],
                                     callback=self.parse_desc_page)
            request.meta['item'] = item
            yield request

    def parse_desc_page(self, response):
        item = response.meta['item']
        desc = response.xpath("//div[@class='article']/div[contains(@class, 'topic-content')]/div[contains(@class, 'topic-doc')]/div[contains(@id, 'link-report')]//p/text()").extract()
        item['group_desc'] = "\n".join(desc)

        replys = []
        for t in response.xpath("//ul[contains(@class, 'topic-reply')]/li/div[contains(@class, 'content')]"):
            r = t.xpath(".//p/text()").extract()
            replys.append("---".join(np.array(r).flatten()))

        item['group_replys'] = "\r\n".join(replys)
        return item
