# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:13:20 2020

@author: Owner
"""



■ 48. 파일 열고 닫기 (open, close)


파일은 텍스트 파일과 바이너리 파일 두가지 종류가 있습니다.
텍스트 파일은 사람이 읽을 수 있는 글자로 저장된 파일이고 바이너리 파일은 컴퓨터가 읽고 이해할 수 있는 이진 데이터를 기록한 파일입니다.
예를들어 윈도우에서 제공하는 메모장 프로그램을 이용하여 내용을 적고 저장하면 텍스트 파일로 저장됩니다. 
이미지 뷰어로 볼 수 있는 jpg 이미지 파일은 이진 데이터를 jpg 형식의 파일로 저장한 바이너리 파일입니다
파이썬에 파일을 다루기 위해서 가장 먼저 해야할 일은 파일을 오픈 하는 것입니다.
파일을 오픈하기 위해서는 open( ) 함수를 이용합니다.

문법 : 
open (파일이름, 모드)
모드                  설명
r                       텍스트 모드로 읽기
w                      텍스트 모드로 쓰기
rb                     바이너리 모드로 읽기
rw                     바이너리 모드로 쓰기

예제1. 이미지 파일을 파이썬에서 여는 방법
	1. lena.png 파일을 내려받아 c:\\data\\ 밑에 저장합니다.
	2. 아래의 코드를 실행합니다.
import PIL.Image as pilimg  # 이미지를 파이썬에 시각화 하기 위한 모듈을 임폴트 합니다.
import numpy as np
import matplotlib.pyplot as plt # 데이터 시각화 전문 모듈을 임폴트 합니다.

im = pilimg.open('c:\\data\\lena.png') 
pix = np.array(im) #넘파이 배열로 변경합니다.
plt.imshow(pix)


문제156. 폐사진을 파이썬에서 시각화 하시오!
import PIL.Image as pilimg #이미지를 파이썬에 시각화 하기 위한 모듈
import numpy as np
import matplotlib.pyplot as plt

im = pilimg.open('c:\\data\\2.png') 
pix = np.array(im)
plt.imshow(pix)
