# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:11:48 2020

@author: Owner
"""

■ 132. 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)
파이썬 내장함수 map()은 리스트 A 와 함수 f 가 주어지면 리스트 A의 요소를 함수 f 에 입력해서 출력하는 결과를 간단하게 출력해줍니다.

문법 : map(함수명, 함수에 제공할 매개변수 값들)

매개변수의 값들을 바꿔가면서 함수를 반복 실행할 때 유용하게 사용할 수 있습니다.

예제 : 
def gob(x):
	return x*x
	
a=[1,2,3,4,5]
result = map(gob, a)
print(list(result))

설명 : map 함수가 리턴해주는 결과를 보려면 반드시 list 함수로 리턴된 값을 변환해서 리스트 형태로 봐야합니다.

설명 : 리스트의 요소 하나하나를 함수에 입력값으로 입력한다.(mapping)

문제391. 숫자를 입력해서 해당 숫자가 3000보다 크면 숫자 1을 리턴하게 하고 입력한 숫자가 3000보다 작다면 0을 리턴하는 함수를 구현하시오!
def high_income(sal):
    if sal > 3000:
        return 1
    else:
        return 0

print(high_income(3500)) #1
print(high_income(2000)) #0

문제392. 위에서 만든 함수를 map 함수에 적용해서 아래의 리스트의 요소가 high_income 함수의 입력 매개변수로 입력해서 아래의 결과가 출력되게 하시오!
def high_income(sal):
    if sal > 3000:
        return 1
    else:
        return 0
a = [4000,5000,2000,3500,1000]
result = map(high_income, a)
print(list(result))


문제393. 동전을 던져서 앞면이 나오는지 뒷면이 나오는지 출력하는 함수를 생성하시오!
import random

coin = ['앞면','뒷면']
cnt = 0
def coin_cnt(num):
    for i in range(1,num+1):
        result = random.choice(coin)
        print(result)

coin_cnt(5)


문제394. 위의 함수를 수정해서 숫자를 입력하면 해당 숫자만큼 동전을 던져서 동전이 앞면이 나오는 확률을 출력하시오!
import random

def coin_cnt(num):
    coin = ['앞면','뒷면']
    cnt = 0
    for i in range(1,num+1):
        result = random.choice(coin)
        if result == '앞면':
            cnt = cnt + 1
    return cnt/num

print(coin_cnt(100))

문제395. 위에서 만든 coin_cnt 함수에 아래의 a 리스트의 요소들을 적용해서 결과 확률이 출력되게 하시오!
a = [10,100,1000,10000,10000]

import random

def coin_cnt(num):
    coin = ['앞면','뒷면']
    cnt = 0
    for i in range(1,num+1):
        result = random.choice(coin)
        if result == '앞면':
            cnt = cnt + 1
    return cnt/num
a = [10,100,1000,10000,10000]
values = map(coin_cnt,a)
print(list(values)) #[0.4, 0.49, 0.507, 0.5031, 0.5034]

문제396. 주사위를 던져서 주사위의 눈이 5가 나올 확률을 출력하는 함수를 만들고 아래의 a 리스트의 주사위를 던지는 횟수를 map 함수로 적용해서 확이 점점 1/6 으로 근사해지는지 실험하시오!
import random
def dice_cnt(num):
    dice = [1,2,3,4,5,6]
    cnt = 0 
    for i in range(1,num+1):
        result = random.choice(dice)
        if result == 5:
            cnt = cnt +1
    return cnt/num
a = [10,100,1000,10000,10000]
values = map(dice_cnt,a)
print(list(values)) # [0.3, 0.18, 0.169, 0.1649, 0.1646]

문제397. 아래의 불량품이 들어있는 박스에서 제품을 3개 뽑았을 때 3개 중에 2개가 불량품일 확률을 출력하는 함수를 구하시오!
box = ['정상','정상','불량품','정상','불량품','정상','정상','불량품']

import numpy as np
def bad_cnt(num):
    box = ['정상','정상','불량품','정상','불량품','정상','정상','불량품']
    cnt = 0
    for i in range(1,num+1):
        result = list(np.random.choice(box,3,replace = True))
        if result.count('불량품') == 2:
            cnt = cnt + 1
    return cnt/num
    
print(bad_cnt(100))

문제398. 위에서 만든 box_cnt 함수에 아래의 a리스트의 횟수를 map 함수로 적용해서 확률이 출력되게하시오!
import numpy as np
def bad_cnt(num):
    box = ['정상','정상','불량품','정상','불량품','정상','정상','불량품']
    cnt = 0
    for i in range(1,num+1):
        result = list(np.random.choice(box,3,replace = True))
        if result.count('불량품') == 2:
            cnt = cnt + 1
    return cnt/num
    
a = [10,100,1000,10000,10000]
values = map(bad_cnt,a)
print(list(values)) #[0.2, 0.27, 0.25, 0.2609, 0.2651]

