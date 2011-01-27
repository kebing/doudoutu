# -*-coding:utf-8-*-
# 解析QQ团的代码
# 

import re

import spider_base
from spider_base import StateBase
from spider_base import SpiderBase
from spider_base import get_attr

class StateInitial(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'basic_buy_group':
            self.change_state(self.context.state_div_basic)

class StateDivBasicBuyGroup(StateBase):
    def start_div(self, attrs):
        c=get_attr(attrs, 'class')
        if c == 'attribute':
            self.change_state(self.context.state_value)

class StateValue(StateBase):
    def enter(self):
        self.state=0

    def exit(self):
        self.state=0

    def start_p(self, attrs):
        if self.state==0:
            c=get_attr(attrs, 'class')
            if c=='primary_price':
                self.state=1
        
    def start_del(self, attrs):
        if self.state==1:
            self.state=2

    def handle_data(self, data):
        if self.state==2:
            #print "value: " + data
            self.context.add_value(data)
            self.state=0
            self.change_state(self.context.state_price)

class StatePrice(StateBase):
    def enter(self):
        self.state=0

    def exit(self):
        self.state=0

    def start_p(self, attrs):
        if self.state==0:
            c=get_attr(attrs, 'class')
            if c=='current_price':
                self.state=1
        
    def start_span(self, attrs):
        if self.state==1:
            self.state=2

    def handle_data(self, data):
        if self.state==2:
            #print "price: " + data
            self.context.add_price(data)
            self.state=0
            self.change_state(self.context.state_photo_and_title)

class StatePhotoAndTitle(StateBase):
    def enter(self):
        self.state=0

    def exit(self):
        self.state=0

    def start_div(self, attrs):
        if self.state==0:
            c=get_attr(attrs, 'class')
            if c=='photo':
                self.state=1
        
    def start_img(self, attrs):
        if self.state==1:
            img=get_attr(attrs,'src')
            title=get_attr(attrs,'alt')
            if img != '' and title!='':
                #print "img: " + img
                #print "title: " + title
                self.context.add_image(img)
                self.context.add_title(title)
                self.state=0
                self.change_state(self.context.state_url)


class StateUrl(StateBase):
    def enter(self):
        self.state=0

    def exit(self):
        self.state=0

    def start_div(self, attrs):
        if self.state==0:
            c=get_attr(attrs, 'class')
            if c=='mod_wrap_v2 share_to_somebody':
                self.state=1
        
    def start_a(self, attrs):
        if self.state==1:
            onclick=get_attr(attrs,'onclick')
            if onclick != '':
                url='http://tuan.qq.com/' + re.sub(r'\?us=smsg.*$', '', re.sub(r'(^.*http://tuan.qq.com/)', '', onclick))
                #print "url: " + url
                self.context.add_url(url)
                self.state=0
                self.change_state(self.context.state_initial)

class SpiderQQTuan(SpiderBase):
    def __init__(self):
        SpiderBase.__init__(self)
        self.state_initial=StateInitial(self)
        self.state_div_basic=StateDivBasicBuyGroup(self)
        self.state_value=StateValue(self)
        self.state_price=StatePrice(self)
        self.state_photo_and_title=StatePhotoAndTitle(self)
        self.state_url=StateUrl(self)
        self.state=self.state_initial

def claw(webs):
    spider_base.claw(SpiderQQTuan, webs)

def test_spider():
    QQTuanList = [
        ['QQ团', 'shenzhen', 'http://tuan.qq.com/shenzhen'],
        ['QQ团', 'shanghai', 'http://tuan.qq.com/shanghai'],
        ['QQ团', 'beijing', 'http://tuan.qq.com/beijing'],
        ['QQ团', 'chongqing', 'http://tuan.qq.com/chongqing'],
        ['QQ团', 'guangzhou', 'http://tuan.qq.com/guangzhou'],
        ['QQ团', 'chengdu', 'http://tuan.qq.com/chengdu'],
        ['QQ团', 'fuzhou', 'http://tuan.qq.com/fuzhou']
        ]
    claw(QQTuanList)


def main():
    test_spider()

if __name__ == '__main__':
    main()

