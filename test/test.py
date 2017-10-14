from .src.selfspider import spider

url = "http://baidu.com"
spider = spider(url)
spider.addBeforeHooks()
spider.run()