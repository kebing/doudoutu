# -*-coding:utf-8-*-
# 解析拉手网的代码
#

import logging
import datetime

from spider_base import *
import re


class StateInitial(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'goods':
            self.change_state(self.context.state_div_goods)

class StateDivGoods(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'mid':
            self.change_state(self.context.state_div_mid)

class StateDivMid(StateBase):
    def start_a(self, attrs):
        title=get_attr(attrs, 'title')
        href=get_attr(attrs, 'href')
        self.context.add_title(title)
        self.context.add_url(href)
        self.change_state(self.context.state_div_price)

class StateDivPrice(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='l price' :
            self.change_state(self.context.state_price)

class StatePrice(StateBase):
    def handle_data(self, data):
        price=parse_first_float(data.strip())
        self.context.logger.debug('got price ' + price 
                                  + ' from ' + data.strip())
        self.context.add_price(price)
        self.change_state(self.context.state_h4_value)

class StateH4Value(StateBase):
    def start_h4(self, attrs):
        value=get_attr(attrs, 'title')
        self.context.add_value(value)
        self.change_state(self.context.state_div_image)


class StateDivImage(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'image':
            self.change_state(self.context.state_image)

class StateImage(StateBase):
    def start_img(self, attrs):
        img=get_attr(attrs, 'src')
        self.context.add_image(img)
        self.change_state(self.context.state_div_timeleft)


class StateDivTimeLeft(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'time_left':
            self.change_state(self.context.state_timeleft)

class StateTimeleft(StateBase):
    def handle_data(self, data):
        timeleft=parse_first_integer(data.strip())
        self.context.add_time_end_by_timeleft(timeleft)
        self.change_state(self.context.state_div_bought)

class StateDivBought(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class').split(' ')
        if 'status' in c:
            self.change_state(self.context.state_h6_bought)

class StateH6Bought(StateBase):
    def start_h6(self, attrs):
        self.change_state(self.context.state_bought)

class StateBought(StateBase):
    def handle_data(self, data):
        bought = parse_first_integer(data.strip())
        self.context.logger.debug('got bought ' + bought
                                  + ' from ' + data.strip())
        self.context.add_bought(bought)
        self.change_state(self.context.state_initial)



class SpiderLashou(SpiderBase):
    logger = logging.getLogger('tuan.spider.SpiderLashou')
    def __init__(self):
        SpiderBase.__init__(self)
        self.state_initial=StateInitial(self)
        self.state_div_goods=StateDivGoods(self)
        self.state_div_mid=StateDivMid(self)
        self.state_div_price=StateDivPrice(self)
        self.state_price=StatePrice(self)
        self.state_h4_value=StateH4Value(self)
        self.state_div_image=StateDivImage(self)
        self.state_image=StateImage(self)
        self.state_div_timeleft=StateDivTimeLeft(self)
        self.state_timeleft=StateTimeleft(self)
        self.state_div_bought=StateDivBought(self)
        self.state_h6_bought=StateH6Bought(self)
        self.state_bought=StateBought(self)
        self.state=self.state_initial

class CityStateInitial(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'cityli_center' or c == 'city_zxsn':
            self.change_state(self.context.state_a_city)
            
class CityStateACity(StateBase):
    def start_a(self, attrs):
        href=get_attr(attrs, 'href').strip()
        print href
        if href[0] != '/' or href.find('.') >= 0 or href.find('?') >= 0 or href.find('=') >= 0 or href.find('&') >= 0 or href.find('#') >= 0:
            self.change_state(self.context.state_end)
            return
        city=href[1:].lower()
        url=self.context.url_prefix + href
        print city
        self.context.add_city(city)
        self.context.add_url(url)
        self.change_state(self.context.state_name)
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'g_main' or c == 'goods':
            self.change_state(self.context.state_end)
        
class CityStateName(StateBase):
    def handle_data(self, data):
        name=data.strip()
        print name
        self.context.add_name(unicode(name,'utf-8'))
        self.change_state(self.context.state_a_city)

class CityStateEnd(StateBase):
    pass

class CitySpiderLashou(CitySpiderBase):
    def __init__(self):
        CitySpiderBase.__init__(self, 'lashou')
        self.url_prefix='http://www.lashou.com'
        self.state_initial=CityStateInitial(self)
        self.state_a_city=CityStateACity(self)
        self.state_name=CityStateName(self)
        self.state_end=CityStateEnd(self)
        self.state=self.state_initial


def test_spider():
    import urllib
    urls = [
        'http://www.lashou.com/shenzhen',
        'http://www.lashou.com/chengdu',
        'http://www.lashou.com/beijing',
        'http://www.lashou.com/shanghai',
        ]
    for url in urls:
        spider = SpiderLashou()
        if fetch_and_parse(spider, url):
            print spider
        else:
            print "fetch fail! url = " + url


def main():
    #logging.basicConfig(filename='', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    #logging.basicConfig(level=logging.ERROR)
    test_spider()

if __name__ == '__main__':
    main()

