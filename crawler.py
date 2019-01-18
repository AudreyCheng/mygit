import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
web_url = 'https://unsplash.com'
r = requests.get(web_url, headers=headers)
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='_1ac-D _3mCZ_')

for a in all_a:
    print a['style']
for a in all_a:
    img_str = a['style']
    print img_str[img_str.index('"')+1 : img_str.index('"',img_str[img_str.index('"')+1)]