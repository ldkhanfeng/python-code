# -*- coding:utf-8 -*-
import urllib.request
import requests
from bs4 import BeautifulSoup

url = "http://10.104.0.225/portal.php"       # 定义网页
page = urllib.request.urlopen(url)           # 打开网页
#print(type(page))                            # <class 'http.client.HTTPResponse'>
#print(type(page.read()))                     # <class 'bytes'>
#print(page)                                  # <http.client.HTTPResponse object at 0x00000000034A3F28>
#print(page.read())                           # 网页源代码，未排版

req = requests.get(url)
#print(req)                                   # <Response [200]>
#print(type(req))                             # <class 'requests.models.Response'>

