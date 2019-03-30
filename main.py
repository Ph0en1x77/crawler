import crawler
import houses_parse
import pymysql
import getregions

if __name__ == '__main__':
    response = crawler.crawler('https://bj.lianjia.com/ershoufang/city?city_id=110000')
    regions_info = getregions.getinfos()
    base_url = 'https://m.lianjia.com/bj/ershoufang/'

    for city_region, city_region_info in regions_info.items():
        for region, url in city_region_info.items():
            i = 1
            while True:
                houses_url = base_url + url + '/pg' + str(i)
                houses_info_response = crawler.crawler(houses_url)
                result = houses_parse.parse_ishashouse(houses_info_response)
                if len(result) != 0:
                    break
                houses_parse.parse_houseinfo(city_region,region,houses_info_response)
                i = i + 1




