import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


for i in range(5):
    page_start = str(i * 20)
    url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=' \
          'recommend&page_limit=20&page_start=20&page_start=' + page_start
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(HTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, verify=False)
    content = response.content.decode()
    content_list = json.loads(content)['subjects']
    for item in content_list:
        title = item['title']
        rate = item['rate']
        link = item['url']
        print(title, rate, link)
