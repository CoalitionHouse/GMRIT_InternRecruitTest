from bs4 import BeautifulSoup
import urllib2
import re

page=urllib2.urlopen("https://raw.githubusercontent.com/kusaraju-padala/GMRIT_InternRecruitTest/master/Buckton_Castle")
soup = BeautifulSoup(page)

f=open("links.txt","w+")

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    f.write(link.get('href'))
    f.write("\n")
    
f.close()
