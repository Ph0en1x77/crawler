from pyquery import PyQuery as pq

def parse_ishashouse(html):
    doc = pq(html)
    return doc('.no_more_house_download').text()

def parse_houseinfo(region,html):
    doc = pq(html)
    for item in doc('.item_list').items():
        return(region,
              item('.item_main').text(),
              item('.item_other').text().split('/')[0],
              item('.item_other').text().split('/')[1],
              item('.price_total').text(),
              item('.unit_price').text(),
              item('.subway_house').text(),
              item('.vr').text(),
              item('.five').text(),
              item('.haskey').text()
              )