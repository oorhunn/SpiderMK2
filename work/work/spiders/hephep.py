import scrapy


class HephepSpider(scrapy.Spider):
    name = 'hephep'
    allowed_domains = ['www.hepsiburada.com']
    start_urls = ['http://www.hepsiburada.com/iphone-11-64-gb-pm-HB00000NSBZ4']

    def parse(self, response):
        for product in response.xpath("//a[@class='hb-recommendation-product-url']"):
            yield {
                'url':  response.urljoin(product.xpath(".//text()").get())
            }





