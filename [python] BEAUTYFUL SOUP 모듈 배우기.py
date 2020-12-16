# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:37:07 2020

@author: Owner
"""

■ 141. beautiful soup 모듈 배우기

파이썬 코드를 복잡하게 작성하지 않아도 편하게 웹스크롤링을 할 수 있도록 여러 함수들을 제공하는 웹스크롤링 전문 모듈입니다.

*카페에서 ecologicalpyramid.html 문서를 내려받아 c 드라이브 밑에 data 폴더 밑에 저장하세요.

예제1. ecologicalpyramid.html 코드를 beautiful soup 모듈에서 사용할 수 있도록 파싱을 하고 파싱된 내용을 출력하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
print(soup)


예제2. ecologicalpyramid.html 코드에서 class 이름 name 에 접근해서 데이터를 긁어오시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_="name")
print(result)

예제3. 위에서 긁어온 데이터에서 html 코드 말고 text 만 출력하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_="name")
for i in result:
    print(i.get_text())


문제408. ecologicalpyramid.html 문서에서 숫자들만 출력하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_="number")
for i in result:
    print(i.get_text())

문제409. 위에서 긁어온 숫자들을 a라는 비어있는 리스트에 저장한 후 a 안의 요소들을 정렬하고 a 리스트를 출력하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\ecologicalpyramid.html")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_="number")
a=[]
for i in result:
    a.append(int(i.get_text()))
a.sort()
print(a)

문제410. 중앙일보사 홈페이지로 가서 신문기사 하나를 보시오
ctrl + s 로 기사의 html 문서를 aa77.html 로 저장합니다.

문제411. aa77.html 을 beautifulsoup 모듈의 함수를 쓸 수 있도록 파싱하고 출력하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\aa77.html",encoding = "UTF8")
soup = BeautifulSoup(f, "html.parser")
print(soup)

문제412. 위의 기사의 본문을 가져오기해 기사 본문의 class 이름이 무엇인 확인하세요.
크롬의 개발자모드 단축키인 F12를 누르면 옆에 html 코드 창이 나오면서 개발자 모드 화면이 열립니다. 그러면 왼쪽 상담의 화살표를 클릭하고 기사본문을 클릭하면 html 문서에 class 이름을 확인할 수 있는 html 문서쪽으로 바로 이동합니다. 

문제413. 클래스 이름 article_body mg fs4 로 접근하여 text를 긁어오시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\aa77.html",encoding = "UTF8")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_='article_body mg fs4')
for i in result:
    print(i.get_text())

문제414. 위에서 스크롤링한 중앙일보 기사를 c 드라이브 밑에 mytext23.txt로 저장하시오!
from bs4 import BeautifulSoup
f=open("c:\\data\\aa77.html",encoding = "UTF8")
soup = BeautifulSoup(f, "html.parser")
result = soup.find_all(class_='article_body mg fs4')
a=[]
for i in result:
    a.append(i.get_text())
f = open("c:\\data\\mytext23.txt","w")
f.write(str(a))
f.close()
