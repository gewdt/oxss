from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsOBJ,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    for link in bsOBJ.findAll("a",href = re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks







def getExternalLinks(bsOBJ,excludeUrl):
    externalLinks = []

    for link in bsOBJ.findAll("a",href = re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks







def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsOBJ = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsOBJ,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("没有外链，找下一个")
        domain = urlparse(startingPage).scheme + "://" +urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsOBJ,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]





def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("外链是：" + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://80a.fun")