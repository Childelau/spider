import re


#正则表达式
html="""
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""

pattern = re.compile('<div.*?<a title="(.*?)".*?star">(.*?)</p>.*?div>', re.S)
r_list = pattern.findall(html)

print(r_list)
for item in r_list:
    print('电影:', item[0], item[1])
    print(20*'*')












