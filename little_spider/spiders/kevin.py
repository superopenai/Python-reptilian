# -*- coding: utf-8 -*-
from pprint import pprint

import scrapy
import re

class KevinSpider(scrapy.Spider):
    name = 'liaoda'
    allowed_domains = ['http://www.lcu.edu.cn/szdw/ldms/index.htm']
    start_urls = ['http://www.lcu.edu.cn/szdw/ldms/index.htm']
    # //*[@id="page-content"]/div/div/div[1]/div[1]/div[3]/h3[5]



    # def parse(self, response):
    #     res=response.xpath("//*[@id=\"page-content\"]/div/div/div[1]/div[3]/div[3]/div[4]/p/text()")
    #     imf = res.extract()
    #
    #     pprint(imf)
    #     pass
    print("爬取聊大师资团队")
    def parse(self, response):
        print("聊大优秀教师")
        post=response.xpath("//*[@id=\"height2\"]/div[2]/ul/li[2]/div[2]/ol/li/a/text()").extract()
        print(post)
        print("享受国务院特殊津贴的专家")
        postget1 = response.xpath ( "//*[@id=\"height2\"]/div[2]/ul/li[2]/div[2]/ol/li[2]/a/text()" ).extract ()
        print(postget1)
        print ( "泰山学者" )
        postget2 = response.xpath ( "//*[@id=\"height2\"]/div[2]/ul/li[2]/div[2]/ol/li[3]/a/text()" ).extract ()
        print ( postget2 )
        print ( "山东省有突出贡献的中青年专家" )
        postget3 = response.xpath ( "///*[@id=\"height2\"]/div[2]/ul/li[2]/div[3]/ol/li[1]/a/text()" ).extract ()
        print ( postget3)
        print ( "山东省优秀教师" )
        postget4 = response.xpath ( "//*[@id=\"height2\"]/div[2]/ul/li[2]/div[3]/ol/li[2]/a/text()" ).extract ()
        print ( postget4 )
        print("省级教学名师")
        postget5 = response.xpath ( "//*[@id=\"height2\"]/div[2]/ul/li[2]/div[3]/ol/li[3]/a/text()" ).extract ()
        print(postget5)


# 并不是直接print(res)来调试   的,我在主目录建立一个mian入口函数
# 使用scrapy.cmdline的执行函数



# response.xpath("//*[@id=\"page-content\"]/div/div/div[1]/div[3]/div[3]/div[4]/p/text()").extract()
# //*[@id="height2"]/div[2]/ul/li[2]/div[2]/dl/dt[1]/a