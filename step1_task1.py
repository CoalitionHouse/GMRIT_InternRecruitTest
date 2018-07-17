from bs4 import BeautifulSoup
import urllib2
import re

url = r"https://raw.githubusercontent.com/kusaraju-padala/GMRIT_InternRecruitTest/master/Buckton_Castle"
page = open(url)
soup = BeautifulSoup(page.read())
f=open("links.txt","w+")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    f.write(link.get('href'))
    f.write("\n")
