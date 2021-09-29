import requests
from bs4 import BeautifulSoup
import json
url='https://webscraper.io/test-sites'
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
div=soup.find("div",class_="container test-sites")
body=div.find_all("div",class_="row test-site")
position=0
list=[]
for i in body:
    name=i.find("h2",class_="site-heading").a.get_text().strip()
    position+=1
    link="https://webscraper.io"
    url=link+i.find("h2",class_="site-heading").a.get('href')
    dic={"position":position,"course_name":name,"url":url}
    list.append(dic)
with open("Commerce_data.json","w") as f:
    json.dump(list,f,indent=4)

