# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:43:52 2020

@author: Owner
"""
■ 151. 이미지를 숫자로 변환하는 방법 (개와 고양이)
개와 고양이 사진을 분류하는 인공신경망을 만드려면 개와 고양이 사진을 각각 2000장씩 내려 받아서 숫자로 변환하는 작업을 해줘야 합니다.

예제1. 머신러닝 데이터 분석의 세계대회인 캐글에서 개와 고양이 사진을 내려받습니다.

예제2. c 드라이브 밑에 images2 폴더에 강아지 사진 30장을 저장하시오.

예제3. c 드라이브 밑에 images2 라는 폴더에 있는 이미지 이름을 가져오는 함수를 image_load2 라는 함수로 생성하시오.
import os
path = "c:\\images2"

def image_load2(path):
    file_list=os.listdir(path)
    return file_list
print(image_load2(path))

예제4. 위의 개사진 이름에서 숫자만 출력하시오!
import os
import re 
test_images='c:\\images2'

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) 
        file_name.append(a)
    return file_name
print(image_load2(test_images))

예제5. 위의 결과를 정렬하시오!
import os
import re 
test_images='c:\\images2'

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) 
        file_name.append(int(a))
        file_name.sort()
    return file_name
print(image_load2(test_images))

예제6. 아래와 같이 절대경로와 확장자가 붙어서 출력되게 하시오!
import os
import re 
test_images='c:\\images2'

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) 
        file_name.append(int(a))
        file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append('c:\\images2\\dog' +str(k)+'.jpg')
    return file_res

print(image_load2(test_images))

예제7.  위의 개사진 이미지들을 opencv 와 numpy 를 이용해서 숫자로 변환하고 numpy  array 로 반환되게 하시오 !
import numpy as np
import cv2
import os
import re 
test_images='c:\\images2'

def image_load2(path):
    file_list = os.listdir(path) 
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) 
        file_name.append(int(a))
        file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append('c:\\images2\\dog.' +str(k)+'.jpg')
    image = []
    for h in file_res:
        img=cv2.imread(h)
        image.append(img)
        
    return np.array(image)

print(image_load2(test_images))

