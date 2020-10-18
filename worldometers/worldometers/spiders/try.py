import scrapy


class TrySpider(scrapy.Spider):
    name = 'try'
    allowed_domains = ['www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98']
    start_urls = ['https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98/']

    def parse(self, response):
        items = response.css

        yield{
            'items': items
        }

