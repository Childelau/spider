import json
#loads
website_info='{"name" : "c语言中文网","PV" : "50万","UV" : "20万","create_time" : "2010年"}'
py_dict = json.loads(website_info)
print('data: %s,type: %s'%(py_dict, type(py_dict)))

item = {'website': 'C语言中文网', 'rank': 1}
item = json.dumps(item,ensure_ascii=False)
print(item,'type: %s'%(type(item)))