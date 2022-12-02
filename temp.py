import time
import random
from pymysql.converters import escape_string


a = "Dont't take to me"


data = escape_string(a)
print(data)

for i in range(10):
    print(random.randint(2,4))

