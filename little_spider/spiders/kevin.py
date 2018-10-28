# -*- coding: utf-8 -*-
from pprint import pprint

import scrapy
import re

class KevinSpider(scrapy.Spider):
    name = 'kevin'
    allowed_domains = ['https://www.mrkevin.net/zbench/1854.html']
    start_urls = ['https://www.mrkevin.net/zbench/1854.html']
    # //*[@id="page-content"]/div/div/div[1]/div[1]/div[3]/h3[5]
    def parse(self, response):
        res=response.xpath("//*[@id=\"page-content\"]/div/div/div[1]/div[3]/div[3]/div[4]/p/text()")
        imf = res.extract()

        # reg="\w{n}"
        # result = re.findall(reg,imf)
        pprint(imf)
        pass



# 并不是直接print(res)来调试的,我在主目录建立一个mian入口函数
# 使用scrapy.cmdline的执行函数



# response.xpath("//*[@id=\"page-content\"]/div/div/div[1]/div[3]/div[3]/div[4]/p/text()").extract()
# //*[@id="height2"]/div[2]/ul/li[2]/div[2]/dl/dt[1]/a
