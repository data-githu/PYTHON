# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:24:24 2021

@author: Owner
"""

■ 147. 이미지 스크롤링 하기 ( 네이버 이미지 검색) 

import  urllib.request   # 웹 url 을 파이썬이 인식할 수 있게 하는 패키지 
from  bs4  import  BeautifulSoup # html 코드에서 원하는 지점을 빨리 찾을 수 있게 만든 모듈
from selenium import webdriver # 손으로 클릭하는것을 컴퓨터가 하겠금 하는 모듈
from selenium.webdriver.common.keys import Keys 
import time  # 중간중간 sleep 을 주려고 

binary = 'C:\\chromedriver\\chromedriver.exe'  # 크롬 드라이버 위치 지정 

browser = webdriver.Chrome(binary)  # browser 객체 생성 

browser.get("https://search.naver.com/search.naver?where=image&amp;sm=stb_nmr&amp;")

elem = browser.find_element_by_id("nx_query") # 검색창 지점을 알아내서 elem 에 담는다

#find_elements_by_class_name("")  # 클래스 이름으로 찾을때 필요한 코드 

# 검색어 입력
elem.send_keys("아이언맨")  # 컴퓨터가 아이언맨 글씨를 직접 적는다.
elem.submit()             # 그리고 엔터를 친다.ㅏ 

# 반복할 횟수
for i in range(1,5):  #  end 키를 누루면서 아래로 내리는데 
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(5) # 슬립을 5초 주면서 5번 수행한다. 

time.sleep(5) # 5초 멈췄다가 

html = browser.page_source   # 현 페이지의 html 코드를 불러와서 
soup = BeautifulSoup(html,"lxml")   # BeautifulSoup을 이용할 수 있도록 파싱한다. 

def fetch_list_url():   #  이미지의 상세 url 가져오는 함수 
    params = []
    imgList = soup.find_all("img", class_="_img")  # img 테그의 클래스 이름 _img 로 접근
    for im in imgList:
        params.append(im["src"])  # src 의 값을 가져와서 params 에 append 합니다. 
    return params

def  fetch_detail_url():  #  상세 이미지 url 가져와서 이미지 다운로드하는 함수 
    params = fetch_list_url()
    #print(params)
    a = 1 
    for p in params:
        # 다운받을 폴더경로 입력
        urllib.request.urlretrieve(p, "c:/naver/"+ str(a) + ".jpg" )

        a = a + 1

fetch_detail_url()

browser.quit()

문제439. 마이크로 소프트 회사에서 만든 검색 페이지인 bing 에서 이미지 검색을 할 수 있도록 하는 웹스크롤링 코드를 작성하시오 ! 
딥러닝 수업 전까지 학습하고 싶은 이미지 두가지를 정해서 사진을 스크롤링하세요 ~ ( 한클래스 당 2000장)

■ bing 이미지 url 주소  
https://www.bing.com/images?FORM=Z9LH


import  urllib.request
from  bs4  import  BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
binary = 'C:\chromedriver/chromedriver.exe' 
 
browser = webdriver.Chrome(binary)
 
browser.get("https://www.bing.com/images?FORM=Z9LH")
elem = browser.find_element_by_id("sb_form_q")
 
 
elem.send_keys("꽃")
time.sleep(5)   # 검색어 입력 후 바로 엔터를 치면 통합검색창으로 넘어가서 5초 sleep
elem.submit()     
 
 
for i in range(1,5):
    browser.find_element_by_xpath("//body").send_keys(Keys.END)
    time.sleep(10)
 
time.sleep(10)
 
html = browser.page_source
soup = BeautifulSoup(html,"lxml")
 
 
def fetch_list_url():
    params = []
    imgList = soup.find_all("img", class_="mimg")
    for im in imgList:
        params.append(im["src"])
    return params
 
 
def  fetch_detail_url():
    params = fetch_list_url()
    a = 1
    for p in params:
        urllib.request.urlretrieve(p, "c:/bingImages/"+ str(a) + ".jpg" )
 
        a = a + 1
 
fetch_detail_url()
 
browser.quit()
