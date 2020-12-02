# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:09:45 2020

@author: Owner
"""


■ 45. 파이썬 모듈 임포트 이해하기 ① import
이미 만들어져 있는 어떤 함수를 우리가 작성하는 코드에서 자유롭게 활용할 수 있으려면 해당 함수가 포함된 모듈을 임폴트해야합니다.
임폴트하는 방법은 다음과 같습니다.

import 모듈이름
from 패키지 import 모듈이름
import 패키지이름.모듈이름

예제 : 아래와 같이 우리가 만든 모듈이 아니라 다른 사람이 만든 모듈을 임폴트해서 써보았는데 이 모듈은 어디에 있는 걸까요? 
import pandas
import numpy

위와 같이 패키지 이름을 안주고 모듈만 import 했는데 잘 실행이 되었습니다.
위와 같은 모듈은 어떤 모듈입니까?

	1. 파이썬 내장 모듈
	2. sys.path 에 정의되어 있는 모듈

*import 를 만나면 파이썬 모듈을 찾는 순서
	1. 파이썬 내장 모듈에 있는지 확인한 후
	2. sys.path 에 정의되어 있는 모듈을 확인합니다.

*sys.path 에 정의된 디렉토리가 무엇인지 확인하는 방법
import sys
for i in sys.path:
	print(i)
	
*site-packages란 무엇인가?
site=packages 란 파이썬의 기본 라이브러리 패키지 외에 추가적인 패키지를 설치하는 디렉토리 입니다.
site-packages 디렉토리에 여러가지 소프트웨어가 사용할 공통 모듈을 넣어두면 물리적인 장소에 구애받지 않고 모듈에 접근하여 반입할 수 있습니다.

아래의 명령어가 수행되려면 아래의 명령어를 수행하는 스크립트가 c:\\Users\\stu 밑에 있어야 합니다. 왜냐하면 my_loc 폴더가 바로 c:\\Users\\stu 밑에 있기 때문입니다.

from my_loc import my_cal

그런데 c:\\Users\\stu 가 아니더라도 다른 디렉토리에서라도 
from my_loc import my_cal 명령어를 자유롭게 실행하려면 my_loc 폴더가 c:\Users\stu\anaconda3\lib\site-packages 밑에 있으면 됩니다.

문제151. my_loc 폴더를 site-packages 폴더 밑에 두세요.
c:\Users\stu\anaconda3\lib\site-packages
from my_loc import my_cal

print(my_cal.add_number(1,2))
print(my_cal.gob_number(1,2))
print(my_cal.devide(10,2))


■ 46. numpy 모듈 이해하기

*numpy 모듈이란? python 언어에서 기본적으로 지원하지 않는 배열(array) 또는 행렬(matrix)의 계산을 쉽게 해주는 라이브러리 입니다.
딥러닝에서 많이 사용하는 선형대수학에 관련된 수식들을 python에서 쉽게 프로그래밍 할 수 있게 해줍니다.

예제 :  아래의 행렬을 만드시오!

	1. 리스트로만 했을 때
a = [ [1,2],[4,7]]
print(a)



	2. numpy array 로 했을 때
import numpy as np
a = [ [1,2],[4,7]]
a2 = np.array(a) # a리스트를 numpy 배열로 구성함
print(a2)


문제152. 아래의 행렬의 합을 출력하시오!
import numpy as np
a = [ [1,2],[4,5]]
b = [ [3,1],[6,2]]

a2 = np.array(a)
b2 = np.array(b)
print(a2+b2)


문제153. 아래의 행렬의 합을 출력하시오!
import numpy as np
a = [ [6,3,4],[5,1,7]]
b = [ [4,5,7],[9,20,4]]

a2 = np.array(a)
b2 = np.array(b)
print(a2+b2)

문제154. 아래의 행렬의 곱을 먼저 손으로 구하시오!
( 1 2 )  ◎   ( 2 1 )      = 1*2 + 2*3 = 8 , 1*1+2*4 = 9 
( 4 3 )        ( 3 4 )      = 4*2 + 3*3 = 17 , 4*1 + 3*4 = 16  
import numpy as np

a = [[1,2],[4,3]]
b = [[2,1],[3,4]]


a2 = np.array(a)
b2 = np.array(b)
print (np.dot(a2,b2))


문제155. 아래의 행렬의 곱을 구하시오!
(3,4,1)  ◎   (2,1)
(2,4,3)        (4,3)
               (6,7)

import numpy as np

a = [[3,4,1],[2,4,3]]
b = [[2,1],[4,3],[6,7]]


a2 = np.array(a)
b2 = np.array(b)
print (np.dot(a2,b2))

■ 47. numpy 모듈 사용하기2

numpy 모듈로 최대값, 최소값, 평균값, 중앙값, 최빈값, 분산값, 표준편차, 공분산값, 상관계수의 통계값들을 쉽게 출력할 수 있습니다.

예제1. 아래의 리스트에서 최대값을 출력하시오!
a = [28, 23, 21, 29, 30, 40, 23, 21]

import numpy as np
a2 = np.array(a)
print(np.max(a2))

예제2. 아래의 리스트에서 최대값, 최소값, 평균값, 최빈값, 중앙값을 출력하시오!
a = [28, 23, 21, 29, 30, 40, 23, 21, 21]

import numpy as np
from scipy.stats import mode 
a2 = np.array(a)
print(np.max(a2))
print(np.min(a2))
print(np.mean(a2)) # 평균값
print(np.median(a2)) # 중앙값
print(mode(a2)) # 최빈값
