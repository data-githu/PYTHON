# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:44:24 2020

@author: Owner
"""

■ 76. 문자열에서 지정한 구간의 문자열 얻기 (슬라이싱)
문자열에서 특정 구간에 있는 문자열을 얻으려면 슬라이싱을 이용하면 됩니다.

예제 : 
print('scott'[0:2]) #sc

a='scott'
print(a[0:2]) #sc
print(a[3:]) #tt

문제259. 아래의 SQL을 파이썬으로 구현하시오!
SQL>
select ename, substr(ename,1,3)
	from emp;

PYTHON>
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[1][0:3])