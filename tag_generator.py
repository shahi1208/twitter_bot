import requests
from bs4 import BeautifulSoup
import random

pages = random.randint(1,5000)

link ='https://archiveofourown.org/tags/ '.format(page=pages)

r = requests.get(link)
soup=BeautifulSoup(r.content,'html.parser')
    
tags=soup.find_all('li', {'class':"freeforms"})
tag=[tag.text for tag in tags]

with open('tag.txt','w') as f:
    f.write(random.choice(tag))
f.close()