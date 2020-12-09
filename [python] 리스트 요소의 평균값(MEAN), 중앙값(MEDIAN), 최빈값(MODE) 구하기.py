# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:21:42 2020

@author: Owner
"""

■ 데이터의 평균값, 중앙값, 최빈값 구하기

문제313. 아래의 엄마와 아이가 함께하는 수영교실의 나이의 평균값을 출력하시오!
[34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]

swim_age = [34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]
import numpy as np
a = np.array(swim_age)
b = np.mean(a) 
print(b)


문제314. 아래의 엄마와 아기의 수영교실의 중앙값을 출력하시오!
[34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]
swim_age = [34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]
import numpy as np
a = np.array(swim_age)
b = np.median(a) 
print(b)

문제315. 엄마와 아기의 수영교실의 최빈값을 출력하시오!
swim_age = [34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]
from scipy import stats
import numpy as np
a = np.array(swim.age)
result = stats.mode(a)
print(result)

문제316. 우리반 나이 데이터를 비어있는 리스트 a에 넣으세요.
import csv
file=open('c:\\data\\emp1222.csv')
emp_122 =csv.reader(file)
a=[]
for emp_list in emp_122:
    a.append(int(emp_list[2]))
print(a)

문제317. 우리반 나이 데이터의 평균값과 중앙값과 최빈값을 출력하시오!
from scipy import stats
import numpy as np

import csv
file=open('c:\\data\\emp1222.csv')
emp_122 =csv.reader(file)
a=[]
for emp_list in emp_122:
    a.append(int(emp_list[2]))
print(np.mean(a))
print(np.median(a))
print(stats.mode(a))