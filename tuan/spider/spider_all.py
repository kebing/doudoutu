# -*-coding:utf-8-*-

from site_data import *

class SpiderFactory:
    def new_deal_spider(self, site):
        return site_spider_map[site][0]()
#    def new_city_spider(self, site):
#        return site_spider_map[site][1]()
    

if __name__ == '__main__':
    pass

