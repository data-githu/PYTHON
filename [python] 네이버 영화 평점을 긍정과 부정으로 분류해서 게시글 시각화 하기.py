# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:22:55 2021

@author: Owner
"""

■ 145.  네이버 영화 평점을 긍정과 부정으로 분류해서 게시글 시각화 하기


문제431. 신성이가 받은 라라랜드 평가 게시글에서  평가 점수만 출력하시오
sample6_laland_review.txt

stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    print( int(i[6:8]) ) 

문제432. 라라랜드 평가글중에 평점이 6점이상인 글들만 출력하시오 !
stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()

for  i  in  stev2:
    if int(i[6:8]) >= 6:
        print ( i , end="" )

문제433.  라라랜드 평가글중에 평점이 6점 이상이면 pos 라는 비어있는 리스트에 해당 평가글을 append 되게하고 6점 미만이면 nag 라는 비어있는 리스트에 평가글이 append 되게하시오 !
stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )
print (pos)

문제434. 위의 pos 에 들어있는 긍정글들을 c 드라이브 밑에 project 밑에  pos_lala.txt 로 저장하시오 !
stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()

문제435.  6점 미만인 글들은 nag_lala.txt 로 c 드라이브 밑에 project 밑에 저장되게하시오 !
stev = open("c:\\data\\sample6_laland_review.txt", encoding="UTF8")
stev2 = stev.readlines()
pos =[]
nag =[] 
for  i  in  stev2:
    if int(i[6:8]) >= 6:
        pos.append( i[8:] )
    else:
        nag.append( i[8:] )

f = open("c:\\project\\pos_lala.txt", "w")
f.writelines(pos)
f.close()
f2 = open(c:\\project\\nag_lala.txt", "w")
f2.writelines(nag)
f2.close()

문제436.  그러면 위의 pos_lala_txt 의 글과 nag_lala.txt 의 글을 워드 클라우드로 각각 시각화 하시오 !
from wordcloud import WordCloud, STOPWORDS # 구두점 데이터 정제
import matplotlib.pyplot as plt  # 그래프 그리는 모듈
from os import path     #  os 에 있는 파일을 파이썬에서 인식하기 위해서
import re   #  데이터 정제를 위해서 필요한 모듈 
import numpy as np  
from PIL import Image  # 이미지 시각화를 위한 모듈 

# 워드 클라우드의 배경이 되는 이미지 모양을 결정
usa_mask = np.array(Image.open("c:\\project\\usa_im.png"))

# 워드 클라우드를 그릴 스크립트 이름을 물어봅니다. 
script = 'pos_lala.txt'

# 워드 클라우드 그림이 저장될 작업 디렉토리를 설정 
d = path.dirname("c:\\project\\")

# 기사 스크립트와 os 의 위치를 연결하여 utf8로 인코딩해서 한글 텍스트를 text 변수로 리턴한다.
text = open(path.join(d, "%s"%script), mode="r",encoding="CP949", errors='ignore' ).read()
file = open('c:/project/word.txt', 'r', encoding = 'utf-8')
word = file.read().split(' ')   # 어절별로 분리해서 word 에 담아 리스트로 구성한다. 
for i in word:
    text = re.sub(i,'',text)  #  re.sub('있다', '', '있다')
    
    
    
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
    


