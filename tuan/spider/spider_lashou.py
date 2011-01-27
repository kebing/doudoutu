# -*-coding:utf-8-*-
# 解析拉手网的代码
#

import datetime

import spider_base
from spider_base import StateBase
from spider_base import SpiderBase
from spider_base import get_attr

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
        #if href[0:27]=='http://www.lashou.com/deal/':
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
        price=data.strip()[3:]
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
        self.change_state(self.context.state_initial)


class SpiderLashou(SpiderBase):
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
        self.state=self.state_initial


def claw(webs):
    spider_base.claw(SpiderLashou, webs)


def test_spider():
    LashouList = [
        ['拉手网', 'shenzhen', 'http://www.lashou.com/shenzhen'],
        ['拉手网', 'chengdu', 'http://www.lashou.com/chengdu'],
        ['拉手网', 'beijing', 'http://www.lashou.com/beijing'],
        ['拉手网', 'shanghai', 'http://www.lashou.com/shanghai']
        ];

    dt=datetime.datetime.now().strftime('%Y-%m-%d')

    for site,city,site_url in LashouList:
        print '<' + city + '>:'
        s=SpiderLashou()
        spider_base.fetch_and_parse(s, site_url)
        spider_base.print_result(s, site, city, dt, site_url)

def main():
    test_spider()

if __name__ == '__main__':
    main()

