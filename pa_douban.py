import requests
from bs4 import BeautifulSoup
#路由
result = []
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    #header
    print(url)
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text)
    aList= soup.select('a[title]')
    for index in aList:
        #去掉\n换行符
        result.append(index.get_text(" ", strip=True))
print(result)

