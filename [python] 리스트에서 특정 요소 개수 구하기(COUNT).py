# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:12:27 2020

@author: Owner
"""

■ 112. 리스트에서 특정 요소 개수 구하기(count)

리스트.count('요소') 은 객체 리스트에서 '요소'의 갯수를 구하는 메소드 입니다.

box = ['yellow','red','red','red','yellow']
print(box.count('red')) #3

문제336. 우리반 데이터의 나이를 비어있는 리스트 a 에 이렵락하고 나서 우리반 나이터 중에서 27살이 몇명있는지 출력하시오!
import csv
file=open('c:\\data\\emp1222.csv')
emp_122 =csv.reader(file)
age=[]
for emp_list in emp_122:
    age.append(int(emp_list[2]))
print(age.count(27)) #5