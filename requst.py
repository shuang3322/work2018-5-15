import requests
import json
from bs4 import BeautifulSoup
def req():

     returns = requests.get('http://weatherapi.market.xiaomi.com/wtr-v2/weather?cityId=101121301')
     returns.encoding = "utf8"
     print(returns.text)
     print(returns.cookies)
     print(returns.headers)
def req2():
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    }
    ss = '上海'
    test = ('https://www.baidu.com/s?wd=%s'% ss)
    print(test)
    returns = requests.get(test,headers=headers)
    # for key,item in test:
    #     print(key,item)
    return returns.text

down_text = req2()
import requests
from bs4 import BeautifulSoup
new_test = BeautifulSoup(down_text,'html.parser')
for k in new_test.find_all('a'):
    print(k)

