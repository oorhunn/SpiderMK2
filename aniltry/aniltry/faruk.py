import requests

headers = {
    'authority': 'recommendation.hepsiburada.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'origin': 'https://www.hepsiburada.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.hepsiburada.com/iphone-11-64-gb-p-HBV00000NSBZ5',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6',
}

params = (
    ('placements', 'apple-item_page.web-bundle1'),
    ('userId', ''),
    ('__rr_debug', 'false'),
    ('r3_forceDisplay', 'false'),
    ('platformType', '1'),
    ('productId', 'HB00000NSBZ4'),
    ('skuList', 'HBV00000NSBZ5'),
    ('chi', '80651136'),
    ('anonymousId', '873f890e-93f1-4c93-fca8-88393d588eef'),
    ('isRTP', 'false'),
)

response = requests.get('https://recommendation.hepsiburada.com/api/v1/recommendations/withproductinfo', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://recommendation.hepsiburada.com/api/v1/recommendations/withproductinfo?placements=apple-item_page.web-bundle1&userId=&__rr_debug=false&r3_forceDisplay=false&platformType=1&productId=HB00000NSBZ4&skuList=HBV00000NSBZ5&chi=80651136&anonymousId=873f890e-93f1-4c93-fca8-88393d588eef&isRTP=false', headers=headers)

print(response.content)