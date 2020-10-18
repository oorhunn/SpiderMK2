import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            #absoulute_url = f"https://www.worldometers.info{link}"
            #absoulute_url = response.urljoin(link)

            yield response.follow(url=link, callback=self.parse_country)

    def parse_country(self, response):
        logging.info(response.url)

