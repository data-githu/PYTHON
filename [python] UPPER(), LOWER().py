# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:52:27 2020

@author: Owner
"""
■ 87. 문자열에서 대소문자 변환하기 (upper, lower)
문자열 객체의 upper() 메소드는 문자열에 있는 모든 알파벳을 대문자로 변환한 결과를 리턴합니다. 문자열 객체의 lower() 메소드는 문자열에 있는 모든 알파벳을 소문자로 변환한 결과를 리턴합니다.

예제 : 
txt = 'A lot of things occur each day'
result1 = txt.upper()
result2 = txt.lower()
print(result1)
print(result2)

문제277. emp2.csv 에서 이름과 월급을 출력하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5])

문제278. 이름을 물어보게하고 이름을 입력하면 해당 사원의 이름과 월급이 출력되게 하는데 소문자로 입력하던 대문자로 입력하던 잘 출력되게 하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
name = input('이름을 입력하세요~')
for emp_list in emp_csv:
    if emp_list[1].lower() == name.lower():
        print(emp_list[1],emp_list[5])
