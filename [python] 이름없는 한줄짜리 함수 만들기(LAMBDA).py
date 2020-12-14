# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:12:09 2020

@author: Owner
"""

■ 131. 이름없는 한줄짜리 함수 만들기(lambda)
파이썬에서 함수를 정의하는 방법은 일반적으로 다음과 같습니다.

def 함수이름(입력매개변수):
	실행코드
a = [1,2,3,4,5]

def odd_func(a,b):
	return a+b
print(odd_func(2,3)) #5

설명 : 함수를 만들때 위와 같이 함수 이름을 주고 생성했습니다.
함수를 생성하는 이유는 함수를 한번 만들면 다음부터는 함수이름을 가지고 함수만 호출하면 되기 때문에 함수를 생성해서 코드를 작성했습니다.

지금부터 만들 함수는 이름없이 함수를 생성하는 코드입니다. 함수 이름을 주지않고 함수를 생성한다는 것은 이 함수는 지금 이 코드에서 한번만 실행하고 앞으로 쓸 일이 없는 경우 함수 이름없이 함수를 생성합니다. 아래와 같이 한 줄 짜리 함수를 생성합니다.
k = lambda a,b:a+b

문법 : 변수이름 = lambda 입력매개변수 : 실행문
k = lambda a,b : a+b
print(k(2,3)) #5

문제382. 아래의 함수를 그냥 이름없는 한줄짜리 함수로 만들어보세요!
def gob_func(a,b):
	return a*b
	
k = lambda a,b : a*b
print(k(2,3))

문제383. 아래의 함수를 그냥 이름없는 한줄짜리 함수로 생성하시오!
def odd_func(a):
	if a%2 ==0:
		return '짝수입니다.'
	else:
		retrun '홀수입니다.'

print(odd_func(2))
print(odd_func(3))

k = lambda a: '짝수입니다.' if a%2 == 0 else '홀수입니다.'
print(k(2))
print(k(3))


문제384. 아래의 함수를 lambda 로 구현하시오!
def high_income(a):
	if a>=3000:
		return '고소득자 입니다.'
	else:
		return '일반 소득자 입니다.'
		
k = lambda a: 고소득자 입니다.' if a>=3000 else '저소득자입니다.'
print(k(4000))

문제385. 아래의 함수를 lambda로 구현하시오!
def child_tall(num):
	if 140 -1.96*5 <= num <= 140 + 1.96*5:
		return '신뢰구간 95% 안에 있습니다.'
	else:
		return '신뢰구간 95% 안에 없습니다.'

k = lambda num: '신뢰구간 95% 안에 있습니다.' if 140 -1.96*5 <= num <= 140 + 1.96*5 else '신뢰구간 95% 안에 없습니다.'
