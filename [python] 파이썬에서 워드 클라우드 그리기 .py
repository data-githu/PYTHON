# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:22:22 2021

@author: Owner
"""

■  144. 파이썬에서 워드 클라우드 그리기 

 웹스크롤링한 데이터를 분석을 하는데  분석하는 방법 

   1.  회사의 신제품이 출시되었을때 소비자들의 반응을 살펴보고자 할 때 ( 기업 ) ---> 감정분석 

   2.  시기별 사회현상을 파악하고자 할 때 (국가)

   3.  인공지능 상담원(딥러닝의 RNN)을 만들기 위한 자연어 처리 학습 데이터로 웹스크롤링한 데이터를 활용

   4.  인공지능의 눈이라고 할 수 있는 딥러닝의 CNN 의 신경망의 학습 자료로 이미지 데이터가 활용 

 * 빅데이터 기사 문제:  데이터의 구조적 관점에서 3가지로 나뉜다.(P1-4)
       
      1. 정형 데이터 : 정형화된 스키마 구조. DBMS 에 저장될 수 있는 구조
                 예: Oracle 의 emp 테이블, MySQL, MSSQL 의 테이블 

       2. 반정형 데이터: 데이터 내부의 데이터 구조에 대한 메타정보가 
                              포함된 구조의 데이터
                  예: html 문서, xml 문서                       

       3. 비정형 데이터 : 웹스크롤링 기술로 수집해서 모은 데이터 
                   예:  텍스트 문서, 이미지, 동영상


문제423.  어제 조선일보에서  봉사로 검색했을 때 다운 받았던 기사에서 가장 많이 나오는 단어(어절)가 무엇인가 ?

stev = open("c:\\data\\bongsa.txt", encoding="UTF8")
stev2 = stev.read().split()  # 어절별로 분리해서 리스트에 담는다.
stev2.sort() # 리스트안의 요소들을 정렬

from  collections  import  Counter 
count_list = Counter(stev2)  #stev2 리스트안의 어절별로 각각 몇건씩 있는지
print (count_list)                # 정리를 합니다. 
result = count_list.most_common(30)  # top 30개만 추출 
print (result)

[('수', 33), ('있다.', 28), ('했다.', 24), ('등', 22), ('–', 17), 
('비자', 17), ('더나은미래', 16), ('봉사', 16), ('마스크', 15), 
('있는', 15), ('봉사활동', 14), ('이주', 13), ('대표는', 12), 
('지난', 12), ('하는', 12), ('&', 11), ('Copyrights', 11), (
'futurechosun.com,', 11), ('ⓒ', 11), ('대한', 11), ('된다.', 11), 
('함께', 11), ('활동', 11), ('활동을', 11), ('금지', 10), ('밝혔다.', 10), 
('위해', 10), ('프로젝트를', 10), ('해외', 10), ('더', 9)]

문제424.  위의 결과를 for loop 문을 이용해서 아래와 같이 출력하시오 !
 수    33
 있다 28
 했다 24 
 등    22
  :      :

for i in result:
    print(i[0],i[1])

문제425.  어제 마지막 문제로 스크롤링 했던 영화 평가 게시글들에서 위와 같이 가장 많이 나오는 어절이 무엇인지 출력하시오 !
             ( 다희의 타이타닉)


문제426.  웹스크롤링을 한 데이터로 감정분석(긍정적, 부정적)을 하기 위해  신성이 형의 라라랜드 영화 평가를 다운로드 해서 c 밑에 data 밑에 두고 가장 많이 나오는 단어가 무엇인지 확인합니다.

positive-words2.txt
negative-words2.txt

문제427.  영화 라라랜드에서 긍정적인 단어가 몇건이 나오는지 출력하시오!
positive = open('c:\\data\\positive-words2.txt', encoding='CP949')
pos = positive.read().split('\n') # positive 에서 행별로 분리해서 pos 에 담는데
                                        # pos 는 리스트 입니다. 
                                        # pos 리스트에 긍정단어들이 들어있습니다
stev = open('c:\\data\\sample6_laland_review.txt', encoding='UTF8')
stev2 = stev.read().split() # 스티븐 잡스 연설문을 어절별로 분리하여 
                                # stev2 에 입력했는데 stev2 도 리스트이고
                                # stev2 리스트에는 스티븐 잡스 연설문이 어절별로
                                # 분리되어서 저장되어 있습니다.
cnt = 0
for i in stev2:  # stev2 에서 단어들을 하나씩 빼옵니다. 
    if i.lower() in pos:  # i의 단어가 pos 긍정단어 리스트에 존재하면 
        cnt += 1     # cnt 를 1씩 증가 시킵니다. 
print(cnt)

문제428. 라라랜드 영화 평가에 부정단어는 몇개가 있고 단어들은 무엇인지 출력하시오 !
positive = open('c:\\data\\negative-words2.txt', encoding='CP949')
pos = positive.read().split('\n') # positive 에서 행별로 분리해서 pos 에 담는데
                                        # pos 는 리스트 입니다. 
                                        # pos 리스트에 긍정단어들이 들어있습니다
stev = open('c:\\data\\sample6_laland_review.txt', encoding='UTF8')
stev2 = stev.read().split() # 스티븐 잡스 연설문을 어절별로 분리하여 
                                # stev2 에 입력했는데 stev2 도 리스트이고
                                # stev2 리스트에는 스티븐 잡스 연설문이 어절별로
                                # 분리되어서 저장되어 있습니다.
cnt = 0
for i in stev2:  # stev2 에서 단어들을 하나씩 빼옵니다. 
    if i.lower() in pos:  # i의 단어가 pos 긍정단어 리스트에 존재하면 
        cnt += 1     # cnt 를 1씩 증가 시킵니다.
        print (i, cnt)
print(cnt)


문제429.  영화 라라랜드의 평가글들을 워드 클라우드로 시각화 하시오!
예제.  파이썬에서 워드 클라우드 그리기 

1. 아나콘다 프롬프트 창을 열고  wordcloud 패키지 설치

conda  install  wordcloud
 
   또는 

pip  install   wordcloud

성공적으로 설치되면 아래의 메세지가 뜹니다. 

Successfully installed wordcloud-1.8.1

2. c 드라이브 밑에 project 폴더를 생성 


3. project 폴더 밑에  4가지 파일을 둡니다.

   -  usa_im.png
   -  s_korea.png
   -  word.txt
   -  중앙일보 스크롤링했던 기사 파일 my_text21.txt 

# 텍스트마이닝 데이터 정제

from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'sample6_laland_review.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를
# text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r", encoding="utf-8").read()
print(text)

# 파이썬이 인식할 수 있는 한글 단어의 갯수를 늘리기 위한 작업 
file = open('c:/project/word.txt', 'r', encoding = 'utf-8')
word = file.read().split(' ')   # 어절별로 분리해서 word 에 담아 리스트로 구성한다. 
for i in word:
    text = re.sub(i,'',text)  #  re.sub('있다', '', '있다')  # <-- 라라랜드 게시글의 있다를 '' 으로
                                                                  # 으로 대체하겠다. 
# 설명: 일반적인 문장에서 자주 나오는 단어들을 전부  '' 로 아래와 같이 대체하려고 하는데
# 아래 처럼 일일히 다 써주면 너무 코딩이 많으니까 for 문을 이용해서 쉽게 한다. 
#re.sub('있다', '', '있다')
#re.sub('하지만', '', '하지만')  
 


# 워드 클라우드를 그린다. 
wordcloud = WordCloud(font_path='C://Windows//Fonts//gulim', # 글씨체
                      stopwords=STOPWORDS,   # 마침표, 느낌표,싱글 쿼테이션 등을 정제
                      max_words=1000, # 워드 클라우드에 그릴 최대 단어갯수
                      background_color='white', # 배경색깔
                      max_font_size = 100, # 최대 글씨 크기 
                      min_font_size = 1, # 최소 글씨 
                      mask = usa_mask, # 배경 모양 
                      colormap='jet').generate(text).to_file('c:\\project\\lala_cloud.png')
                  # c 드라이브 밑에 project 폴더 밑에 생성되는 워드 클라우드 이미지 이름
  
plt.figure(figsize=(15,15))  # 가로 15, 세로 15 사이즈 
plt.imshow(wordcloud, interpolation='bilinear')  # 글씨가 퍼지는 스타일 
plt.axis("off")  # 축표시 없음






