from urllib import request
import requests
import re
import time
import random
import csv
from ua_info import ua_list

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://www.maoyan.com/board/4?offset=10'

    #请求函数
    def get_html(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'}
        res = requests.get(url, headers=headers)
        
        html = res.text
        print(html)
        print(20*'==')
        #调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        #reg
        # re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        re_bds = '<dd>.*?class="poster-default".*?<img.*?class="board-img".*?src="(.*?)"</dd>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        print(r_list)

    
    def run(self):
        self.get_html(self.url)



if __name__ == '__main__':
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print('错误：', e)