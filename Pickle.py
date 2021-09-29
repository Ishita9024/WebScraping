import requests
from bs4 import BeautifulSoup
import json
url="https://paytmmall.com/shop/search?from=recentSearch&userQuery=pickle&category=101419%2C101471"
res=requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
num=soup.find("div",class_="_1EI9")
serial=num.span.get_text()
split=serial.split()
p=split[1]
pr=(int(p)//32)+1
serial_no=0
pickle=[]
for j in range(1,pr+1):
    Url="https://paytmmall.com/shop/search?from=recentSearch&userQuery=pickle&page="+str(j)+"&category=101419%2C101471"
    Data1=requests.get(Url)
    Soup = BeautifulSoup(Data1.text,'html.parser')
    diV1=Soup.find("div",class_="_3RA-")
    diV2=diV1.find_all("div",class_="UGUy")
    diV3=diV1.find_all("div",class_="_1kMS")
    diV4=diV1.find_all("div",class_="_3WhJ")
    for i in range(len(diV2)):
        pickle_name=diV2[i].get_text()
        pickle_rate=diV3[i].get_text()
        pickle_link=diV4[i].a["href"]
        url1="https://paytmmall.com"+pickle_link
        serial_no+=1
        dic={"position":serial_no,"name":pickle_name,"price":pickle_rate,'url':url1}
        pickle.append(dic)
with open("Pickle_data.json","w") as f:
    json.dump(pickle,f,indent=4)

