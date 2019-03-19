from pyquery import PyQuery as pq

def parse(html):
    doc = pq(html)
    dict = {}
    for item in doc('.level2 li').items():
        if (item.text() != '不限'):
            dict[item.text()] = item('a').attr('href')
    return dict