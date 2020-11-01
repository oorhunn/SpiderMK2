import scrapy
from scrapy_splash import SplashRequest

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled = false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(6))
            rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
            rur_tab[5]:mouse_click()
            assert(splash:wait(5))
            splash:set_viewport_full()
            return splash:png()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://www.livecoin.net/en", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        print(response.body)
