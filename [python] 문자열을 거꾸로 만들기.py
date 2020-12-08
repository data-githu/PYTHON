# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:45:31 2020

@author: Owner
"""

■ 78. 문자열을 거꾸로 만들기
슬라이싱을 이용하면 매우 간단하게 거꾸로 된 문자열을 얻을 수 있습니다.
문자열 txt를 처음부터 끝까지 스텝 -1 로 슬라이싱 하면 됩니다.
예제 :
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
print(txt[ : ]) #문자열 전체 다 출력
print(txt[ : : ] #문자열 전체 다 출력
print(txt[ : : : ] #문자열 전체 다 출력
result = txt[::-1]
print(result)

문제261. 이름을 출력하는데 이름의 철자를 거꾸로 출력하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[1][ : :-1])