from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pymysql

conn = pymysql.connect(host="10.11.101.18", user="test_smj", passwd="test_smj", db="test_smj",charset="utf8")
cur = conn.cursor()
cur.execute("USE test_smj")

random.seed(datetime.datetime.now())


def store(title, content):
    cur.execute("INSERT INTO namelist (title,content) VALUES (\"%s\",\"%s\")",(title, content))
    cur.connection.commit()
# INSERT INTO `namelist`(`id`, `name`, `title`, `content`) VALUES (33,'a','s','f')

def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsOBJ = BeautifulSoup(html, "html.parser")
    title = bsOBJ.find("h1").get_text()
    content = bsOBJ.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bsOBJ.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Tom_Hanks")




try :
    while len(links) > 0:
        newarticle = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newarticle)
        links = getLinks(newarticle)

finally:
    cur.close()
    conn.close()


# html = urlopen("https://en.wikipedia.org/wiki/Tom_Hanks")
# bsOBJ = BeautifulSoup(html, "html.parser")
# title = bsOBJ.find("h1").get_text()
# content = bsOBJ.find("div", {"id": "mw-content-text"}).find("p").get_text()
# print(title)
# print(content)