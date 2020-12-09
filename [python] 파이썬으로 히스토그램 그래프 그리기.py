# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:53:33 2020

@author: Owner
"""

■ 파이썬으로 히스토그램 그래프 그리기

 히스토그램 그래프는 계급을 가로축에 도수를 세로축에 나타낸 뒤 각 계급의 크기를 가로의 길이로 하고 도수를 세로의 길이로 하는 직사각형을 차례대로 그려서 나타낸 그래프 입니다.


예제 : 
	1. 평균이 150, 표준편차가 5인 초등학생 10만명의 키를 생성한다.
import numpy as np
height = np.random.randn(100000)*5+150

	2. 계급의 크기를 나타내는 가로의 길이를 설정
bins = [142,144,146,148,150,152,154,156,158,160]

bins = list(range(142,161,2))
print(bins)

	3. 히스토그램 그래프의 세로축에 해당하는 도수(건수)를 구하는 코드
hist, bins = np.histogram(height, bins)
print(hist, bins)

#[ 6026  9717 13322 15530 15439 13288  9639  6126  3200] [142 144 146 148 150 152 154 156 158 160]

	4. 위의 데이터를 가지고 히스토그램 그래프를 그린다.
import numpy as np
import matplotlib.pyplot as plt
height = np.random.randn(100000)*5+150
bins = list(range(142,161,2))
hist, bins = np.histogram(height, bins)
plt.hist(height, bins)


히스토그램 꾸미기
import numpy as np
import matplotlib.pyplot as plt
height = np.random.randn(100000)*5+150
bins = list(range(142,161,2))
hist, bins = np.histogram(height, bins)
plt.grid()
plt.hist(height, bins, rwidth=0.9, alpha = 0.7, color = 'blueviolet') 

#rwidth : 히스토그램의 넓이, alpha : 투명도

문제318. 우리반 나이 데이터를 가지고 히스토그램 그래프를 그리시오.
x축의 계급(간격)은 24-44 (2살간격으로)
import numpy as np
import matplotlib.pyplot as plt
import csv
file=open('c:\\data\\emp1222.csv')
emp_122 =csv.reader(file)
age=[]
for emp_list in emp_122:
    age.append(int(emp_list[2]))
bins = list(range(24,45,2))
plt.grid()
plt.hist(age, bins, rwidth=0.9, alpha = 0.7, color = 'blueviolet') 