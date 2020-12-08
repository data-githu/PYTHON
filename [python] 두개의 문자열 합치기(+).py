# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:47:09 2020

@author: Owner
"""

■ 79. 두 개의 문자열 합치기 (+)
두개의 문자열을 합치는 방법은 매우 간단합니다.
문자열1 + 문자열2 + 문자열3 으로 +연산자를 이용하면 됩니다.

예제 : 
a='scott'
b='king'
print(a+b) #scottking

문제262. 아래의 SQL을 파이썬으로 구현하시오!
SQL>
select ename || job
	from emp
python>
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1]+emp_list[2])
    

문제263. 아래와 같이 결과가 출력되게하시오!
SQL>
select ename || '의 직업은 '|| job|| '입니다.'
	from emp;
	
python>
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1]+'의 직업은 '+emp_list[2]+'입니다.')