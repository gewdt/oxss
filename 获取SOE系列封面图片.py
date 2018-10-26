import requests
from bs4 import BeautifulSoup
import time,re
import requests.adapters

baseurl = 'https://avmoo.net/cn/search/soe/page/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


page = 0
for num in range(14,100):
    time.sleep(10)
    req = requests.get(baseurl+str(num), headers=headers,allow_redirects=False)
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    content = req.text
    obj = BeautifulSoup(content, 'html.parser')
    # pic1 = obj.findAll("img", {"data-original": re.compile("http://img.doutula.com/production/uploads/image//2018.*\..*!dta")})
    pics = obj.findAll("img", {"src": re.compile("https://jp.netcdn.space/digital/video/soe.*/soe.*\.jpg")})
    page +=1
    filename = 0
    for pic in pics:
        time.sleep(1)
        filename += 1
        img = requests.get(pic["src"], headers=headers)
        with open("d:/soe/"+pic["src"][-15:-1] +".jpg", "wb") as file:
            file.write(img.content)
        print(pic["src"])

    print(len(pics))



