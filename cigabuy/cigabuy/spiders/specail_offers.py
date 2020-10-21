import scrapy


class SpecailOffersSpider(scrapy.Spider):
    name = 'specail_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/weekly-deals-c-56_187.html']

    def parse(self, response):
        for product in response.xpath("//div[@class='p_box_wrapper']"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discounted_price': product.xpath(".//div[@class='p_box_price cf']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price cf']/span[2]/text()").get()
            }
#this part for scraping the next page but robots of the site forbid it and right now i do not know the solution
        # next_page = response.xpath("//a[@class='nextPage']/@href").get()
        #
        # if next_page:
        #     yield scrapy.Request(url=next_page, callback=self.parse)



