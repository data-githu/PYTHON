# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:05:38 2020

@author: Owner
"""

■ 111. 리스트에 있는 요소 개수 구하기 (len)
파이썬 내장함수인 len() 은 시퀀스 자료형의 크기를 구하는 함수입니다.
len()을 리스트에 적용하면 리스트의 모든 요소의 개수를 리턴합니다.

예 : 
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
print(len(a))

문제332. 초등학생 10만명의 체중 데이터를 모수로 보고 10만명의 체중 데이터에서 100명을 샘플링하여 평균을 구하시오!
import numpy as np
weight = np.random.randn(100000)*5+45
sample = np.random.choice(weight,100,replace=True).mean()
print(sample)

문제333. 위의 모집단에서 표본 100명을 추출하여 표본평균을 구하는 작업을 1000번 수행해서 1000개의 표본평균을 a라는 비어있는 리스트에 넣으시오!
import numpy as np
weight = np.random.randn(100000)*5+45
a=[]
for i in range(1,1001):
    sample = np.random.choice(weight,100,replace=True).mean()
    a.append(sample)
print(a)

문제334. 위의 a리스트의 요소의 갯수를 출력하시오!
import numpy as np
weight = np.random.randn(100000)*5+45
a=[]
for i in range(1,1001):
    sample = np.random.choice(weight,100,replace=True).mean()
    a.append(sample)
print(len(a))