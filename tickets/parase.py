#! usr/bin/python
# coding: utf-8

# import re
# from pprint import pprint

# with open("station.rtf", 'r') as f:
# 	text = f.read()
# 	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)#\u4e00-\u9fa5所有汉字的unicode表示范围
# 	pprint(dict(stations), indent=4)
import re
from pprint import pprint


with open('station.html', 'r') as f:
    text = f.read()
    reObject = re.compile('([\u4e00-\u9fa5]+)\|([A-Z]+)')
    stations = reObject.findall(text)  # 正则\w 表示匹配大小写子母以及数字  \s匹配非空白字符
    pprint(dict(stations), indent=4)  # 缩进4

    # print(text)


