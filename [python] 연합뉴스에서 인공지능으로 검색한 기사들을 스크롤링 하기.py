# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:04:03 2021

@author: Owner
"""

■ 연합뉴스에서 인공지능으로 검색한 기사들을 스크롤링 하기 

연합뉴스는  셀레니움을 이용해서  웹스크롤링을 해야합니다
( 셀레니움은 손으로 클릭해서 웹의 기사를 긁어오는것을 컴퓨터에게 시키는 모듈이름)

# 1. 연합 뉴스에서 인공지능으로 검색했을 때 url 을 알아내시오

https://www.yna.co.kr/search/index?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&ctype=A&page_no=1

# 2. 위의 url 의 html 코드를 beautiful soup 으로 파싱하여 출력하시오 !

from bs4 import BeautifulSoup
import urllib.request

list_url = 'https://www.yna.co.kr/search/index?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&ctype=A&page_no=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
print (soup)

# 3. 위의 사이트에서 상세기사 url 을 알아내기 위한 태그이름과 클래스이름을 알아내시오

답:  태그이름은 div 이고 클래스 이름은 cts_atclst 입니다. 

# 4.  위의 태그이름과 클래스 이름을 가지고  상세 기사 url 을 출력하시오 ! 

from bs4 import BeautifulSoup
import urllib.request
list_url = 'https://www.yna.co.kr/search/index?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&ctype=A&page_no=1'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
#print(soup)
result1=soup.find_all('div', class_ ='cts_atclst')
for i in result1:
    print (i) 


선생님 구글링했는데 연합뉴스 html이 비어있다는 내용이 있네요.
"안타깝게도 정보가 없다. 우리가 원하는 정보는 list_thumb 클래스ul
태그 내부인데 비어 있다.
실제로 이러한 경우가 종종 있다. 
이 경우는 보통 html을 요청했을 때,  javascript가 포함되어 브라우저에서 작동시켜야 내용이 채워지는 경우들이다. 
따라서 html 자체만을 보는 것으로는 원하는 결과를 얻을 수 없다.

귀찮지만 이럴때는 다른 방식을 사용해야 한다.
가상의 브라우저를 만들어 JS를 구동시킨 결과를 파싱하면 되는 것이다.


