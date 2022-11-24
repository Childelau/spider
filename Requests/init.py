import requests

url = 'https://fanyi.baidu.com'
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'donkey'
}
response =  requests.post(url, data=data)
print(response.encoding)
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)

img_url = 'https://img0.baidu.com/it/u=1250551608,2180019998&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500'
headers = {'headers': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
html = requests.get(url=img_url,headers=headers).content
#二进制方式下载图片
with open('D:/GitHub/spider/static/alg.jpg','wb') as f:
    f.write(html)


