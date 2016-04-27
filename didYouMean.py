import os
import urllib3
import io
import gzip
import sys
import urllib
import re

from bs4 import BeautifulSoup
from io import StringIO
def getPage(url):
    http = urllib3.PoolManager()
    page = http.request('GET', url)
    return page.data

def didYouMean(q):
    q = str(str.lower(q)).strip()
    url = "http://www.google.com/search?q=" + q
    html = getPage(url)
    soup = BeautifulSoup(html, "html.parser")
    ans = soup.find('a', attrs={'class' : 'spell'})
    try:
        result = repr(ans.contents)
        result = result.replace("u'","")
        result = result.replace("/","")
        result = result.replace("<b>","")
        result = result.replace("<i>","")
        result = re.sub('[^A-Za-z0-9\s]+', '', result)
        result = re.sub(' +',' ',result)
    except AttributeError:
        result = 1
    return result

if __name__ == "__main__":
    response = didYouMean(sys.argv[1])
    print (response)
