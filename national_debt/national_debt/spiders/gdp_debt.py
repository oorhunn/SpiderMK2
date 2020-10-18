import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['www.worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//tr/td")
        for country in countries:
            name = country.xpath(".//text()").get()

            yield {
                'name': name
            }



