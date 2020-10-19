import scrapy


class SpecailOffersSpider(scrapy.Spider):
    name = 'specail_offers'
    allowed_domains = ['www.cigabuy.com/weekly-deals-c-56_187.html']
    start_urls = ['https://www.cigabuy.com/weekly-deals-c-56_187.html/']

    def parse(self, response):
        pass
