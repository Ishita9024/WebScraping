import requests
from bs4 import BeautifulSoup
import json
def scrap_top_list():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    div = soup.find("div",class_="lister")
    body = div.find("tbody",class_="lister-list")
    name = body.find_all("tr")
    list=[]
    position=0
    for i in name:
        movie = i.find("td",class_="titleColumn").a.get_text()
        rating = i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        Rating=float(rating)
        year = i.find("td",class_="titleColumn").span.get_text()
        Release_year=int(year[1:5])
        link="https://www.imdb.com"
        url = link + i.find("td",class_="titleColumn").a.get('href')
        position+=1
        dic={"movie_name":movie,"movie_rating":Rating,"movie_year":Release_year,"movie_link":url,"movie_position":position}
        list.append(dic)
    with open("Task1_data.json","w") as f:
        json.dump(list,f,indent=4)
    return list
data=scrap_top_list()





