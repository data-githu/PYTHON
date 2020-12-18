# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:50:51 2020

@author: Owner
"""

■ 이데일리뉴스에서 첫눈을 검색한 기사들을 스크롤링 하기

예제1. 이데일리뉴스에서 첫눈을 검색하여 첫페이지의 url을 가져오시오.
https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1

예제2. 위의 url 의 첫페이지의 html 코드를 BeautifulSoup 으로 파싱하시오.
from bs4 import BeautifulSoup
import urllib.request

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
print(soup)

예제3. 상세기사 url 을 찾기 위한 태그 이름과 클래스 이름을 알아내시오.
태그이름 : div, 클래스 이름 : newsbox_04

예제4. 상세기사 url을 출력하시오! 
from bs4 import BeautifulSoup
import urllib.request

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
#print(soup)
result1=soup.find_all('div',class_ ='newsbox_04')
for i in result1:
    print("http://edaily.co.kr/" + i.find_all('a')[0].get("href"))

예제5. 위의 상세기사 url 을 params라는 비어있는 리스트에 담으시오!
from bs4 import BeautifulSoup
import urllib.request

list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
#print(soup)
result1=soup.find_all('div',class_ ='newsbox_04')
params=[]
for i in result1:
    params.append("http://edaily.co.kr/" + i.find_all('a')[0].get("href"))
print(params)

예제6. 위의 코드를 가지고 eda_scroll 이라는 함수를 생성하시오!
from bs4 import BeautifulSoup
import urllib.request

def eda_scroll():
    list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    #print(soup)
    result1=soup.find_all('div',class_ ='newsbox_04')
    params=[]
    for i in result1:
        params.append("http://edaily.co.kr/" + i.find_all('a')[0].get("href"))
    return params
print(eda_scroll())

예제7. 위의 상세기사 url 하나를 가지고 기사 본문을 출력하시오!
from bs4 import BeautifulSoup
import urllib.request
list_url = 'http://edaily.co.kr//news/read?newsId=01387446625997536&mediaCodeNo=258'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result1 = soup.find_all('div',class_='news_body')
for i in result1:
    print(i.get_text())

예제8. 위의 스크립트로 eda_detail_scroll 함수를 생성하시오!
def eda_detail_scroll():
    list_url = 'http://edaily.co.kr//news/read?newsId=01387446625997536&mediaCodeNo=258'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    result1 = soup.find_all('div',class_='news_body')
    for i in result1:
        return i.get_text()

print(eda_detail_scroll())

예제9. 처음에 만들었던 함수인 eda.scroll()함수를 수정하는데 페이지 1개가 아니라 페이지 3개의 상세기사 url이 params 리스트에 담겨지도록 수정하시오!
from bs4 import BeautifulSoup
import urllib.request

def eda_scroll():
    params=[]
    for i in range(1,4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=' +str(i)+ ' '
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        #print(soup)
        result1=soup.find_all('div',class_ ='newsbox_04')
        for i in result1:
            params.append("http://edaily.co.kr/" + i.find_all('a')[0].get("href"))
    return params
print(eda_scroll())

예제10. eda_datail_scroll() 함수 안에서 eda_scroll() 함수를 호출하여 상세기사 url을 60개를 다 가져와서 60개의 기사를 출력할 수 있도록 eda_detail_scroll() 함수를 수정하세요.
def eda_detail_scroll():
    list_url = eda_scroll()
    for i in list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        result1 = soup.find_all('div',class_='news_body')
        for i in result1:
            print( i.get_text())

print(eda_detail_scroll())

예제11. 위의 출력되고 있는 기사 본문이 c드라이브 data 밑에 eda.txt로 저장되게 하세요.
from bs4 import BeautifulSoup
import urllib.request

def eda_scroll():
    params=[]
    for i in range(1,4):
        list_url = 'https://www.edaily.co.kr/search/news/?keyword=%ec%b2%ab%eb%88%88&page=' +str(i)+ ' '
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        #print(soup)
        result1=soup.find_all('div',class_ ='newsbox_04')
        for i in result1:
            params.append("http://edaily.co.kr/" + i.find_all('a')[0].get("href"))
    return params

def eda_detail_scroll():
    list_url = eda_scroll()
    f=open("c:\\data\\eda.txt","w",encoding="UTF-8")
    for i in list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        result1 = soup.find_all('div',class_='news_body')
        for i in result1:
            f.write(str(i.get_text())+"\n")
    f.close()
print(eda_detail_scroll())
