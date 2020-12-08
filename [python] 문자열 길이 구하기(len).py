# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:50:03 2020

@author: Owner
"""

■ 83. 문자열 길이 구하기 (len)
예제 : 
a='scott'
print(len(a)) #5

문제271. 파이썬으로 emp2.csv 를 읽어 이름, 이름의 길이를 출력하시오!
SQL>
select ename, length(ename)
	from emp;

python>
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
cnt = 0
for emp_list in emp_csv:
    print(emp_list[1],len(emp_list[1]))