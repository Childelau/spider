from lxml import etree
html_str = '''
<div class="wrapper">
    <a href="www.biancheng.net/product/" id="site">website product</a>
    <ul id="sitename">
    <li><a href="http://www.biancheng.net/" title="编程帮">编程</a></li>
    <li><a href="http://world.sina.com/" title="新浪娱乐">微博</a></li>
    <li><a href="http://www.baidu.com" title="百度">百度贴吧</a></li>
    <li><a href="http://www.taobao.com" title="淘宝">天猫淘宝</a></li>
    <li><a href="http://www.jd.com/" title="京东">京东购物</a></li>
    <li><a href="http://c.bianchneg.net/" title="C语言中文网">编程</a></li>
    <li><a href="http://www.360.com" title="360科技">安全卫士</a></li>
    <li><a href="http://www.bytesjump.com/" title=字节">视频娱乐</a></li>
    <li><a href="http://bzhan.com/" title="b站">年轻娱乐</a></li>
    <li><a href="http://hao123.com/" title="浏览器">搜索引擎</a></li>
    </ul>
</div>
'''

parse_html = etree.HTML(html_str)
#xpath
xpath_bds = '//a/text()'
r_list = parse_html.xpath(xpath_bds)
print(r_list,30*'*')

xpath_bds1  = '//a/@href'
r_list1  =parse_html.xpath(xpath_bds1)
print(r_list1,30*'*')

xpath_bds2 = '//ul[@id="sitename"]/li/a/@href'
r_list2 = parse_html.xpath(xpath_bds2)
print(r_list2)