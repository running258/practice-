import urllib
from lxml import etree
import re
import json
import chardet
import requests


curstart = 2

values = {
    'tableId': '32',
    'State': '1',
    'bcId': '124356639813072873644420336632',
    'State': '1',
    'tableName': 'TABLE32',
    'State': '1',
    'viewtitleName': 'COLUMN302',
    'State': '1',
    'viewsubTitleName': 'COLUMN299,COLUMN303',
    'State': '1',
    'curstart': str(curstart),
    'State': '1',
    'tableView': urllib.request.quote("国产药品商品名"),
    'State': '1',
}

post_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url = "http://app1.sfda.gov.cn/datasearch/face3/search.jsp"

response = requests.post(url, data=values, headers=post_headers)

resHtml = response.text
print (response.status_code)
print (resHtml)

Urls = re.findall(r'callbackC,\'(.*?)\',null', resHtml)
for url in Urls:
    # 坑
    print (url.encode('gb2312'))