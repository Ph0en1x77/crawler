from pyquery import PyQuery as pq
import re

def parse_ishashouse(html):
    doc = pq(html)
    return doc('.no_more_house_download').text()

def parse_houseinfo(region,html):
    doc = pq(html)
    for item in doc('.item_list').items():
        return("'" + region +"'",
               "'" + item('.item_main').text() +"'",
               "'" + item('.item_other').text().split('/')[0] +"'",
               re.match('([0-9]+\.?[0-9]+)', item('.item_other').text().split('/')[1]).group(),
               str(int(float(re.match('([0-9]+\.?[0-9]+)', item('.price_total').text()).group()) * 10000)),
               re.match('([0-9]+\.?[0-9]+)', item('.unit_price').text()).group(),
               "'" + item('.subway_house').text() +"'",
               "'" + item('.vr').text() +"'",
               "'" + item('.five').text() +"'",
               "'" + item('.haskey').text() +"'"
              )