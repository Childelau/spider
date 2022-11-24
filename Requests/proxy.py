import requests
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
}
proxies = {
    'http': 'http://123.182.59.65:8089',
    'https':'https://123.182.59.65:8089'
}
html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)