# -*- coding: utf-8 -*-

import scrapy


class Tp1k2Item(scrapy.Item):
    bk_name=scrapy.Field()
    
    bk_rating_nums=scrapy.Field()
    bk_rater_nums=scrapy.Field()
    
    bk_url=scrapy.Field()
    bk_image_url=scrapy.Field()
    others=scrapy.Field()
    image_paths=scrapy.Field()
'''    


*小说(4758050)	*外国文学(1678096)	*文学(1303917)	*随笔(1022084)

'''