# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
# execute("scrapy crawl ZH -a query=funny".split())
# execute(['scrapy', 'crawl', 'ZH'])

execute("scrapy crawl ZH".split())
execute("scrapy crawl buluo_spider".split())




