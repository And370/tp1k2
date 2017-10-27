tag='小说'                  
                
                
                
                


from scrapy.http import Request
import scrapy
from tp1k2.items import Tp1k2Item
import time
import random
page_num=1
class Tp1k2spider(scrapy.Spider):
    global tag
    
    name = 'tp1k2'
    print('\n\n\n\n这是一只测试爬虫。\n\n\n\n交流AND370yeah@163.com\n\n\n')
    
    start_urls = ['https://book.douban.com/tag/%s'%tag+'?start=0&type=S'
    ]
    
    def parse(self, response):
        global page_num
        
        bk_name=response.xpath("//div[@class='info']//h2[@class]/a/@title").extract()
        
        bk_rating_nums=response.xpath("//div[@class='info']//span[@class='rating_nums']/text()").extract()
        new_rating=[rating.replace('</span>','') for rating in bk_rating_nums]
        
        others=response.xpath("//div[@class='info']//div[@class='pub']/text()").extract()
        new_others=[other.replace(' ','').replace('\n','') for other in others]
        
        bk_rater_nums=response.xpath("//div[@class='info']//span[@class='pl']/text()").extract()
        new_rater=[rater.replace(' ','').replace('\n','').replace('</span>','').replace('(','').replace('人评价)','') for rater in bk_rater_nums]
        
        bk_url=response.xpath("//div[@class='info']/h2[@class]/a/@href").extract()
        bk_image_url=response.xpath("//div[@class='pic']/a/img/@src").extract()
        next=response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract_first()
        
        item=Tp1k2Item()
        item['bk_name']=bk_name
        item['others']=new_others
        item['bk_rating_nums']=new_rating
        item['bk_rater_nums']=new_rater
        
        item['bk_url']=bk_url
        item['bk_image_url']=bk_image_url
        
        yield item
        sleep_time=random.uniform(0.2,0.7)
        
        print('\n\n第%d页：'%page_num)
        
        while next and page_num<50:
            
            #nums=(page_num-1)*20
            #next_page =('https://book.douban.com/tag/%s?start='%tag+'%d&type=S'%nums)
            page_num=page_num+1
            next_page='https://book.douban.com'+next
            print('next_page:\n'+next_page)
            next=None
            time.sleep(sleep_time)
            yield scrapy.Request(next_page,callback=self.parse)
        