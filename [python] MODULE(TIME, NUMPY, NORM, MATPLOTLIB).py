# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:07:07 2020

@author: Owner
"""


■ 43. 파이썬 모듈 이해하기
파이썬에서는 각각의 소스 파일을 일컬어 모듈이라고 합니다.
이미 만들어져 있고 안정성이 검증된 함수들을 성격에 맞게 하나의 파일로 묶어 놓은 것을 모듈이라고 합니다.
외부의 모듈에 있는 함수를 사용하려면 이 모듈을 먼저 우리 코드로 가져와서 자유롭게 사용할 수 있도록 해야하는데 이런 일을 파이썬에서는 모듈을 import 한다라고 합니다.

예제 : 
import time # time 모듈을 임폴트 합니다.
print('5초간 프로그램을 정지합니다.')
time.sleep(5) # 5초동안 멈춰있는 것입니다.
print('5초가 지났습니다.')

문제142. 서울시 초등학생 백만명의 키를 모집단을 구성하는데 평균키가 148.5 이고 표준편차가 30인 모집단을 만드시오.
import numpy as np
std = 30
avg = 148.5
N = 100000

population=np.random.randn(N) * std + avg
print(population)

문제143. 위의 모집단에서 100명을 표본으로 추출하여 100명의 평균키를 비어있는 리스트 a에 입력하는 작업을 10000번 수행하여 a 리스트에 10000개의 표본의 평균키가 입력되게 하시오!
import numpy as np

std = 30
avg = 148.5
N = 100000
a= [ ]

population=np.random.randn(N) * std + avg
for i in range(1,10001):
    result  = np.random.choice(population, 100).mean()
    a.append(result)
print(a)
print(len(a))

문제144. 통계학을 전문으로 구현하는 모듈인 scipy 모듈을 임폴트하여 위의 표본의 평균값에 대한 확률밀도값을 출력하시오!
import numpy as np
from scipy.stats import norm # scipy의 stats 패키지로 부터 norm 이라는 모듈을 import 하시오.

std = 30
avg = 148.5
N = 100000
a= [ ]

population=np.random.randn(N) * std + avg

for i in range(1,10001):
    result  = np.random.choice(population, 100).mean()
    a.append(result)
x=np.arange(140,160,0.001) #140-160까지 0.001 간격으로 숫자를 생성
y= norm.pdf(x, np.mean(a), np.std(a)) #초등학생 키의 표본퍙균값들에 대한 확률밀도함수 값이 출력됩니다.
print(y)

문제145. 데이터 시각화 전문 모듈인 matplotlib를 임폴트 하여 위의 표본 평균값 10000개의 데이터를 시각화 하시오!
import numpy as np
from scipy.stats import norm # scipy의 stats 패키지로 부터 norm 이라는 모듈을 import 하시오.
import matplotlib.pyplot as plt #matplotlib 모듈안에 pyplot 라는 함수를 사용하겠습니다.
std = 30
avg = 148.5
N = 100000
a= [ ]

population=np.random.randn(N) * std + avg

for i in range(1,10001):
    result  = np.random.choice(population, 100).mean()
    a.append(result)
x=np.arange(140,160,0.001) #140-160까지 0.001 간격으로 숫자를 생성
y= norm.pdf(x, np.mean(a), np.std(a)) #초등학생 키의 표본퍙균값들에 대한 확률밀도함수 값이 출력됩니다.
plt.plot(x,y,color='blue')
plt.show()

문제146. 위의 확률밀도함수 그래프의 아래쪽 영역도 색깔로 채우시오!
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
std = 30
avg = 148.5
N = 100000
a= [ ]

population=np.random.randn(N) * std + avg

for i in range(1,10001):
    result  = np.random.choice(population, 100).mean()
    a.append(result)
x=np.arange(140,160,0.001) 
y= norm.pdf(x, np.mean(a), np.std(a)) 
plt.plot(x,y,color='blue')
plt.fill_between(x,y,interpolate = True, color ='skyblue', alpha=0.7)
#설명 : plt 모듈안의 fill_between 함수를 이용해서 확률밀도함수 그래프의 아래 영역을 색깔로 채우는데 interpolate = True
plt.show()

문제147. 위에서 그린 확률밀도함수 그래프의 색깔을 변경하고 그래프를 사진으로 첨부해서 올리세요~
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
std = 30
avg = 148.5
N = 100000
a= [ ]

population=np.random.randn(N) * std + avg

for i in range(1,10001):
    result  = np.random.choice(population, 100).mean()
    a.append(result)
x=np.arange(140,160,0.001) 
y= norm.pdf(x, np.mean(a), np.std(a)) 
plt.plot(x,y,color='blueviolet')
plt.fill_between(x,y,interpolate = True, color ='violet', alpha=0.7)
#설명 : plt 모듈안의 fill_between 함수를 이용해서 확률밀도함수 그래프의 아래 영역을 색깔로 채우는데 interpolate = True
plt.show()
