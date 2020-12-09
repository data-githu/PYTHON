# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:10:29 2020

@author: Owner
"""

■ 96. 순차적인 정수 리스트 만들기(range)

[0,1,2,3] 이나 [100,101,102,103] 과 같이 순차적인 정수 리스트를 만드는 가장 간단한 방법은 파이썬 내장함수인 range() 입니다.

예제 : 
print(range(1,11)) # range(1,11)
print(list(range(1,11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

문제299. 아래와 같이 주사위의 눈을 담은 리스트를 만드시오!
dice = list(range(1,7))
print(dice)


문제300. 주사위 2개를 만들고 주사위 2개를 동시에 던져서 두 주사위의 눈의 합이 10이 나오는 확률을 구하시오!
import random

dice1 = list(range(1,7))
dice2 = list(range(1,7))
cnt = 0
for i in range(1,10001):
    result1 = random.choice(dice1)
    result2 = random.choice(dice2)
    if result1 + result2 == 10:
        cnt = cnt + 1
print(cnt/10000)

문제301. 아래의 결과를 출력하시오!
[2,3,4,6,8,10,12,14,16,18]

a = list(range(2,20,2)) 
print(a)
