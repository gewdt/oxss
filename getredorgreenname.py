from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsOBJ = BeautifulSoup(html)
namelist = bsOBJ.find_all("span",{"class":"green"})

for name in namelist:
    print(name.get_text())


#print(namelist)