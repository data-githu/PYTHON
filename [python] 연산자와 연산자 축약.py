# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:42:06 2020

@author: Owner
"""

■ 19. 대입연산자 이해하기 (=)

변수에 값을 대입하는데 사용되는 기호는 = 입니다.
수학에서 = 은 외쪽과 오른쪽의 값이 같다는 의미를 가지지만 파이썬을 포함한 컴퓨터 프로그래밍 언어에서는 = 은 왼쪽변수에 오른쪽 값을 대입하겠다는 의미입니다.

예제 : a=7

*대입 연산자와 일반 연산자의 비교
	1. = : 대입연산자
	2. == : 같다
	3. in : 여러개의 값을 비교

문제52. 주사위 한개를 10번 던지시오
import random

dice = [1,2,3,4,5,6]

for i in range(1,11):
    result=random.choice(dice)
    print(result)

문제53. 주사위를 10번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오.
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,11):
        result = random.choice(dice)
        if result == 3:
            cnt = cnt + 1
print(cnt)


문제54. 주사위를 10번 던져서 주사위의 눈이 짝수가 나오는 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,11):
        result = random.choice(dice)
        if result in (2,4,6):
            cnt = cnt + 1
print(cnt)

문제56. 주사위를 2개를 동시에 던져서 두개의 눈의 합이 10이 되는 횟수를 출력하시오!
(주사위는 20번 던지시오)
import random
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
cnt = 0

for i in range(1,21):
    result1 = random.choice(dice1)
    result2= random.choice(dice2)
    if result1 + result2 == 10:
        cnt = cnt + 1
print(cnt)


문제57. 주사위 2개를 동시에 던져서 두 눈의 합이 10이 되는 확률을 출력하시오!
(주사위는 100번 던지시오)
import random
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
cnt = 0

for i in range(1,101):
    result1 = random.choice(dice1)
    result2= random.choice(dice2)
    if result1 + result2 == 10:
        cnt = cnt + 1
print(cnt/100)



■20.사칙연산자 이해하기
*사칙 연산자를 파이썬과 오라클과 비교

                     오라클             파이썬
                       +                      +
	                -                       -
	                *                       *
	                /                       /
	              mod                   %
	             power         power(2,3) or 2**3
	              sqrt                   sqrt
	              log2                  log2
	             log10                 log10
	
	
예제1. 밑수가 10이고 진수가 10인 log 값을 출력하시오.
(log 함수를 사용하려면 math 모듈을 import 해야합니다.)
import math #수학에 관련한 함수들이 다 코딩되어있는 모듈 math 를 쓰겠다.
print(math.log10(10))


문제58. 아래의 수학식을 파이썬으로 구현하시오!
import math
print(2*math.log2(10)+ (1/3)*math.log2(10))


■ 21. 연산자 축약 이해하기 ( =, -=, *=, /=)
변수에 값을 사칙 연산하여 그 결과를 동일한 변수에 대입할 때 연산자를 축약해서 대입할 수 있습니다.

예 : cnt = cnt + 1 를 다음과 같이 쓸 수 있습니다.
	cnt += 1


문제58. 주사위를 10번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오! (축약연산자 이용)
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,11):
        result = random.choice(dice)
        if result == 3:
            cnt += 1
print(cnt)


■ 22. TRUE 와 FALSE 이해하기

참을 나타내는 것이 TRUE 이고 거짓을 나타내는 것이 FALES 입니다.
조건을 판단해서 그 조건이 참이면 TRUE, 거짓이면 FALSE 를 리턴합니다.
TRUE 는 1, FALSE 는 0 값을 가집니다. 참과 거짓을 나타낼 때는 TRUE 와 FALSE 로 표현하면 더 직관적이고 프로그램 코드 가독성을 높일 수 있습니다.

예 : 
a=TRUE
b=FALSE

print(a)
print(1==1) #결과가 TRUE 로 출력됩니다.
print(1==2) #결과가 FALSE 로 출력됩니다.

■ 23. 관계연산자 이해하기

오라클             vs                파이썬
  >                                       >
  >=                                     >=
  <                                       <
  <=                                     <=
  =                                       ==
  !=                                      !=
  in                                       in

문제60. 주사위를 20번 던져서 주사위의 눈이 4이상 나오는 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,21):
        result = random.choice(dice)
        if result >= 4:
            cnt += 1
print(cnt)


문제61. (통계 정규분포 문제) 주사위 한개를 288회 던져서 주사위의 눈이 5이상 나오는 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,289):
        result = random.choice(dice)
        if result >= 5:
            cnt += 1
print(cnt)


문제62. (통계 정규분포 문제) 주사위 한개를 288회 던져서 주사위의 눈이 5이상 나오는 확률을 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,289):
        result = random.choice(dice)
        if result >= 5:
            cnt += 1
print(cnt/288)

문제63. (통계 정규분포 문제) 주사위 한개를 288회 던져서 주사위의 눈이 5이상 나올 횟수를 출력하는데 이 작업을 100번 해서 횟수가 100개 출력되게 하시오!
import random
dice = [1,2,3,4,5,6]
a=[]

for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    print(cnt)

문제64. (점심시간 문제) 위에서 출력된 횟수 100개를 비어있는 리스트 a 리스트에 담고 a 리스트의 갯수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
a=[]

for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
print(len(a))


설명 : 위의 코드는 주사위 288번을 던져서 주사위의 눈이 5이상이 나올 횟수 100개를 a 리스트에 입력하는 코드

문제65. 동전을 100번 던져서 앞면이 나오는 횟수를 출력하시오!
import random
coin = ['앞면','뒷면']
cnt = 0

for i in range(1,101):
    result = random.choice(coin)
    if result == '앞면':
        cnt += 1
print(cnt)


문제66. 동전 1개와 주사위 1개를 동시에 100번 던져서 동전이 앞면이 나오고 주사위의 눈이 5가 나오는 횟수를 출력하시오!
import random
coin =['앞면','뒷면']
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,101):
    result1 = random.choice(coin)
    result2 = random.choice(dice)
    if result1 == '앞면' and result2 == 5:
        cnt += 1
print(cnt)

문제67. 동전 1개와 주사위 1개를 동시에 100번 던져서 동전이 앞면이 나오고 주사위의 눈이 5가 나오는 횟수를 50번해서 횟수 50개가 출력되게 하시오!
import random
coin =['앞면','뒷면']
dice = [1,2,3,4,5,6]


for j in range(1,51):
    cnt = 0
    for i in range(1,101):
        result1 = random.choice(coin)
        result2 = random.choice(dice)
        if result1 == '앞면' and result2 == 5:
            cnt += 1
    print(cnt)

문제68. 위의 횟수 50개를 비어있는 리스트 a에 담으시오.
import random
coin =['앞면','뒷면']
dice = [1,2,3,4,5,6]
a = []

for j in range(1,51):
    cnt = 0
    for i in range(1,101):
        result1 = random.choice(coin)
        result2 = random.choice(dice)
        if result1 == '앞면' and result2 == 5:
            cnt += 1
    a.append(cnt)
print(a)

문제69. 담겨진 리스트 a의 요소의 갯수를 확인하시오!
import random
coin =['앞면','뒷면']
dice = [1,2,3,4,5,6]
a = []

for j in range(1,51):
    cnt = 0
    for i in range(1,101):
        result1 = random.choice(coin)
        result2 = random.choice(dice)
        if result1 == '앞면' and result2 == 5:
            cnt += 1
    a.append(cnt)
print(len(a))


문제70. a리스트들의 요소들의 평균값을 출력하시오! (numpy를 이용해서 구현하시오!)
import random
import numpy as np

coin =['앞면','뒷면']
dice = [1,2,3,4,5,6]
a = []

for j in range(1,51):
    cnt = 0
    for i in range(1,101):
        result1 = random.choice(coin)
        result2 = random.choice(dice)
        if result1 == '앞면' and result2 == 5:
            cnt += 1
    a.append(cnt)
print(np.mean(a))


예제1: 아래의 리스트의 요소들의 평균값을 구하시오!
import numpy as np
b=[7,4,5,3,2]

print(np.mean(b))

예제2: 아래의 리스트의 요소들의 평균값을 출력하시오!(numpy 사용하지않고 수행하시오)
b=[7,4,5,3,2]
cnt = 0

for i in b:
    cnt += i
print(cnt/5)



print(np.mean(a)) #평균
print(np.var(a)) #분산
print(np.std(a)) #표준편차

문제71. 문제 64번 코드를 활용하여 a리스트의 요소들의 평균과 분산과 표준편차를 구하시오!
import random
import numpy as np
dice = [1,2,3,4,5,6]
a=[]

for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
print(np.mean(a))
print(np.var(a))
print(np.std(a))


문제72. 위의 a 리스트에 담긴 요소 100개를 출력하시오!
import random
dice = [1,2,3,4,5,6]
a=[]

for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
print(a)

문제73. 위의 a리스트를 하나씩 출력해보시오!
import random
dice = [1,2,3,4,5,6]
a=[]

for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
for k in a:
    print(k)

문제74. a 리스트의 요소들의 숫자가 90이상이고 106이하인 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
cnt1 = 0
for k in a:
    if k >= 90 and k <= 106:
        cnt1 = cnt1 +1
print(cnt1)


문제 75. a 리스트의 요소들의 숫자가 90 이상이고 106 이하인 확률을 출력하시오!
import random
dice = [1,2,3,4,5,6]
a=[]
for j in range(1,101):
    cnt = 0
    for i in range(1,289):
            result = random.choice(dice)
            if result >= 5:
                cnt += 1
    a.append(cnt)
cnt1 = 0
for k in a:
    if k >= 90 and k <= 106:
        cnt1 = cnt1 +1
print(cnt1/100)


오늘의 마지막 문제 - 확률문제

6개의 제품이 들어있는 상자가 있는데 그 중에 2개가 불량품이라고 하자 제품검사를 위해서 3개를 추출했을 때 적어도 한개가 불량품일 확률은 어떻게 되는가?
import random
box = ['정상','정상','정상','정상','불량','불량']
cnt = 0

for i in range(1,10001):
    result1 = random.choice(box)
    result2 = random.choice(box)
    result3 = random.choice(box)
    if result1 == '정상' and result2 == '정상' and result3 =='정상':
        cnt = cnt + 1
print(1-(cnt/10000))