from hashlib import md5
url = 'https://www.dytt8.net/html/gndy/dyzz/20221116/63158.html'
secret = md5()
#十六进制加密
finger = secret.hexdigest()
print(finger)