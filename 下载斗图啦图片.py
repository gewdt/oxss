import requests
import lxml
from bs4 import BeautifulSoup
import re

baseurl = "http://www.doutula.com/article/list/?page="
headers = {"Referer": "http://www.doutula.com/",
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
page = 0
for num in range(1,501):

    req = requests.get(baseurl+str(num), headers=headers)
    content = req.text
    obj = BeautifulSoup(content, 'lxml')
    # pic1 = obj.findAll("img", {"data-original": re.compile("http://img.doutula.com/production/uploads/image//2018.*\..*!dta")})
    pics = obj.findAll("img", {"data-original": re.compile("https://ws.*\.sinaimg.cn/bmiddle/.*\.jpg")})
    page +=1
    filename = 0
    for src in pics:
        filename += 1
        img = requests.get(src["data-original"], headers=headers)
        with open("imgs/"+str(page)+"-"+ str(filename) +".jpg", "wb") as file:
            file.write(img.content)
        print(src["data-original"])

    print(len(pics))