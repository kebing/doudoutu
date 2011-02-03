# -*-coding:utf-8-*-

from sgmllib import SGMLParser
import urllib
import datetime
import logging

    
def get_attr(attrs, name):
    v=[v for k,v in attrs if k==name]
    if len(v)==1:
        return v[0]
    else:
        return ''
    
def print_result(spider, site, city, dt, site_url, rank):
    for url, title, price, value, image in zip(spider.urls, spider.titles, spider.prices, spider.values, spider.images):
        s='%(0), "%(1)", %(2), %(3), %(4), %(5), %(6), %(7), %(8), %(9)'
        print s % {'0':url, '1':title.encode('utf-8'), '2':price, '3':value, '4':site, '5':city, '6':dt, '7':image, '8':site_url, '9':rank}

class StateBase():
    logger = logging.getLogger('tuan.spider.StateBase')
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
    def start_h1(self, attrs):
        return
    def start_h2(self, attrs):
        return
    def start_h3(self, attrs):
        return
    def start_h4(self, attrs):
        return
    def start_h5(self, attrs):
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
    def start_table(self, attrs):
        return
    def start_tr(self, attrs):
        return
    def start_td(self, attrs):
        return
    def start_th(self, attrs):
        return
    def start_li(self, attrs):
        return
    def start_ul(self, attrs):
        return
    def start_dd(self, attrs):
        return
    def start_strong(self, attrs):
        return

class SpiderBase(SGMLParser):
    logger = logging.getLogger('tuan.spider.SpiderBase')
    def __init__(self):
        SGMLParser.__init__(self)
        self.urls=[]
        self.values=[]
        self.prices=[]
        self.titles=[]
        self.images=[]
        self.timeleft=[]
        self.bought=[]
        self.ison=[]
        self.state=StateBase(self)
    def zip_info(self):
        return zip(self.urls, self.values, self.prices, self.titles, self.images, self.timeleft)
    def add_url(self, url):
        self.logger.debug('add_url:'+ url)
        self.urls.append(url)
    def add_title(self, title):
        self.logger.debug('add_title:'+ title)
        self.titles.append(title)
    def add_price(self, price):
        self.logger.debug('add_price:'+ price)
        self.prices.append(price)
    def add_value(self, value):
        self.logger.debug('add_value:'+ value)
        self.values.append(value)
    def add_image(self, image):
        self.logger.debug('add_image:'+ image)
        self.images.append(image)
    def add_timeleft(self, timeleft):
        self.logger.debug('add_timeleft:'+ timeleft)
        self.timeleft.append(timeleft)
    def add_bought(self, bought):
        self.logger.debug('add_bought:'+ bought)
        self.bought.append(bought)
    def add_ison(self, ison):
        self.logger.debug('add_ison:'+ ison)
        self.bought.ison(ison)
    def change_state(self, new_state):
        self.state.exit()
        self.state=new_state
        self.state.enter()
    def start_div(self, attrs):
        self.state.start_div(attrs)
    def handle_data(self, data):
        self.state.handle_data(data)
    def start_h1(self, attrs):
        self.state.start_h1(attrs)
    def start_h2(self, attrs):
        self.state.start_h2(attrs)
    def start_h3(self, attrs):
        self.state.start_h3(attrs)
    def start_h4(self, attrs):
        self.state.start_h4(attrs)
    def start_h5(self, attrs):
        self.state.start_h5(attrs)
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
    def start_table(self, attrs):
        self.state.start_table(attrs)
    def start_tr(self, attrs):
        self.state.start_tr(attrs)
    def start_td(self, attrs):
        self.state.start_td(attrs)
    def start_th(self, attrs):
        self.state.start_th(attrs)
    def start_li(self, attrs):
        self.state.start_li(attrs)
    def start_ul(self, attrs):
        self.state.start_ul(attrs)
    def start_dd(self, attrs):
        self.state.start_dd(attrs)
    def start_strong(self, attrs):
        self.state.start_strong(attrs)

    def __str__(self):
        result=''
        for url, value, price, title, image, timeleft in self.zip_info():
            result += '%(url)s %(value)s %(price)s %(title)s %(image)s %(timeleft)s\n' % {
                'url':url, 'value':value, 'price':price,
                'title':title, 'image':image,
                'timeleft':timeleft,
                }
        return result



class CitySpiderBase(SGMLParser):
    def __init__(self, site):
        SGMLParser.__init__(self)
        self.site=site
        self.city=[]
        self.name=[]
        self.url=[]
        self.state=StateBase(self)
        
    def zip_info(self):
        return zip(self.city, self.name, self.url)
    
    def add_city(self, city):
        self.city.append(city)
        
    def add_name(self, name):
        self.name.append(name)
        
    def add_url(self, url):
        self.url.append(url)
        
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
        for city, name, url in self.zip_info():
            result += '%(site)s %(city)s %(name)s %(url)s\n' % {
                'site':self.site, 'city':city,
                'name':name, 'url':url,
                }
        return result

