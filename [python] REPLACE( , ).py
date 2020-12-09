# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:58:17 2020

@author: Owner
"""

■ 93. 문자열에서 특정 문자(열)를 다른 문자(열)로 바꾸기(replace)

문자열 객체의 replace() 메소드는 문자열에서 특정문자나 문자열을 다른 문자나 문자열로 변경합니다.

예제 : 
txt = 'My password is 1234'
result = txt.replace('1','0')
print(result)

문제296. emp2.csv 에서 이름과 월급을 출력하는데 월급을 출력할 대 0 대신에 *로 출력하시오!
import csv
file = open("c:\\data\\emp3.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[2],emp_list[6].replace('0','*'))

문제297. 아래의 리스트를 가지고 아래와 같이 출력하시오!
a = ['name:홍길동', 'age:17', 'magor:경영학', 'nation : 한국']
name ----> 홍길동
age ----> 17
magor ----> 경영학
nation  ---->  한국

a = ['name:홍길동', 'age:17', 'magor:경영학', 'nation : 한국']
for i in a:
    print(i.replace(':',' ----> '))


