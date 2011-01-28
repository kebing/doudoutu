# -*-coding:utf-8-*-

import spider_lashou

site_spider_map = {
    #  site  :    deal spider             |   city spider
    'lashou' : [spider_lashou.SpiderLashou,
                spider_lashou.CitySpiderLashou],
    }

class SpiderFactory:
    def new_deal_spider(self, site):
        return site_spider_map[site][0]()
    
    def new_city_spider(self, site):
        return site_spider_map[site][1]()
    

if __name__ == '__main__':
    pass

