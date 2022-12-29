# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:58:12 2022

@author: watson
"""

import requests
from bs4 import BeautifulSoup

import db

from datetime import datetime as dt # 抓日期函式庫

today = dt.today() # 抓今天的日期格式

todayS = today.strftime('%Y-%m-%d') # 將設定好的日期格式轉換為字串使用


url = "https://zh.m.wikipedia.org/zh-tw/%E5%8F%B0%E7%81%A3%E5%93%BA%E4%B9%B3%E5%8B%95%E7%89%A9%E5%88%97%E8%A1%A8"

payload = {'p':'sony'}

data = requests.get(url).text

soup = BeautifulSoup(data,'html.parser')

oneclass=soup.find_all('ol')[0]

species = oneclass.find_all('a')
scien = oneclass.find_all('i')
family = "鼴鼠科"


for info,sci in zip(species,scien):
    name = info.text
    scientific = sci.text
    link = "https://zh.m.wikipedia.org"+info.get('href')
    
    print(name)
    print(scientific)  
    print(family)
    print(link)
    webdata = requests.get(link).text
    websoup = BeautifulSoup(webdata,'html.parser')
    webpic= websoup.find_all('a',class_="image")
    if len(webpic)>0:
        pic_url = webpic[0].find('img').get('src')
        print(pic_url)
    else:
        pic_url = "尚在建構中"
        print(pic_url)
    webdis = websoup.find_all('p')
    intro = ""
    for i in webdis:
        intro += i.text
    print(intro)
    
        

        
    
    

# cursor = db.conn.cursor()



# for row in allgoods:
         
#      link = row.get('href')
#      webdata = requests.get(link).text
#      websoup = BeautifulSoup(webdata,'html.parser')
#      webgoods = websoup.find_all('div',class_="ProductItemPage__infoSection___3K0FH")
#      for webrow in webgoods:
#          photo = webrow.find("img").get('src')
#          title = webrow.find("h1").text
#          price = webrow.find("div",class_="HeroInfo__mainPrice___1xP9H").text
#          price = price.replace('$','').replace(',','')

         
#          print(link)
#          print(photo)
#          print(title)
#          print(price)
#          print()
    

#          sql = "select * from product where name='{}' ".format(title)
        
#          cursor.execute(sql)
#          db.conn.commit()
        
#          if cursor.rowcount == 0 :  # 表示沒有該產品
#               sql = "insert into product(name,price,product_url,photo_url,create_date,discount) values('{}','{}','{}','{}','{}','0')".format(title,price,link,photo,todayS)
#               cursor.execute(sql)
#               db.conn.commit()
        
    
# db.conn.close()    
    
    
    




