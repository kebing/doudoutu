# -*-coding:utf-8-*-

from sgmllib import SGMLParser
import urllib
import datetime

from google.appengine.ext import db
import models

def store_results(spider, site, city_py, dt, site_city_url, rank):
    rcity=models.get_city_by_py(city_py)
    if rcity is None:
        print "Error: no city " . city_py
        return
    rsitecity=models.get_site_city_info_by_url(site_city_url)
    if rsitecity is None:
        print "Error: no site city " . site_city_url
        return
    rsite=models.get_site_info_by_name(rsitecity.site_name)
    if rsite is None:
        print "Error: no site " . rsitecity.site_name
        return
    date=dt
    for url, title, price, value, image in zip(spider.urls, spider.titles, spider.prices, spider.values, spider.images):
        rdeal=models.get_deal_info_by_url(url)
        if rdeal is None:
            deal=DealInfo()
            deal.deal_url=url
            deal.deal_value=value
            deal.deal_price=price
            deal.deal_title=title
            deal.deal_image_url=image
            deal.deal_date=date
            deal.deal_rank=rsite.site_rank
            deal.site_city_url=site_city_url
            deal.city_py=city_py
            deal.put()
            print "Info: put deal info " . url
        else:
            print "Debug: skip exists deal info " . url

    
def get_attr(attrs, name):
    v=[v for k,v in attrs if k==name]
    if len(v)==1:
        return v[0]
    else:
        return ''

def fetch_and_parse(spider, site_url):
    usock = urllib.urlopen(site_url)
    data=usock.read()
    usock.close()
    spider.feed(data)
    spider.close()
    
def print_result(spider, site, city, dt, site_url, rank):
    for url, title, price, value, image in zip(spider.urls, spider.titles, spider.prices, spider.values, spider.images):
        s='{0}, "{1}", {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'
        print s.format(url, title.replace('"', '""'), price, value, site, city, dt, image, site_url, rank)

def claw(spider, webs):
    dt=datetime.datetime.now().strftime('%Y-%m-%d')
    for site, city, site_url, rank in webs:
        s=spider()
        fetch_and_parse(s, site_url)
        #print_result(s, site, city, dt, site_url, rank)
        store_results(s, site, city, dt, site_url, rank)


class StateBase():
    def __init__(self, context):
        self.context=context

    def change_state(self, new_state):
        self.context.change_state(new_state)

    def enter(self):
        return

    def exit(self):
        return

    def start_div(self, attrs):
        return

    def handle_data(self, data):
        return

    def start_h4(self, attrs):
        return

    def start_p(self, attrs):
        return

    def start_span(self, attrs):
        return

    def start_img(self, attrs):
        return

    def start_del(self, attrs):
        return

    def start_a(self, attrs):
        return


class SpiderBase(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.urls=[]
        self.titles=[]
        self.prices=[]
        self.values=[]
        self.images=[]
        self.state=StateBase(self)

    def add_id(self, id):
        self.ids.append(id)

    def add_url(self, url):
        self.urls.append(url)

    def add_title(self, title):
        self.titles.append(title)

    def add_price(self, price):
        self.prices.append(price)

    def add_value(self, value):
        self.values.append(value)

    def add_image(self, image):
        self.images.append(image)

    def change_state(self, new_state):
        self.state.exit()
        self.state=new_state
        self.state.enter()

    def start_div(self, attrs):
        self.state.start_div(attrs)

    def handle_data(self, data):
        self.state.handle_data(data)

    def start_h4(self, attrs):
        self.state.start_h4(attrs)

    def start_p(self, attrs):
        self.state.start_p(attrs)

    def start_span(self, attrs):
        self.state.start_span(attrs)

    def start_img(self, attrs):
        self.state.start_img(attrs)

    def start_del(self, attrs):
        self.state.start_del(attrs)

    def start_a(self, attrs):
        self.state.start_a(attrs)

    def __str__(self):
        result=''
        for url, title, price, value, image in zip(self.urls, self.titles, self.prices, self.values, self.images):
            s='{0}, {1}, {2}, {3}, {4}'
            result += s.format(url, title, price, value, image)
