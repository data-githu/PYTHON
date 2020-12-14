# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:12:30 2020

@author: Owner
"""

■ 118. 리스트의 모든 요소의 합 구하기(sum)

파이썬 내장 함수 sum()을 이용해 list 의 모든 요소의 합을 출력합니다.

예제 :
listdata = [2,2,1,3,4,5,6,7,8]
result =sum(listdata)
print(result) #38

문제 351. 아래의 리스트의 짝수번재 요소의 합을 출력하시오!
listdata = [2,2,1,3,4,5,6,7,8]
print(sum(listdata[1::2]))

문제352. (알고리즘 문제) 아래의 리스트에 1-10까지의 숫자중에 없는 숫자가 하나있다 그 없는 숫자는 무엇인가?
a=[2,1,5,4,6,7,9,10,3]

result = sum(range(1,11))-sum(a)
print(result)