import scrapy
from scrapy_splash import SplashRequest


class HephepSpider(scrapy.Spider):
    name = 'hephep'
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
        yield SplashRequest(url="https://www.hepsiburada.com", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        print(response.body)





