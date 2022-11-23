from urllib import request, parse
from fake_useragent import UserAgent


#伪装客户端，反爬虫
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
}
# 1、创建请求对象，包装ua信息
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)


html = res.read().decode('utf-8')
print(html)


#实例对象
ua = UserAgent()
print(ua.Firefox)
print(ua.Firefox)

print(ua.ie)
print(ua.Chrome)


#url处理
print('url处理==============================================')

query_string = {'wd': 'pp'}
result = parse.urlencode(query_string)
print(result)
url = 'http://www.baidu.com/s?{}'.format(result)
print(url)

