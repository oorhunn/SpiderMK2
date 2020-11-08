# -*- coding: utf-8 -*-

# Scrapy settings for livecoin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'faruk'

SPIDER_MODULES = ['work.spiders']
NEWSPIDER_MODULE = 'work.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'livecoin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
        'Referer': 'https://www.hepsiburada.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'authority': 'px.moatads.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://387f833e90529a9e295520bb35396142.safeframe.googlesyndication.com/',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6',
    'if-none-match': 'W/^\\^8360eb270b919a1fb4776bc448d9ed14^\\^',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Origin': 'https://www.hepsiburada.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6',
    'x-client-data': 'CIW2yQEIpLbJAQjEtskBCKmdygEIxLjKAQisx8oBCPbHygEI6cjKAQity8oBCLTLygEIgc/KAQjc1coBCJeaywEYisHKAQ==',
    'cookie': 'RUL=ENO88PwFGNOj9YsGIi8BNmGQ45laxS3fQ4NC4qaV6K41fJIChLF6qVvh-IVuPBbYY83Hwh3ZSQY517DZiQ^|cs=AP6Md-Ur43M6MpUeKtSu-lnJafkb; DSID=AAO-7r42UCEY-oLFpl_2RWzZI4t6wWc6WfPVDgpGTCNZMbFvfy4fr_sDzhpHvCEpBkiuS985myHLmfV1Y4GCCgRs5iomB1p1fNz8EKh0l2HGbvXWDfZL9hM; IDE=AHWqTUnbHy1L5sJZLJLwNOACZ5ARxnLfxJ2sMZpa7dm4SM61UY1qCG8CLf5v427u',
    'if-modified-since': 'Mon, 19 Mar 2018 17:30:33 GMT',
    'If-None-Match': 'W/^\\^25fe0d189653038bad2f1220d93a3495^\\^',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://www.hepsiburada.com',
    'If-Modified-Since': 'Wed, 04 Nov 2020 11:37:22 GMT',
    'access-control-request-method': 'POST',
    'access-control-request-headers': 'content-type,x-braze-api-key,x-braze-contentcardsrequest,x-braze-datarequest,x-requested-with',
    'x-braze-api-key': 'a19ee87d-6625-49ed-ad8c-f427b0067dec',
    'x-braze-triggersrequest': 'true',
    'x-requested-with': 'XMLHttpRequest',
    'x-braze-datarequest': 'true',
    'x-braze-contentcardsrequest': 'true',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Content-Length': '0',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'livecoin.pipelines.LivecoinPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


SPLASH_URL = 'http://localhost:8050'

FEED_EXPORT_ENCODING = 'utf-8'
