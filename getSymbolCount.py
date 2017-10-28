import urllib.request, urllib.parse, urllib.error;
from bs4 import BeautifulSoup;

site = urllib.request.urlopen('https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols').read()
soup = BeautifulSoup(site)
tags = soup('tt')
count = 0
for tag in tags:
    count = count + 1
print(count)
