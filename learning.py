from bs4 import *
import requests as rq
import openpyxl
try:
    respose=rq.get("https://www.espncricinfo.com/rankings/content/page/211271.html")
    soup=BeautifulSoup(respose.text,'html.parser')
    div = soup.find_all("div", class_= "ciPhotoContainer")
    l=len(div)
    print(l)
    format=div[0].find_all('h3')
    for i in format:
        print(i.text)
    table=soup.find("table",class_="StoryengineTable")
    print(table)

    

except Exception as e:
    print(e)