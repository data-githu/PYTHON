# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:49:15 2020

@author: Owner
"""

■ 143. 웹스크롤링 실전2 (중앙일보사)
중앙일보사 홈페이지에서 인공지능으로 검색을 했을 대 나오는 기사들을 전부 웹스크롤링 합니다.

예제1. 중앙일보사 홈페이지에서 인공지능으로 검색했을 때 나오는 url 을 가져오시오!
https://news.joins.com/Search/TotalNews?page=1&Keyword=인공지능&SortType=New&SearchCategoryType=TotalNews


예제2. 위의 사이트에서 보이는 상세 기사를 클릭해보시오!
https://news.joins.com/article/23947044
https://news.joins.com/article/23946979
https://news.joins.com/article/23946876


예제3. 인공지능으로 검색했을 때 나오는 상세기사의 url을 출력하시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = 'https://news.joins.com/Search/TotalNews?page=3&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews'
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1=soup.find_all('h2', class_ ='headline mg')
for i in result1:
    for k in i: #h2 태그안의 a태그의 html 코드를 가져오기 위한 코드
        print(k.get('href'))


예제4. 위의 상세 기사 url 을 params 라는 비어있는 리스트에 다 넣으시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = 'https://news.joins.com/Search/TotalNews?page=3&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews'
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1=soup.find_all('h2', class_ ='headline mg')
params=[]
for i in result1:
    for k in i: #h2 태그안의 a태그의 html 코드를 가져오기 위한 코드
        params.append(k.get('href'))
print(params)


예제5. 상세기사 url 중에 하나를 복사해오고 그 상세기사 url 의 웹페이지로 접속해서 본문 기사의 태그 이름과 클래스 이름이 무엇인지 확인하시오!
태그이름은 div , 클래스 이름은 article_body mg fs4


예제6. 위의 상세기사의 본문을 스크롤링해서 출력하시오!
from bs4 import BeautifulSoup
import urllib.request
list_url = 'https://news.joins.com/article/23944347'
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result1=soup.find_all('div', class_ ='article_body mg fs4')
params2= []
for i in result1:
    params2.append(i.get_text(" ", strip = True))
print(params2)


예제7. 상세기사 url 을 가져와서 params 리스트에 넣고 출력하는 예제4번 코드를 함수로 생성하시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
def j_scroll():
    list_url = 'https://news.joins.com/Search/TotalNews?page=3&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews'
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    result1=soup.find_all('h2', class_ ='headline mg')
    params=[]
    for i in result1:
        for k in i: #h2 태그안의 a태그의 html 코드를 가져오기 위한 코드
            params.append(k.get('href'))
    return params
print(j_scroll())


예제8. 상세 기사 url 로 본문 기사를 스크롤링해서 리스트에 담았던 예제 6번을 j_detail_scroll() 함수로 생성하시오!
from bs4 import BeautifulSoup
import urllib.request
def j_detail_scroll():
    list_url = 'https://news.joins.com/article/23944347'
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    result1=soup.find_all('div', class_ ='article_body mg fs4')
    params2= []
    for i in result1:
        params2.append(i.get_text(" ", strip = True))
    return params2
print(j_detail_scroll())


예제9. 지금 만든 j_detail_scroll() 함수는상세기사 딱 한개의 본문을 출력하는 함수인데 이  j_detail_scroll() 함수에 j_scroll 함수를 실행했을때 나오는 상세 url 제공할 수 있도록 코드를 수정하시오!
from bs4 import BeautifulSoup
import urllib.request
def j_scroll():
    list_url = 'https://news.joins.com/Search/TotalNews?page=3&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews'
    url = urllib.request.Request(list_url)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    result1=soup.find_all('h2', class_ ='headline mg')
    params=[]
    for i in result1:
        for k in i:
            params.append(k.get('href'))
    return params

def j_detail_scroll():
    list_url = j_scroll()
    params2= []
    for i in list_url:
        url = urllib.request.Request(i)
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1=soup.find_all('div', class_ ='article_body mg fs4')
        for i in result1:
            params2.append(i.get_text(" ", strip = True))
    return params2

print(j_detail_scroll())
   

■ 중앙일보의 기사를 스크롤링하는 내용 총정리
	1. 검색 키워드를 가지고 검색을 한 후  그 url을 얻어낸다.
	2. 상세기사 URL을 리스트에 담는 j_scroll 함수를 생성한다.
	3. 상세기사 URL로 기사본문을 스크롤링하는 j_detail_scroll() 함수를 생성한다.
	4. j_detail_scroll() 함수 안에서 j_scroll 함수를 호출해서 상세기사 url 여러개를 받아오도록 코딩하고 받아온 상세기사 url로 본문 기사들을 params2 에 담는다는 코드로 수정한다.


문제417. 동아일보에서 검색 키워드를 가지고 검색을 한 후 그 url을 얻어낸다.
https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1



문제418. 상세기사 url을 리스트에 담는 d_scroll() 함수를 생성하세요
from  bs4  import  BeautifulSoup
import  urllib.request   

def  d_scroll():
    list_url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    result1 = soup.find_all( 'p', class_ = 'txt')
    params=[]
    for  i  in  result1:
        for k in i:
            params.append(k.get("href") )
    return params
print(d_scroll())


문제419. 상세기사 url로 기사본문을 스크롤링하는 d_detail_scroll() 함수 생성하세요.
def d_detail_scroll():

    list_url = d_scroll()
    params2 =[ ]
    for i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
        result1 = soup.find_all( 'div', class_ = 'article_txt')
        for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
            params2.append( i.get_text(" ", strip=True) ) 
    return params2
print(d_detail_scroll())


문제420. 한겨례 신문사에서 인공지능으로 검색했을때 나오는 기사 본문 스크롤링하는 함수 두개를  생성하시오!
#%%
from  bs4  import  BeautifulSoup
import  urllib.request   

def  h_scroll():
    list_url = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&media=news&submedia=&sort=d&period=all&datefrom=1988.01.01&dateto=2020.12.16&pageseq=0'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup = BeautifulSoup( result, "html.parser")
    result1 = soup.find_all( 'dt')
    params=[]
    for  i  in  result1:
        for k in i:
            params.append('http:' + k.get("href") )
    return params
print(h_scroll())

#%%
def h_detail_scroll():

    list_url = h_scroll()
    params2 =[ ]
    for i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup = BeautifulSoup( result, "html.parser")
            
        result1 = soup.find_all( 'div', class_ = "text")
        
        
        for  i  in  result1:  # result1 리스트의 요소를 하나씩 빼내는 코드
            params2.append( i.get_text(" ", strip=True) )  
    
    return params2
print(h_detail_scroll())


문제421. 하고 싶은 신문사에서 스크롤링하고 싶은 키워드를 넣고 검색했을 때 나오는 본문기사들을 수집하는 함수를 생성하시오! (페이지 1-3 를 스크롤링하세요.)
from bs4 import BeautifulSoup
import urllib.request
def j_page_scroll():
    params3 = []
    for i in range(1,4):
        params3.append('https://news.joins.com/Search/TotalNews?page='+ str(i)+'&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=TotalNews')
    return params3
print(j_page_scroll())

def j_scroll():
    list_url = j_page_scroll()
    params=[]
    for j in list_url:
        url = urllib.request.Request(j)
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1=soup.find_all('h2', class_ ='headline mg')
        for i in result1:
            for k in i:
                params.append(k.get('href'))
    return params
print(j_scroll())

def j_detail_scroll():
    list_url2 = j_scroll()
    params2= []
    for i in list_url2:
        url = urllib.request.Request(i)
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")
        result1=soup.find_all('div', class_ ='article_body mg fs4')
        for i in result1:
            params2.append(i.get_text(" ", strip = True))
    return params2

print(j_detail_scroll())
