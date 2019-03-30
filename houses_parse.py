from pyquery import PyQuery as pq
import re
import pymysql

def parse_ishashouse(html):
    doc = pq(html)
    return doc('.no_more_house_download').text()

def parse_houseinfo(city_region,region,html):
    doc = pq(html)
    con = pymysql.connect(host="localhost", user='root', password='123456', port=3306, database='crawler')
    cursor = con.cursor()
    for item in doc('.item_list').items():
        houses_info = ("'" + city_region +"'",
               "'" + region +"'",
               "'" + item('.item_main').text() +"'",
               "'" + item('.item_other').text().split('/')[0] +"'",
               re.match('([0-9]+\.?[0-9]+)', item('.item_other').text().split('/')[1]).group(),
               str(int(float(re.match('([0-9]+\.?[0-9]+)', item('.price_total').text()).group()) * 10000)),
               re.match('([0-9]+\.?[0-9]+)', item('.unit_price').text()).group(),
               "'" + item('.subway_house').text() +"'",
               "'" + item('.vr').text() +"'",
               "'" + item('.five').text() +"'",
               "'" + item('.haskey').text() +"'")
        print(houses_info)
        sql = 'insert into house_info values' + ' (' + ','.join(houses_info) + ')'
        try:
         cursor.execute(sql)
         con.commit()
        except:
            con.rollback()
    con.close()