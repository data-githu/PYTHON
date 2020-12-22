# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:35:26 2020

@author: Owner
"""

■ 150. 이미지를 숫자로 변환하는 방법(폐사진)
딥러닝 수업을 할 때 이미지를 인공 신경망에 넣어서 학습을 시키는데 인공 신경망에 사진을 넣을 때 숫자로 변환을 해서 넣어야 합니다.

사진 -----------> 인공신경망 -----------> 폐결절, 정상폐, 폐암 (7-10가지로 분류 판정)

예제1. c 드라이브 밑에 images 폴더에 있는 사진들의 이름을 불러오는 함수를 생성
import os
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    return file_list

print(image_load(test_images))

예제2. 위의 결과에서 숫자만 나오게 함수의 코드를 수정하시오!
import os
import re #데이터 정제를 전문으로 하는 모듈
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path) #해당 디렉토리의 파일명을 추출한다.
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i) # i의 값중에서 숫자가 아닌 것들은 싱글 두개를 붙인 것인 null 로 변경하시오.
        file_name.append(a)
    return file_name
print(image_load(test_images))

문제475. 위에서 출력된 리스트 안의 요소들은 문자입니다. 그런데 문자가 아니라 리스트의 요소들이 숫자가 되게 하세요!
import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
    return file_name
print(image_load(test_images))

문제476. 위의 리스트의 요소가 ascending 하게 정렬되게 하시오!
import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
        file_name.sort()
    return file_name
print(image_load(test_images))


문제477. 위의 함수의 코드를 추가해서 아래와 같이 출력되게 하시오!
['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png', '15.png', '16.png', '17.png', '18.png', '19.png', '20.png']

import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
        file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append(str(k)+'.png')
    return file_res
print(image_load(test_images))

문제478. 위의 함수의 코드를 수정해서 아래와 같이 이름 앞에 절대경로가 붙게 하시오!
['c:\\images\\1.png', 'c:\\images\\2.png', 'c:\\images\\3.png', 'c:\\images\\4.png', 'c:\\images\\5.png', 'c:\\images\\6.png', 'c:\\images\\7.png', 'c:\\images\\8.png', 'c:\\images\\9.png', 'c:\\images\\10.png', 'c:\\images\\11.png', 'c:\\images\\12.png', 'c:\\images\\13.png', 'c:\\images\\14.png', 'c:\\images\\15.png', 'c:\\images\\16.png', 'c:\\images\\17.png', 'c:\\images\\18.png', 'c:\\images\\19.png', 'c:\\images\\20.png']

import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
        file_name.sort()
    file_res=[]
    for k in file_name:
        file_res.append('c:\\images\\' +str(k)+'.png')
    return file_res
print(image_load(test_images))


예제3. 폐사진 이미지를 숫자로 변환하기 위하여 필요한 파이썬 모듈을 install 하시오!

아나콘다 프롬프트 창을 엽니다.
conda install opencv

위의 명령어로 했을 때 오류가 나면 아래와 같이 하세요.

pip install opencv-python

설명 : opencv 모듈은 이미지를 파이썬에서 숫자로 변환하고 다양한 이미지 처리를 할 수 있게 해주는 기술을 제공하는 함수입니다.

예 : 구글지도, 네이버지도, 카카오지도에 보면 street veiw에서 사람의 얼굴, 자동차 번호판을 모자이크 처리를 해줘야 합니다.

예제4. 위에서 설치한 opencv 모듈을 이용해서 폐사진을 숫자로 변환합니다.
import cv2 #opencv import
import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
        file_name.sort()
        
    file_res=[]
    for k in file_name:
        file_res.append('c:\\images\\' +str(k)+'.png')
        
    image=[]    
    for h in file_res:
        img = cv2.imread(h)
        image.append(img)
        
    return image    

print(image_load(test_images))

예제5. 위의 숫자로 변환한 리스트를 인공 신경망에 넣기 위해서 numpy 모듈의 array 형태로 제공을 해줘야 합니다.
import numpy as np #행렬 연산을 쉽고 빠르게 할 수 있게 해주는 모듈
import cv2 
import os
import re
test_images='c:\\images'

def image_load(path):
    file_list = os.listdir(path)
    file_name=[]
    for i in file_list:
        a=re.sub('[^0-9]','',i)
        file_name.append(int(a))
        file_name.sort()
        
    file_res=[]
    for k in file_name:
        file_res.append('c:\\images\\' +str(k)+'.png')
        
    image=[]    
    for h in file_res:
        img = cv2.imread(h)
        image.append(img)
        
    return np.array(image)    

print(image_load(test_images))