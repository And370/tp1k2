#这是个特殊的启动器

import os
import time
import codecs
'''
print(os.name)
print(os.system('scrapy crawl tp1k2'))
'''
tags=['小说']#这里可以放更多你想要的标签
for tag in tags:#利用读写文件来为spider里三个py文件参数做修改
    p=codecs.open('xxx\\pipelines.py','r+',encoding='utf-8')
    p.write("tag=\'%s\'###########################"%tag)#注释符号是为了保证足够长以覆盖比较长的tag
    p.close()
    
    s=codecs.open('xxx\\settings.py','r+',encoding='utf-8')
    s.write("tag=\'%s\'###########################"%tag)
    s.close()

    main=codecs.open('xxx\\tp1k2.py','r+',encoding='utf-8')
    main.write("tag=\'%s\'###########################"%tag)
    main.close()

    print(os.system('scrapy crawl tp1k2'))