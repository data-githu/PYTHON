# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:28:58 2020

@author: Owner
"""

■ 114. 리스트 요소 정렬하기 ① sort

list.sort() 는 리스트 객체 list의 모든 요소를 정렬합니다.

예 : 
a = [2,4,1,3,5]
a.sort()
print(a)

만약에 역순으로 정렬하고 싶다면?
a = [2,4,1,3,5]
a.sort(reverse = True)
print(a)

문제 338. emp2.csv에서 월급을 비어있는 리스트인 a에 담고 월급을 역순으로 정렬해서 리스트의 요소로 구성하시오!
import csv
file=open('c:\\data\\emp2.csv')
emp_csv =csv.reader(file)
a=[]
for emp_list in emp_csv:
    a.append(int(emp_list[5]))
a.sort(reverse=True)
print(a)