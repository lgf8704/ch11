import requests


kv = {'wd': 'python'}
r = requests.get("http:www.baidu.com/s", params=kv)
r.raise_for_status()
