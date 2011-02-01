# -*-coding:utf-8-*-
# 解析美团网
#

import datetime

import spider_base
from spider_base import StateBase
from spider_base import SpiderBase
#from spider_base import CitySpiderBase
from spider_base import get_attr
import re


class StateInitial(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'id')
        if c == 'index-deals':
            print "index-deals"
            self.change_state(self.context.state_div_goods)
        elif c == 'deal-default':
            print "deal-default"
            self.change_state(self.context.state_default_goods)

class StateDivGoods(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        print "class: " + c
        if c == 'sidebar':
            print "sidebar"
            self.change_state(self.context.state_end)
        elif c == 'item' or c == 'item odd':
            print "item"
            self.change_state(self.context.state_a_title)
        elif c == 'primary cf':
            print "primary cf"
            self.change_state(self.context.state_primary_a_title)

class StatePrimaryH1Title(StateBase):
    def start_h1(self, attrs):
        print "h1"
        self.change_state(self.context.state_primary_a_title)
        
class StatePrimaryATitle(StateBase):
    def start_a(self, attrs):
        print "a"
        href=get_attr(attrs, 'href')
        self.context.add_url(href)
        self.change_state(self.context.state_primary_data_title)

class StatePrimaryDataTitle(StateBase):
    def handle_data(self, data):
        title=data.strip()
        print title
        self.context.add_title(title)
        self.change_state(self.context.state_primary_p_price)

class StatePrimaryPPrice(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='deal-price' :
            print "p-class: " + c
            self.change_state(self.context.state_primary_price)

class StatePrimaryStrongPrice(StateBase):
    "unused"
    def start_strong(self, attrs):
        self.change_state(self.context.state_primary_price)

class StatePrimaryPrice(StateBase):
    def handle_data(self, data):
        price=data.strip()[3:]
        print "price: " + price
        self.context.add_price(price)
        self.change_state(self.context.state_primary_del_value)

class StatePrimaryTableValue(StateBase):
    "unused"
    def start_table(self, attrs):
        c=get_attr(attrs, 'class')
        print "table_value " + c
        if c == 'discount':
            print "table_value " + c
            self.change_state(self.context.state_primary_tr_value)
    def start_tr(self, attrs):
        print "table_value " + c
        self.change_state(self.context.state_primary_tr_value)

class StatePrimaryTrValue(StateBase):
    "unused"
    def start_tr(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='number':
            print "number"
            self.change_state(self.context.state_primary_del_value)

class StatePrimaryDelValue(StateBase):
    def start_del(self, attrs):
        self.change_state(self.context.state_primary_value)

class StatePrimaryValue(StateBase):
    def handle_data(self, data):
        value=data.strip()[3:]
        print "value: " + value
        self.context.add_value(value)
        self.change_state(self.context.state_primary_p_bought)

class StatePrimaryPBought(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'deal-buy-tip-top':
            print c
            self.change_state(self.context.state_primary_bought)

class StatePrimaryStrongBought(StateBase):
    "unused"
    def start_strong(self, attrs):
        self.change_state(self.context.state_primary_bought)

class StatePrimaryBought(StateBase):
    def handle_data(self, data):
        bought=data.strip()
        print "bought: " + bought
        self.context.add_bought(bought)
        self.change_state(self.context.state_primary_div_time_left)

class StatePrimaryDivTimeLeft(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class').split(' ')
        if 'deal-timeleft' in c:
            timeleft=get_attr(attrs, 'diff')
            self.context.add_timeleft(timeleft)
            self.change_state(self.context.state_primary_div_image)

class StatePrimaryDivImage(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'cover' :
            self.change_state(self.context.state_primary_image)
    
class StatePrimaryImage(StateBase):
    def start_img(self, attrs):
        img=get_attr(attrs, 'src')
        self.context.add_image(img)
        self.change_state(self.context.state_div_goods)
    

class StateH1Title(StateBase):
    def start_h1(self, attrs):
        self.change_state(self.context.state_a_title)
        
class StateATitle(StateBase):
    def start_a(self, attrs):
        href=get_attr(attrs, 'href')
        self.context.add_url(href)
        self.change_state(self.context.state_data_title)

class StateDataTitle(StateBase):
    def handle_data(self, data):
        title=data.strip()
        self.context.add_title(title)
        self.change_state(self.context.state_div_image)

class StateDivImage(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'cover' :
            print c
            self.change_state(self.context.state_image)
    
class StateImage(StateBase):
    def start_img(self, attrs):
        img=get_attr(attrs, 'src')
        self.context.add_image(img)
        self.change_state(self.context.state_p_price)

class StatePPrice(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='deal-price' :
            self.change_state(self.context.state_strong_price)

class StateStrongPrice(StateBase):
    def start_strong(self, attrs):
        self.change_state(self.context.state_price)

class StatePrice(StateBase):
    def handle_data(self, data):
        price=data.strip()[3:]
        self.context.add_price(price)
        self.change_state(self.context.state_table_value)

class StateTableValue(StateBase):
    def start_Table(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'discount':
            self.change_state(self.context.state_del_value)

class StateDelValue(StateBase):
    def start_del(self, attrs):
        self.change_state(self.context.state_value)

class StateValue(StateBase):
    def handle_data(self, data):
        value=data.strip()[3:]
        self.context.add_value(value)
        self.change_state(self.context.state_div_time_left)

class StateDivTimeLeft(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class').split(' ')
        if 'deal-timeleft' in c:
            timeleft=get_attr(attrs, 'diff')
            self.context.add_timeleft(timeleft)
            self.change_state(self.context.state_p_bought)

class StatePBought(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'deal-buy-tip-top':
            self.change_state(self.context.state_strong_bought)

class StateStrongBought(StateBase):
    def start_p(self, attrs):
        self.change_state(self.context.state_bought)

class StateBought(StateBase):
    def handle_data(self, data):
        bought=data.strip()
        self.context.add_bought(bought)
        self.change_state(self.context.state_div_goods)

class StateEnd(StateBase):
    pass

class StateDefaultGoods(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        cid=get_attr(attrs, 'id')
        if c == 'cf' and cid == 'deal-intro':
            self.change_state(self.context.state_default_a_title)

class StateDefaultH1Title(StateBase):
    def start_h1(self, attrs):
        self.change_state(self.context.state_default_a_title)
        
class StateDefaultATitle(StateBase):
    def start_a(self, attrs):
        href=get_attr(attrs, 'href')
        self.context.add_url(href)
        self.change_state(self.context.state_default_data_title_prefix)

class StateDefaultDataTitlePrefix(StateBase):
    def handle_data(self, data):
        self.change_state(self.context.state_default_data_title)

class StateDefaultDataTitle(StateBase):
    def handle_data(self, data):
        title=data.strip()
        self.context.add_title(title)
        self.change_state(self.context.state_default_p_price)

class StateDefaultPPrice(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='deal-price' :
            self.change_state(self.context.state_default_strong_price)

class StateDefaultStrongPrice(StateBase):
    def start_strong(self, attrs):
        self.change_state(self.context.state_default_price)

class StateDefaultPrice(StateBase):
    def handle_data(self, data):
        price=data.strip()[3:]
        self.context.add_price(price)
        self.change_state(self.context.state_default_table_value)

class StateDefaultTableValue(StateBase):
    def start_Table(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'deal-discount':
            self.change_state(self.context.state_default_td_value)

class StateDefaultTdValue(StateBase):
    def start_td(self, attrs):
        self.change_state(self.context.state_default_del_value)

class StateDefaultDelValue(StateBase):
    def start_del(self, attrs):
        self.change_state(self.context.state_default_value)

class StateDefaultValue(StateBase):
    def handle_data(self, data):
        value=data.strip()[3:]
        self.context.add_value(value)
        self.change_state(self.context.state_default_div_time_left)

class StateDefaultDivTimeLeft(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class').split(' ')
        if 'deal-timeleft' in c:
            timeleft=get_attr(attrs, 'diff')
            self.context.add_timeleft(timeleft)
            self.change_state(self.context.state_default_p_bought)

class StateDefaultPBought(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'deal-buy-tip-top':
            self.change_state(self.context.state_default_strong_bought)

class StateDefaultStrongBought(StateBase):
    def start_strong(self, attrs):
        self.change_state(self.context.state_default_bought)

class StateDefaultBought(StateBase):
    def handle_data(self, data):
        bought=data.strip()
        self.context.add_bought(bought)
        self.change_state(self.context.state_default_div_img)

class StateDefaultDivImage(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'deal-buy-cover-img' :
            self.change_state(self.context.state_default_image)
    
class StateDefaultImage(StateBase):
    def start_img(self, attrs):
        img=get_attr(attrs, 'src')
        self.context.add_image(img)
        self.change_state(self.context.state_end)



class SpiderMeituan(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)
        self.state_initial=StateInitial(self)
        self.state_div_goods=StateDivGoods(self)
        self.state_h1_title=StateH1Title(self)
        self.state_a_title=StateATitle(self)
        self.state_data_title=StateDataTitle(self)
        self.state_div_image=StateDivImage(self)
        self.state_image=StateImage(self)
        self.state_p_price=StatePPrice(self)
        self.state_strong_price=StateStrongPrice(self)
        self.state_price=StatePrice(self)
        self.state_table_value=StateTableValue(self)
        self.state_del_value=StateDelValue(self)
        self.state_value=StateValue(self)
        self.state_div_time_left=StateDivTimeLeft(self)
        self.state_p_bought=StatePBought(self)
        self.state_strong_bought=StateStrongBought(self)
        self.state_bought=StateBought(self)
        
        self.state_primary_h1_title=StatePrimaryH1Title(self)
        self.state_primary_a_title=StatePrimaryATitle(self)
        self.state_primary_data_title=StatePrimaryDataTitle(self)
        self.state_primary_p_price=StatePrimaryPPrice(self)
        self.state_primary_strong_price=StatePrimaryStrongPrice(self)
        self.state_primary_price=StatePrimaryPrice(self)
        self.state_primary_table_value=StatePrimaryTableValue(self)
        self.state_primary_tr_value=StatePrimaryTrValue(self)
        self.state_primary_del_value=StatePrimaryDelValue(self)
        self.state_primary_value=StatePrimaryValue(self)
        self.state_primary_p_bought=StatePrimaryPBought(self)
        self.state_primary_strong_bought=StatePrimaryStrongBought(self)
        self.state_primary_bought=StatePrimaryBought(self)
        self.state_primary_div_time_left=StatePrimaryDivTimeLeft(self)
        self.state_primary_div_image=StatePrimaryDivImage(self)
        self.state_primary_image=StatePrimaryImage(self)
        
        self.state_default_goods=StateDefaultGoods(self)
        self.state_default_h1_title=StateDefaultH1Title(self)
        self.state_default_a_title=StateDefaultATitle(self)
        self.state_default_data_title_prefix=StateDefaultDataTitlePrefix(self)
        self.state_default_data_title=StateDefaultDataTitle(self)
        self.state_default_p_price=StateDefaultPPrice(self)
        self.state_default_strong_price=StateDefaultStrongPrice(self)
        self.state_default_price=StateDefaultPrice(self)
        self.state_default_table_value=StateDefaultTableValue(self)
        self.state_default_td_value=StateDefaultTdValue(self)
        self.state_default_del_value=StateDefaultDelValue(self)
        self.state_default_value=StateDefaultValue(self)
        self.state_default_div_time_left=StateDefaultDivTimeLeft(self)
        self.state_default_p_bought=StateDefaultPBought(self)
        self.state_default_strong_bought=StateDefaultStrongBought(self)
        self.state_default_bought=StateDefaultBought(self)
        self.state_default_div_image=StateDefaultDivImage(self)
        self.state_default_image=StateDefaultImage(self)
        
        self.state_end=StateEnd(self)
        self.state=self.state_initial


def test_spider():
    import urllib
    urls = ['http://bj.meituan.com/',
#            'http://sz.meituan.com/',
#            'http://sh.meituan.com/',
#            'http://gz.meituan.com/',
#            'http://cd.meituan.com/',
#            'http://km.meituan.com/'
            ]
    for url in urls:
        usock = urllib.urlopen(url)
        data = usock.read()
        usock.close()
        spider = SpiderMeituan()
        spider.feed(data)
        spider.close()
        print url
        print spider

def main():
    test_spider()

if __name__ == '__main__':
    main()

