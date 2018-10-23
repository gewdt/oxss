from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

html = urlopen("https://en.wikipedia.org/wiki/Tom_Hanks")
bsOBJ = BeautifulSoup(html,"html.parser")
for link in bsOBJ.find_all("a"):
    if "href" in link.attrs:
        print(link.attrs["href"])