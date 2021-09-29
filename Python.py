import requests
from bs4 import BeautifulSoup
import json
url="https://en.wikipedia.org/wiki/Python_(programming_language)"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
div=soup.find("table",class_="infobox vevent")
body=div.find_all("th",class_="infobox-label")
tbody=div.find_all("td",class_="infobox-data")
main_list=[]
key_list=[]
value_list=[]
dic={}
for i in body:
    name=i.get_text()
    key_list.append(name)
for i in tbody:
    value=i.get_text()
    value_list.append(value)
for i in range(len(value_list)):
    dic[key_list[i]]=value_list[i]
main_list.append(dic)
with open("Python_data.json","w") as d:
    json.dump(main_list,d,indent=4)
