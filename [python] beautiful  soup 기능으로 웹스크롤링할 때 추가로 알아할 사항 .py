# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:02:46 2021

@author: Owner
"""

■ beautiful  soup 기능으로 웹스크롤링할 때 추가로 알아할 사항 

예제1.  웹스크롤링을 할 사이트에 접속합니다. 

https://futurechosun.com/

예제2.  위의 사이트에서 키워드 '봉사' 로 검색을 합니다.

https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC
https://futurechosun.com/page/2?s=%EB%B4%89%EC%82%AC
https://futurechosun.com/page/3?s=%EB%B4%89%EC%82%AC

예제3. 위의 첫페이지의 html 코드를 파이썬으로 불러오는 작업

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request  

#2. 첫페이지의 url 을 파싱합니다. 
list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
print(result)

#3. 웹스크롤링 전문 모듈인 beautiful soup 모듈을 이용할 수 있도록
#   내려받은 html 코드를 beautiful soup 을 이용할 수 있게 파싱합니다. 
#   이용할 수 있게 한다는것은 beautiful soup 의 함수인 find_all 을 이용해서 
#   태그 이름과 클래스 이름을 가지고 검색하기 원하는 지점을 빠르게 찾아가기
#  위해서 파싱한다는 것입니다. 

#앞의 코드들....
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
print(soup)

#4.  더나은 미래 첫페이지에 보이는 기사들 12개의 기사 url 을 알아내기 위해
#    태그 이름과 클래스 이름이 무엇인지 알아내시오 ~  ( href 가 있는 곳을 찾는다)

답 : 태그이름은 div 이고 클래스 이름은 elementor-post__title 입니다.

※ 중요설명:  href 와 가장 가까이 있는 태그 이름과 클래스 이름을 알아내야 합니다 

#5.  태그이름 div 에 클래스 이름  elementor-post__title 에 해당하는 beautiful soup 으로 파싱된 html 코드들을 모두 긁어오시오 

#앞의 코드들 ....
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
print (result1)

[ 
<div class="elementor-post__title"> 
<a href="https://futurechosun.com/archives/52491"> 
“편견에 주눅 들었던 결혼 이주 여성들… ‘봉사’로 자존감 되찾았다죠” </a></div>, 

<div class="elementor-post__title"> 
<a href="https://futurechosun.com/archives/47330"> 
[글로벌 이슈] 전 세계 코로나19 확산으로… 해외 봉사 ‘올스톱’ 위기 </a></div>,


설명:  지금 위의 result1 의 결과를 보면 리스트로 되어져있고 리스트 안에 각 요소들이 div 태그가  위아래로 있고 안쪽에 a 테그가 있는 구조로 beautifulsoup 으로 파싱된 html 코드들이 요소로 구성되어 있습니다. 우리가 원하는 지점은 a 태그인데 a 태그로 접근하려면 먼저 result1 리스트의 요소들을 하나씩 빼내와야 합니다.  리스트 안의 요소를 하나씩 빼내올려면 뭘 써야하나요  ?   for  loop 문을 사용해야 합니다.

#6.  result1 리스트의 요소들(beautiful soup 으로 파싱된 html 코드들)을  
      for  loop 문으로 하나씩 빼냅니다.

# 앞의 코드들 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
for  i   in  result1:
    print(i)

<div class="elementor-post__title"> 
<a href="https://futurechosun.com/archives/52491"> 
“편견에 주눅 들었던 결혼 이주 여성들… ‘봉사’로 자존감 되찾았다죠” </a></div>

#7.  빼낸 요소인 위의 html 코드 3줄에서 a 테그에 해당하는 부분만 가져오게 하시오

# 앞의 코드들 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
for  i   in  result1:
    print( i.find_all('a') )

[<a href="https://futurechosun.com/archives/46834"> 코이카, 의료 해외봉사단 대구·경북 지역에 투입한다 </a>]

# 8. 위의 a 테그의 html 코드들 담은 리스트는 요소를 딱 하나만 담고 있다.
# 그래서 리스트안의 그 요소만 딱 뽑아내서 출력을 하시오 ! 

힌트: 
a = [ 2 ]
print (a[0])  # 2 

# 앞의 코드들 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
for  i   in  result1:
    print( i.find_all('a')[0] )

<a href="https://futurechosun.com/archives/33380"> “이젠 봉사도 DIY!” 서울시, 대학생이 직접

#9.  그러면 뽑아낸 a 테그의 html 문서에서 href 의 값만 얻어내시오 ~

# 앞의 코드들 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
for  i   in  result1:
    print( i.find_all('a')[0].get("href") )

https://futurechosun.com/archives/52491           
https://futurechosun.com/archives/47330
https://futurechosun.com/archives/47004      
https://futurechosun.com/archives/46834
https://futurechosun.com/archives/43905

#10.  위의 상세기사 url 을  params 라는 리스트에 append 시킨다.
#앞의 코드들 ...
params = [ ]
for  i   in  result1:
     params.append( i.find_all('a')[0].get("href") )

print(lenparams))  # 24

# 11. 첫페이지만 가져오는게 아니라 1페이지부터 3페이지까지 24x3 = 72 
       페이지의 기사 url 을 params 리스트에 append 시키시오

#1. 웹스크롤링에 필요한 모듈을 임폴트 합니다. 
from  bs4  import  BeautifulSoup
import  urllib.request  

#2. 첫페이지의 url 을 파싱합니다. 

list_url = 'https://futurechosun.com/page/1?s=%EB%B4%89%EC%82%AC'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup = BeautifulSoup( result, "html.parser")
result1=soup.find_all('div',class_ ='elementor-post__title')
params = [ ]
for  i   in  result1:
     params.append( i.find_all('a')[0].get("href") )

print(len(params))

#12.  조선일보 더나은 미래 사이트는 사진을 클릭했을때도 상세기사로 가고
       기사제목을 클릭햇을때도 똑같이 상세기사로 가는 구조로 되어있어서
       상세기사 url 이 중복되어서 스크롤링이 되었습니다. 그래서 params 의
       요소들의 중복을 제거하시오 !

앞의 코드들 ..
    for  i   in  result1:
         params.append( i.find_all('a')[0].get("href") )

my_result = set(params)    # set 함수를 이용하면 중복이 제거가 된 요소들만 남는다.
my_result2 = list(my_result) #  중복이 제거된 요소들을 다시 리스트로 감싸서 리스트화
                                    #  시킨다. 
print(len(my_result2)) # 36 

# 13.  위의 코드들을 가지고  bs_scroll() 이라는 함수로 생성하시오 !
        print(len(my_result2))   ----> return  my_result2 로 변경하세요 ~~ 

from bs4 import BeautifulSoup
import urllib.request

def bs_scroll():    
    params1 = []
    
    for i in range(1,4):
            
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        stuff = BeautifulSoup( result, "html.parser")
        
        res1 = stuff.find_all('div',class_ ="elementor-post__title")
        
        for i in res1:
            params1.append(i.find_all('a')[0].get('href'))        
    
    return(params1)

print(len(bs_scroll()))  # 36


#14.  더나은미래의 상세기사 url 하나를 가지고 본문 기사를 출력하시오 !

https://futurechosun.com/archives/52491

from  bs4  import  BeautifulSoup
import  urllib.request
list_url = 'https://futurechosun.com/archives/52491'
url = urllib.request.Request(list_url) 
result = urllib.request.urlopen(url).read().decode("utf-8") 
soup=BeautifulSoup(result,"html.parser")
result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
for i in result:
    print(i.find_all('p'))



#15. 위의 코드를 가지고 bs_detail_scroll() 함수로 생성하시오 !

print( bs_detail_scroll() )  

답:
from  bs4  import  BeautifulSoup
import  urllib.request


def bs_detail_scroll():
    list_url = 'http://futurechosun.com/archives/52491'
    url = urllib.request.Request(list_url) 
    result = urllib.request.urlopen(url).read().decode("utf-8") 
    soup=BeautifulSoup(result,"html.parser")
    result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
    for i in result:
        print(i.find_all('p'))

print( bs_detail_scroll())

#16.  지금 방금 생성한 bs_detail_scroll()  함수의 코드안에 bs_scroll() 함수를 호출하는
       코드를 추가해서 bs_scroll() 함수가 리턴하는 36개의 상세기사 url 에 대한
       기사 본문이 전부 출력되게 하시오 !

from bs4 import BeautifulSoup
import urllib.request

def bs_scroll():    
    params1 = []
    
    for i in range(1,4):
            
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        stuff = BeautifulSoup( result, "html.parser")
        
        res1 = stuff.find_all('div',class_ ="elementor-post__title")
        
        for i in res1:
            params1.append(i.find_all('a')[0].get('href'))        
    
    return(params1)


def bs_detail_scroll():
    list_url = bs_scroll()
    for  i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup=BeautifulSoup(result,"html.parser")
        result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result:
            print(i.find_all('p'))

print( bs_detail_scroll())


#17.  bs_detail_scroll() 함수의 params2 리스트를 추가해서 params2 리스트에
       지금 위에서 출력하고 잇는 36개의 기사가 append 되게 하시오 !

from bs4 import BeautifulSoup
import urllib.request

def bs_scroll():    
    params1 = []
    
    for i in range(1,3):
            
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        stuff = BeautifulSoup( result, "html.parser")
        
        res1 = stuff.find_all('div',class_ ="elementor-post__title")
        
        for i in res1:
            params1.append(i.find_all('a')[0].get('href'))        
    
    return(params1)


def bs_detail_scroll():
    list_url = bs_scroll()
    params2 =[]
    for  i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup=BeautifulSoup(result,"html.parser")
        result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result:
            params2.append(i.find_all('p'))
    return params2        

print( bs_detail_scroll())

#18.  위에서 수집한 기사가 들어있는 params2 리스트의 내용을 c 드라이브 밑에
       data 밑에 bongsa.txt 로 생성되게 하시오 !

from bs4 import BeautifulSoup
import urllib.request

def bs_scroll():    
    params1 = []
    
    for i in range(1,2):
            
        list_url = 'https://futurechosun.com/page/'+str(i)+'?s=%EB%B4%89%EC%82%AC'
        url = urllib.request.Request(list_url) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        stuff = BeautifulSoup( result, "html.parser")
        
        res1 = stuff.find_all('div',class_ ="elementor-post__title")
        
        for i in res1:
            params1.append(i.find_all('a')[0].get('href'))        
    
    return(params1)


def bs_detail_scroll():
    list_url = bs_scroll()
    f = open('c:\\data\\bongsa.txt', 'w', encoding="UTF-8")
    for  i  in  list_url:
        url = urllib.request.Request(i) 
        result = urllib.request.urlopen(url).read().decode("utf-8") 
        soup=BeautifulSoup(result,"html.parser")
        result=soup.find_all('div', class_ ='elementor-element elementor-element-24e82692 elementor-widget__width-initial elementor-widget elementor-widget-theme-post-content')
        for i in result:
            for j in i.find_all('p'):
                f.write(str(j.get_text()) + "n")
    
  
    f.close()

print( bs_detail_scroll())


