tag='小说'                  
                
                
                
                
import json
import codecs
import time
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from tp1k2.items import Tp1k2Item

class Tp1k2ImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        #print('本————大————王————开始请求了!!!!!!!!!!!!!!!!!')
        for image_url in item['bk_image_url']:
            yield Request(image_url)
        #print('本————大————王————开始存图了!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
    def item_completed(self,results,item,info):
        image_paths=[x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem('图片未下载好%s'%image_paths)
        item['image_paths']=image_paths
        #print('正在保存图片!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return item
page_num=1
class Tp1k2Pipeline(object):
    def open_spider(self,spider):
        global tag
        self.file = codecs.open('%s_book1k.json'%tag, 'a', encoding='utf-8')#2.在这里修改文件名
        
    def process_item(self, item, spider):
        global page_num
        line=('\n第%d页:'%page_num+'\n')
        for i in range(len(item['bk_name'])):
            '''
            bk_name={'bk_name':item['bk_name'][i]}
            bk_rating_nums={'bk_rating_nums':item['bk_rating_nums'][i]}
            bk_rater_nums={'bk_rater_nums':item['bk_rater_nums'][i]}
            bk_url={'bk_url':item['bk_url'][i]}
            line=line+json.dumps(bk_name,ensure_ascii=False)+'\t\t\t'
            line=line+json.dumps(bk_rating_nums,ensure_ascii=False)+'\t\t\t'
            line=line+json.dumps(bk_rater_nums,ensure_ascii=False)+'\t\t\t'
            line=line+json.dumps(bk_url,ensure_ascii=False)+'\n'
            '''
            form={'bk_name':item['bk_name'][i],'others':item['others'][i],'bk_rating_nums':item['bk_rating_nums'][i],'bk_rater_nums':item['bk_rater_nums'][i],'bk_url':item['bk_url'][i]}
            
            line=line+json.dumps(form,ensure_ascii=False)+'\n'

        self.file.write(line)
        
        page_num=page_num+1
        
        return item

    def closed_spider(self, spider):
        self.file.close()