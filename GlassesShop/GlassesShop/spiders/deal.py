import scrapy
import logging


class DealSpider(scrapy.Spider):
    name = 'deal'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for product in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            yield {
                'url': product.xpath(".//div/a/@href").get(),
                'img_url': product.xpath(".//div/a/img[1]/@src").get(),
                'name': product.xpath("normalize-space(.//div[@class='p-title-block']/div[2]/div/div/div/a/text())").get(),
                'price': product.xpath(".//div[@class='p-title-block']/div[2]/div/div[2]/div/div/span/text()").get(),
            }

        next_page = response.xpath("//a[@rel='next']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

