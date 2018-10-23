from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org"+articleUrl)
    bsOBJ = BeautifulSoup(html,"html.parser")
    return bsOBJ.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Tom_Hanks")

while len(links) > 0 :
    newarticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newarticle)
    links = getLinks(newarticle)