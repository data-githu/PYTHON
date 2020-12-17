# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:48:34 2020

@author: Owner
"""

*빅데이터 수집을 위해 반드시 알아야 할 필수 기술 ? 웹스크롤링

*웹스크롤링을 위해서 사용한 파이썬 모듈? Beautiful soup 모듈

*웹스크롤링을 편하게 잘하기 위한 방법은?
크롬의 개발자 모드(F12) 로 들어가서 화살표를 이용해서 웹상에서 스크롤링하기 원하는 지점의 html 클래스 이름을 빠르게 찾을 수 있습니다.


■ 142. 웹스크롤링 실전 1단계 (EBS 레이디 버그 게시판)

예제1 : ebs 레이디 버그 시청자 게시판의 url 을 가지고 직접html 문서를 내려받을 수 있도록 코드를 구현 (어제는 우리가 ctrl + s 를 누르고 웹페이지를 우리 피시에 저장하고 구현했는데 오늘은 그렇게 하지 않고 웹에서 바로 html 문서를 내려 받을 수 있도록 구현)
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
print(result)


예제2. 위에서 긁어온 html 코드를 Beautiful soup 의 함수를 이용해서 웹스크롤링을 할 수 있도록 Beautiful soup 을 쓸 수 있게 파싱하시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
print(soup)


예제3. 지금 페이지의 시청자 게시판의 글 내용에 해당하는 부분의 태그와 클래스 이름을 알아내시오!
<p class_="con"> 재미있다 </p>


예제4. <p> 중에 class 가 con 에 해당하는 부분을 스크롤링 하세요!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result2 = soup.find_all('p', class_ ="con")
print(result2)


예제5. 위의 결과에서 html 문서 말고 한글 텍스트만 가져오시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result2 = soup.find_all('p', class_ ="con")
for i in result2:
	print(i.get_text())


예제6. 위에서 출력되고 있는 텍스트들이 좀 더 깔끔하게 나오게 하시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result2 = soup.find_all('p', class_ ="con")
for i in result2:
	print(i.get_text(" ",strip=True))

예제7. 위에서 출력되고 있는 텍스트들이 params 라는 비어있는 리스트에 담기게 하시오!
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")
result2 = soup.find_all('p', class_ ="con")
params=[]
for i in result2:
	params.append(i.get_text(" ",strip=True))
print(params)

예제8. 게시글을 올린 날짜를 스크롤링하기 위해 게시글 날짜가 있는 html 문서에 태그 이름과 클래스 이름을 확인하시오!
태그 이름은 span 이고 클래스 이름은 date 입니다.

예제9. 위의 날짜를 모두 스크롤링해서 params2 라는 리스트에 담으시오!
#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")

#2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
result2 = soup.find_all('p', class_ ="con")
result3 = soup.find_all('span', class_ ="date")
#3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.
params=[]
params2=[]
for i in result2:
	params.append(i.get_text(" ",strip=True))
print(params)
for i in result3:
    params2.append(i.get_text(" ",strip=True))
print(params2)


예제10. 위의 날짜와 본문 내용이 아래와 같이 출력되게 하시오!
2020.09.05 21:19 벌써 가을 인길요~
2020.09.04 18:14 가을이 빨리 되면 좋겠어요

#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(list_url)
result = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(result, "html.parser")

#2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
result2 = soup.find_all('p', class_ ="con")
result3 = soup.find_all('span', class_ ="date")

#3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.
params=[]
params2=[]
for i in result2:
	params.append(i.get_text(" ",strip=True))
for i in result3:
          params2.append(i.get_text(" ",strip=True))

#4. 날짜와 본문을 같이 출력합니다.
for k,j in zip(params, params2):
    print(j+' '+k)

예제11. 레이디 버그 게시판 전체의 글을 다 스크롤링해서 예제 10번의 결과처럼 출력되게하세요!
http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=1&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=2&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&
http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=3&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&


예제12. 아래의 결과출력하는데 페이지 번호가 1-22번까지 변경되어서 출력되게 하시오!
for i in range(1,23):
    print('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819')

예제13. 예제12번 코드를 예제10번 코드에 적용해서 레이디 버그 전체 게시판의 글들이 날짜와 함께 출력되게 하시오!
#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

list_url = []
for i in range(1,23):
    list_url.append('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819')
for m in list_url:
    url = urllib.request.Request(m)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    
    #2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result2 = soup.find_all('p', class_ ="con")
    result3 = soup.find_all('span', class_ ="date")
    #3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.
    params=[]
    params2=[]
    for i in result2:
    	params.append(i.get_text(" ",strip=True))
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
    for k,j in zip(params, params2):
        print(j+' '+k)
    
설명 : 위의 params와 params 가 for 문 안쪽에 있기 때문에 페이지 번호가 돌 때 마다 params 리스트  안의 내용이 새로운 날짜와 내용으로 변경되게 됩니다.


예제14. params 와 params2 에 레이디 버그 시청자 게시판 모든 게시날짜와 본문 내용이 들어가도록 코드를 수정하시오!
#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
params=[]
params2=[]
list_url = []
for i in range(1,23):
    list_url.append('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819')
for m in list_url:
    url = urllib.request.Request(m)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    
    #2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result2 = soup.find_all('p', class_ ="con")
    result3 = soup.find_all('span', class_ ="date")
    #3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.

    for i in result2:
    	params.append(i.get_text(" ",strip=True))
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
for k,j in zip(params, params2):
    print(j+' '+k)

문제415. 레이디 버그 게시판의 전체 게시글은 총 몇건인가?   
#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
params=[]
params2=[]
list_url = []
for i in range(1,23):
    list_url.append('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819')
for m in list_url:
    url = urllib.request.Request(m)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    
    #2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result2 = soup.find_all('p', class_ ="con")
    result3 = soup.find_all('span', class_ ="date")
    #3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.

    for i in result2:
    	params.append(i.get_text(" ",strip=True))
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
for k,j in zip(params, params2):
    result4 = j+' '+k

print(len(params))
print(len(params2))


문제416. 게시글 429개 전체를 c드라이브 밑에 mytext34.txt 라는 이름으로 저장하시오!
*텍스트 파일을 저장하는 파이썬 코드
text = 'abcdefghigklmn'

f=open('c:\\data\\mytext34.txt','w',encoding = 'UTF8')
f.write(text)
f.close()

#1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request #웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
params=[]
params2=[]
list_url = []
f=open('c:\\data\\mytext34.txt','w',encoding = 'UTF8')
for i in range(1,23):
    list_url.append('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819')
for m in list_url:
    url = urllib.request.Request(m)
    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(result, "html.parser")
    
    #2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result2 = soup.find_all('p', class_ ="con")
    result3 = soup.find_all('span', class_ ="date")
    #3. 시청자 게시판의 날짜오 본문을 params와 params2 리스트에 담습니다.

    for i in result2:
    	params.append(i.get_text(" ",strip=True))
    for i in result3:
        params2.append(i.get_text(" ",strip=True))
for k,j in zip(params, params2):
    f.write(j+' '+k + '\n')
f.close()

