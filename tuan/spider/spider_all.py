# -*-coding:utf-8-*-

import spider_list
import spider_qqtuan
import spider_lashou

SpiderAll = [
    ['QQ团', spider_qqtuan.claw, spider_list.QQTuanList],
    ['拉手网', spider_lashou.claw, spider_list.LashouList]
    ];

def claw():
    for site, spider, webs in SpiderAll:
#        print "Claw site <{0}>".format(site)
        spider(webs)

if __name__ == '__main__':
    claw()

