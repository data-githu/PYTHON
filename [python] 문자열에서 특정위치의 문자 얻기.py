# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:43:01 2020

@author: Owner
"""
■ 75. 문자열에서 특정 위치의 문자 얻기

문자열에서 특정위치의 문자를 얻는 방법은 인덱싱을 이용하는 것입니다.
인덱스는 0부터 시작합니다. 파이썬 인덱스는 음수도 가능합니다.

예제 :
print(scott[0]) #s

a='scott' #a 라는 문자형 변수를 생성하면서 scott을 a를 빈칸에 담았다.
print(a[0]) #s


문제253. 아래의 txt 변수에서 w를 출력하시오!
txt = 'A tale that was not right'
print(txt[12])

문제254. 위의 txt 변수에서 맨끝의 철자인 t를 출력하시오!
txt = 'A tale that was not right'
print(txt[-1])


문제255. emp3.csv에서 이름만 출력하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1])

문제256. 위의 출력된 이름의 데이터 유형이 무엇인지 확인하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(type(emp_list[1]))

문제257. 문제255번을 다시 수행해서 emp2.csv에서 이름을 다시 출력하는데 이름의 첫번째 철자만 출력하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0])

문제258. 첫번째 철자가 소문자로 나오게 하시오.
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower())
