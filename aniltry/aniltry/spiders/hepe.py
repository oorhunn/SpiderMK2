import scrapy
from scrapy_splash import SplashRequest
import json
import logging


class HepeSpider(scrapy.Spider):
    name = 'hepe'
    allowed_domains = ['www.hepsiburada.com']
    script = '''
            function main(splash, args)
                splash.private_mode_enabled = true
                url = args.url
                assert(splash:go(url))
                assert(splash:wait(1))
                return splash:html()
            end
        '''
    def start_requests(self):
        yield SplashRequest(url="https://www.hepsiburada.com/iphone-11-64-gb-p-HBV00000NSBZ5", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })
        logging.warning("request")

    def parse(self, response):
        logging.warning("parse part")
        yield response.body

