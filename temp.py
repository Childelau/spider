from urllib import request
import re


url = 'https://www.dytt8.net/html/gndy/dyzz/20221028/63097.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
rq = request.Request(url=url,headers=headers)
res = request.urlopen(rq)
html = res.read().decode('gb2312', 'ignore')
print(html)

# re_bds = '<div class="title_all"><h1><font color="#07519a">(.*?)</font></h1></div>'
re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<a.*?href="(.*?)"'

pattern = re.compile(re_bds, re.S)
result = pattern.findall(html)
print(result)
