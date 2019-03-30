import requests
from urllib.parse import urlencode

def crawler(url, params):
    headers = {
        'Host': 'm.lianjia.com',
        'Referer': 'https://m.lianjia.com/bj/ershoufang/',
        'Uers-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'
    }
    url = url + urlencode(params)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['info'][0]['district']

def getinfos():
    district = {}
    url = 'https://m.lianjia.com/api/dict/city?'
    params = {
        'city_id': 110000
    }
    regions = crawler(url, params)
    for city_region in regions:
        city_region_na = city_region['district_name']
        dict = {}
        for region in city_region['bizcircle']:
            region_name = region['bizcircle_name']
            region_url = region['bizcircle_quanpin']
            dict[region_name] = region_url
        district[city_region_na] = dict
    return district