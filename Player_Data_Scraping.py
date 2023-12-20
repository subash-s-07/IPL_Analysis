from bs4 import *
import requests as rq
import openpyxl
import pandas as pd
from csv import writer
def give(player):
    response=rq.get(player)
    soup=BeautifulSoup(response.text,'html.parser')
    data=soup.find_all("table")
    col=[]
    for i in data[0].find('tr').find_all('th'):
        col.append(i.text)
    length=len(col)
    table=data[0].find_all('td') 
    l=length
    table_list=[]
    temp=[]
    i=1
    while(i<=len(table)):
        if(i%l==0):
            temp.append(table[i-1].text)
            table_list.append(temp)
            temp=[]
        else:
            temp.append(table[i-1].text)
        i=i+1
    df=pd.DataFrame(table_list,columns=col)
    df=df.set_index("Format")
    return df
data=pd.read_csv("D:\web scraping\Indianplayer.csv")
l=[]
data=data.set_index("0")
data_list=data.values.tolist()
data_index=data.index.tolist()
for i in range(len(data_list)):
    df=give(data_list[i][0])
    d=df.columns.tolist()
    l=['Mat','Inns','NO','Runs','HS','Ave','SR','100s','50s','4s','6s']
    if 'Mat' in d:
        if 'Inns' in d:
            if 'NO' in d:
                if 'Runs' in d:
                    if 'HS' in d:
                        if 'Ave' in d:
                            if 'SR' in d:
                                if '100s' in d:
                                    if '50s' in d:
                                        if '4s' in d:
                                            if '6s' in d:         
                                                df=df[['Mat','Inns','NO','Runs','HS','Ave','SR','100s','50s','4s','6s']]
                                                print(df)
                                                a=df.iloc[:,0].index.tolist()
                                                if "Test" in a:
                                                    df1=df.loc["Test"].tolist()
                                                    df1.append(data_index[i])
                                                    print(df1)
                                                    with open('D:\web scraping\Test Batting.csv', 'a') as f_object:
                                                        writer_object = writer(f_object)
                                                        writer_object.writerow(df1)
                                                        f_object.close()