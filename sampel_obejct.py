
from icrawler.builtin import BingImageCrawler                  
classes=['speaker']
number=2000
for c in classes:
    google_crawler=BingImageCrawler         (storage={'root_dir':'speaker'}) 
    google_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)          