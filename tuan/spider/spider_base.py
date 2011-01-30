# -*-coding:utf-8-*-

from sgmllib import SGMLParser
import urllib
import datetime


    
def get_attr(attrs, name):
    v=[v for k,v in attrs if k==name]
    if len(v)==1:
        return v[0]
    else:
        return ''

    
def print_result(spider, site, city, dt, site_url, rank):
    for url, title, price, value, image in zip(spider.urls, spider.titles, spider.prices, spider.values, spider.images):
        s='{0}, "{1}", {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}'
        print s.format(url, title.replace('"', '""'), price, value, site, city, dt, image, site_url, rank)



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

    def add_timeleft(self, timeleft):
        self.timeleft.append(timeleft)

    def add_bought(self, bought):
        self.bought.append(bought)

    def add_ison(self, ison):
        self.bought.ison(ison)

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
        for url, title, price, value, image, timeleft in self.zip_info():
            s='{0}, {1}, {2}, {3}, {4}, {5}\n'
            result += s.format(url, title, price, value, image, timeleft)
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
            s='{0}, {1}, {2}, {3}\n'
            result += s.format(self.site, city, name.encode('utf-8'), url)
        return result

