import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/71.0.3578.98 Safari/537.36'}
r = requests.get('https://www.qiushibaike.com/', headers = headers)
content = r.text
soup = BeautifulSoup(r.text, 'lxml')

divs = soup.find_all(class_='article block untagged mb15')

print(divs)
# print content

for div in divs:
    joke = div.span.get_text()
    print(joke)
    print('- - - - - -')  



