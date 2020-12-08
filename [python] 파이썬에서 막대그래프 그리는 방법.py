# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:42:02 2020

@author: Owner
"""

■ 파이썬에서 막대 그래프 그리는 방법
import matplotlib.pyplot as plt

y_value = [21.6, 23.6, 45.8, 77.0]
x_index = [0,1,2,3]

plt.bar ( x_index, y_value)
plt.show()

문제281. 아래의 리스트 값을 이용하여 막대그래프를 그리시오!
import matplotlib.pyplot as plt

y_value = [0.00191, 0.01, 0.07, 0.16]
x_index = [0,1,2,3]

plt.bar ( x_index, y_value)
plt.show()

문제282. 위의 그래프의 결과에 제목, x축 라벨과 y축 라벨을 같이 출력하시오!
import matplotlib.pyplot as plt

y_value = [0.00191, 0.01, 0.07, 0.16]
x_index = [0,1,2,3]

plt.bar ( x_index, y_value)
plt.title('Coin Probability') #그래프 제목
plt.xlabel('cnt') # 그래프 x축 라벨
plt.ylabel('probability') # 그래프 y축 라벨
plt.show()

문제283. 동전을 10번 던져서 앞면이 n번 나올 때의 확률 결과를 이용하여 막대 그래프로 시각화 하시오.
import random

def coin_prob(num):
    coin = ['앞면','뒷면']
    cnt = 0
    for k in range(1,10001):
        a = [ ]
        for i in range(1,11):
            result = random.choice(coin)
            a.append(result)
        if a.count('앞면') == num:
            cnt = cnt + 1
    return cnt/10000

b=[]
for i in range(0,11):
    result2 = coin_prob(i)
    b.append(result2)

import matplotlib.pyplot as plt

y_value = b
x_index = [0,1,2,3,4,5,6,7,8,9,10]

plt.bar ( x_index, y_value)
plt.title('Coin Probability')
plt.xlabel('cnt')
plt.ylabel('probability')
plt.show()

