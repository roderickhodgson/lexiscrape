from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from lexiscrape_crawler.items import Content

class LexiSpider(BaseSpider):
    name = "lexi"

    def __init__(self, *args, **kwargs): 
        super(LexiSpider, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('url')]
    
    
    def set_url(url):
        start_urls.append(url)

    def parse(self, response):
        content_item = Content()
        hxs = HtmlXPathSelector(response)
        title = hxs.select('//html/head/title/text()')
        body = hxs.select("//*[contains(@id, '')]/p/text()")

        content_item['body_raw'] = body.extract()
        content_item['title'] = title.extract()[0]

        return content_item
