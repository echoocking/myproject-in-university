# -*-coding: utf-8 -*-

import requests
import cookielib
import re
import time
import os
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request,FormRequest
try:
    from scrapy.selector import Selector
except:
    print '选择器未能正确加载'

try:
    from scrapy.http import HtmlResponse
except:
    print "htmlResponse 未能正确加载"

try:
    from PIL import Image
except:
    pass
import codecs  # 写文件时 写入unicode字符报错 通过此 来转换编码
from scrapy.spiders import Rule  #使用rule时候，不要定义parse方法
from TryToZH.settings import COOKIES
from ..items import TrytozhItem
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
'''
https://www.zhihu.com/topic/19550517/
分析。首先进入topics-->提取data_id-->获取herf='topic/194454'-->获取herf (question/55656)-->获取问题和回答。
所以先了解爬虫的工作流程的写法。再学习xpath 稍加修饰。齐活~~~~
使用小脚本提取出data_id,herf。毕竟比较少。然后将其作为url的集合,交给crawl去爬取。所以问题直接简化为了获取question的url。并且进入url获取问题和回答。
'''

class Login:
    def __init__(self):
        self.agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
        self.header = {
            'Host': 'www.zhihu.com',
            'Referer': 'https://www.zhihu.com/',
            'User-Agent': self.agent
        }

        self.session = requests.session()
        # cookielib类提供操作cookie的一系列方法,提供可存储的cookie对象。
        self.session.cookies = cookielib.LWPCookieJar(filename='cookies')  # CookieJar 类可以捕获cookie 以便在后续需要cookie的时候,可以重新发送。
        # s所以这一句 是将获取的cookie存储在文件名为'cookies'的文件中,并且把cookie的值赋值给session的cookies属性。
        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print 'cookie 未能加载'

    def get_xsrf(self):
        index_url = 'http://www.zhihu.com'
        index_page = self.session.get(index_url, headers=self.header)
        html = index_page.text
        pattern = r'name="_xsrf" value="(.*?)"'  # r'name="_xsrf" value="(.*+)"'  所以写加为什么不对??
        _xsrf = re.findall(pattern, html)  # 需要注意的是, 匹配后返回的是一个list
        return _xsrf[0]

    def get_captcha(self):
        t = str(int(time.time() * 1000))
        print 't:', t
        print 'time.time()', time.time()
        url = 'https://www.zhihu.com/captcha.gif?r={}&type=login', t  # 所以 用{} ,t  有什么不对???  haha 先放着吧
        print 'imgurl:', url
        r = self.session.get(url, headers=self.header)

        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
            f.close()

        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print '请到 %s处找到captcha.jpg' % os.path.abspath('captcha.jpg')
        captcha = raw_input("请输入验证码: ")
        return captcha

    def is_login(self):
        url = 'http://www.zhihu.com/settings/profile'
        login_code = self.session.get(url, headers=self.header, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

    def login_zh(self, account, password):
        if re.match(r'^1[0-9]{10}$', account):
            print '手机号登录'
            post_url = 'https://www.zhihu.com/login/phone_num'
            post_data = {
                '_xsrf': self.get_xsrf(),
                'password': password,
                'phone_num': account,
                'remember_me': True
            }
        elif '@' in account:
            print "邮箱登录"
            post_url = "https://www.zhihu.com/login/email"
            post_data = {
                "_xsrf": self.get_xsrf(),
                "email": account,
                "password": password,
                "remember_me": True
            }
        else:
            print "请输入正确的账户名"

        try:  # 不需要验证码
            login_item = self.session.post(post_url, data=post_data, headers=self.header)
            login_status = login_item.status_code
            print login_status
            print "知乎登录被占领~"
        except:
            post_data['captcha'] = self.get_captcha()
            self.session.post(post_url, post_data, headers=self.header)
            print "就算要输验证码 但是还是不在话下"

        self.session.cookies.save()


class Crawl(scrapy.spiders.Spider):
    login = Login()
    item = TrytozhItem()
    if login.is_login():
        print "您已经登录了"
    else:
        account = 'echooc@outlook.com'
        password = '*******'

    login.login_zh(account, password)
    name = 'ZH'  # 可以生成多个实例。但是spider的名称不能相同且必须存在
    allow_domins = ["www.zhihu.com/topics"]
    start_urls = ['https://www.zhihu.com/topic/19550994/hot',
                  ]
    print 'enter'

    def is_ban(self):
        print "出现错误。可能需要验证码"
        flag = raw_input("请到浏览器中处理,处理成功(t),处理失败(任意字符)")
        if flag == 't' or 'T':
            errflag = False
        else:
            errflag = True
        return errflag

    def start_requests(self):
        self.cookies = COOKIES
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url,
                              meta={'cookiejar': i},
                              headers=self.login.header,
                              cookies=self.cookies,
                              callback=self.parse)
# 提取 一个页面的 问题url
    def parse(self, response):
        # print response.body
        qUrl = set()
        login = Login()
        driver = webdriver.Chrome()
        print 'i am in'

        # selenium 在弹出的浏览器中 模拟登录
        WebDriverWait(driver, 5)
        driver.get(response.url)
        driver.find_element_by_xpath('//*[@id="SidebarSignFlow"]/div[1]/div[2]/form/div[6]/span/a').click()
        driver.find_element_by_xpath('//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[1]/input').send_keys('echooc@outlook.com')
        driver.find_element_by_xpath('//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[2]/input').send_keys('*******')
        driver.find_element_by_xpath('//*[@id="SidebarSignFlow"]/div[2]/div/div[2]/form/div[4]/input').click()
        try:
            driver.find_element_by_class_name('zu-top-nav-userinfo ')
        except:
            # 获取验证码
            t = str(int(time.time() * 1000))
            # print 't:', t
            print 'time.time()', time.time()
            captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"  # 所以 用{} ,t  有什么不对???  haha 先放着吧
            print 'imgurl:', captcha_url
            r = login.session.get(captcha_url, headers=login.header)
            with open('captcha.jpg', 'wb') as f:
                f.write(r.content)
                f.close()
            try:
                im = Image.open('captcha.jpg')
                im.show()
            except:
                print '请到 %s处找到captcha.jpg' % os.path.abspath('captcha.jpg')
            captcha = raw_input("请输入验证码: ")

        for i in range(50):
            # selenuim 响应实在太慢了 所以读取不了
            #页面的元素加载需要时间，而这个时间是不确定的，但是你的执行是一直在一步步往下走，如果实际页面等待时间过长导致某个dom元素还没出来.
            wait = WebDriverWait(driver, 10)
            # 和以下一句的作用是 等到 下面的元素出来,最多等10秒。但是由于是动态加载的 并且我使用的是一个固定的元素 所以没有给加载的时间
            # 所以读取的内容有限。
            wait.until(lambda dr: driver.find_element_by_xpath('//div[@class="feed-content"]/h2/a'))
            #  Selector(response).xpath('//div[@class="feed-content"]/h2/a/@href').extract() 这里的response一直是 一开始传入的response
            soup = BeautifulSoup(driver.page_source, "html.parser")  # "html.parser默认的解释器
            for i in soup.find_all("a", class_='question_link'):
                print str(i)
                qUrl.add(re.search('(/question/[0-9]*)', str(i)).group())

            try:
                wait = WebDriverWait(driver, 2)
                wait.until(lambda dr: driver.find_element_by_class_name('zu-button-more'), message="get button")
                # ----------- 这里是 需要点击按钮翻页的写法
                # # next_page = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div[4]/a')  # 暂且认为你是正确的 如果模拟登录了没有问题的话 那么就不改了
                # next_page = driver.find_element_by_class_name('zu-button-more')
                # next_page.click()
                driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                with codecs.open('url.txt', 'w+', encoding='utf-8') as f1:
                    for i in list(qUrl):
                        f1.write('\n')
                        f1.write(i)
                f1.close()

            except:
                if self.is_ban():
                    yield Request(url=response.url,
                                  meta={"change_proxy": True},
                                  callback=self.parse)
                else:
                    print ("---------- 可能已经结束 或者 报错。")
                    break


    # 高匿IP / 管道 / url写入文件,从文件中读取后调用 读取信息/为了防止出错 怎么办 就是如果出现错误 需要重新跑么 之类的思考 /查一下 selenuim能不能绕过反爬虫



#--------------------  以下是 实现跳转的 尝试代码--------------------

    # def parse(self, response):
    #     # print response.body
    #     print 'i am in'
    #     item = Selector(response).xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/*')
    #     # 返回多个selector对象组成的列表 里面的data是 div/的内容信息。
    #     # [<Selector xpath='/html/body/div[3]/div[1]/div/div/div[2]/div/*' data=u'<div class="item"><div class="blk">\n<a t'>]
    #     print 'item', item
    #     guangchang_url = item.xpath('div/a[1]/@href').extract()  # 将每一项取出,进行匹配 得到的是内容为匹配的字段的列表
    #     item_url = []
    #     for u in guangchang_url:
    #         item_url.append('www.zhihu.com' + u + '/hot')
    #     print 'gg:', item_url
    #
    #     for i, url in enumerate(item_url):
    #         yield FormRequest(url,
    #                           meta={'cookiejar': i},
    #                           headers=self.login.header,
    #                           cookies=self.cookies,
    #                           )

    #
    # def parse_item(self, response):
    #     print response.body
        # print item_url





'''
判断是否被ban
'''








