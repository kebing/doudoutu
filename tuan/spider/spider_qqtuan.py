# -*-coding:utf-8-*-
# 解析QQ团的代码
# 

import re
import logging
from spider_base import *


class StateInitial(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'index_tuan_tit':
            self.change_state(self.context.state_h3_title)

class StateH3Title(StateBase):
    def start_h3(self, attrs):
        self.change_state(self.context.state_span_title)

class StateSpanTitle(StateBase):
    def start_span(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'c_tx4':
            self.change_state(self.context.state_title)

class StateTitle(StateBase):
    def handle_data(self, data):
        title=data.strip()
        self.context.add_title(title)
        self.change_state(self.context.state_div_attr)

class StateDivAttr(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'index_tuan_attr':
            self.change_state(self.context.state_span_price)

class StateSpanPrice(StateBase):
    def start_span(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'num_price':
            self.change_state(self.context.state_price)

class StatePrice(StateBase):
    def handle_data(self, data):
        price=parse_first_float(data.strip())
        self.context.add_price(price)
        self.change_state(self.context.state_p_value)

class StatePValue(StateBase):
    def start_p(self, attrs):
        c=get_attr(attrs, 'class')
        if c=='original_price':
            self.change_state(self.context.state_del_value)

class StateDelValue(StateBase):
    def start_del(self, attrs):
        self.change_state(self.context.state_value)

class StateValue(StateBase):
    def handle_data(self, data):
        value=parse_first_float(data.strip())
        self.context.add_value(value)
        self.change_state(self.context.state_span_bought)

class StateSpanBought(StateBase):
    def start_span(self, attrs):
        if get_attr(attrs, 'class') == 'sellCountter':
            self.change_state(self.context.state_bought)

class StateBought(StateBase):
    def handle_data(self, data):
        bought=parse_first_float(data.strip())
        self.context.add_bought(bought)
        self.change_state(self.context.state_span_lefttime)

class StateLefttime(StateBase):
    def enter(self):
        self.unit=''
        self.hour=0
        self.minute=0
        self.second=0

    def exit(self):
        self.unit=''
        self.hour=0
        self.minute=0
        self.second=0

    def start_span(self, attrs):
        c=get_attr(attrs,'class')
        if c == 'hour_num':
            self.unit='hour'
        elif c == 'minute_num':
            self.unit='minute'
        elif c == 'second_num':
            self.unit='second'
        else:
            self.unit=''
        
    def handle_data(self, data):
        value=parse_first_integer(data)
        if self.unit=='hour':
            self.hour=value
        elif self.unit=='minute':
            self.minute=value
        elif self.unit=='second':
            self.second=value
            lefttime=self.hour*60*60+self.minute*60+self.second
            self.context.add_timeleft(lefttime)
            self.change_state(self.context.state_div_image)
        else:
            "error"

class StateDivImage(StateBase):
    def start_div(self, attrs):
        if get_attr(attrs, 'class')=='index_tuan_photo':
            self.change_state(self.context.state_image)

class StateImage(StateBase):
    def start_img(self, attrs):
        img=get_attr(attrs, 'init_src')
        self.context.add_image(img)
        self.change_state(self.context.state_initial)

class SpiderQQTuan(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)
        self.state_initial=StateInitial(self)
        self.state_h3_title=StateH3Title(self)
        self.state_span_title=StateSpanTitle(self)
        self.state_title=StateTitle(self)
        self.state_div_attr=StateDivAttr(self)
        self.state_span_price=StateSpanPrice(self)
        self.state_price=StatePrice(self)
        self.state_p_value=StatePValue(self)
        self.state_del_value=StateDelValue(self)
        self.state_value=StateValue(self)
        self.state_span_bought=StateSpanBought(self)
        self.state_bought=StateBought(self)
        self.state_lefttime=StateLefttime(self)
        self.state_div_image=StateDivImage(self)
        self.state_image=StateImage(self)
        self.state=self.state_initial

def test_spider():
    import urllib
    urls = [
        'http://tuan.qq.com/shenzhen',
        'http://tuan.qq.com/shanghai',
        'http://tuan.qq.com/beijing',
        'http://tuan.qq.com/chongqing',
        'http://tuan.qq.com/guangzhou',
        'http://tuan.qq.com/chengdu',
        'http://tuan.qq.com/fuzhou',
        ]
    for url in urls:
        usock = urllib.urlopen(url)
        data = usock.read()
        usock.close()
        spider = SpiderQQTuan()
        spider.feed(data)
        spider.close()
        print spider


def main():
    #logging.basicConfig(filename='', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    #logging.basicConfig(level=logging.ERROR)
    test_spider()

if __name__ == '__main__':
    main()

