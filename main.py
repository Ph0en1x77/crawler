import crawler
import regions_parse
import houses_parse
import pymysql

if __name__ == '__main__':
    response = crawler.crawler('https://bj.lianjia.com/ershoufang/city?city_id=110000')
    regions_url = regions_parse.parse(response)
    base_url = 'https://m.lianjia.com'
    con = pymysql.connect(host="localhost",user='root',password='123456',port=3306,database='crawler')
    cursor = con.cursor()
    for key in regions_url:
        i = 1
        while True:
            houses_url = base_url + regions_url[key] + 'pg' + str(i)
            houses_info_response = crawler.crawler(houses_url)
            result = houses_parse.parse_ishashouse(houses_info_response)
            if len(result) != 0:
                break
            houses_info = houses_parse.parse_houseinfo(key,houses_info_response)
            sql = 'insert into house_info values' + ' (' + ','.join(houses_info) +')'
            try:
                cursor.execute(sql)
                con.commit()
            except:
                con.rollback()
            i = i + 1
    con.close()



