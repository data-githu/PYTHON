# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:20:40 2020

@author: Owner
"""

■ 90. 문자열에서 특정 문자(열) 위치 찾기 (find)

문자열 객체의 find() 함수는 문자열에서 특정 문자나 문자열이 위치하는 인덱스를 리턴합니다. find() 에서 찾고자 하는 문자를 입력하면 해당 문자나 문자열이 최초로 나타나는 위치에 대한 인덱스를 리턴합니다.

예제 : 
txt = 'A lot of things occur each day'
word_count1 = txt.find('o')
print(word_count1) #3 : o라는 철자가 위치한 인덱스 번호를 리턴합니다.

문제284. 우리반 데이터 (emp122.csv) 를 파이썬으로 로드해서 이메일만 출력하시오!
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6])

문제285. 위에서 출력한 이메일에서 @의 위치 인덱스 번호를 출력하시오!
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6].find('@'))

문제286. 이번에는 이메일에서 .의 위치인덱스를 출력하시오!
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6].find('.'))

문제287. 이번에는 이메일을 출력하는데 이메일의 첫번째 철자부터 세번째 철자까지만 출력하시오!
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[6][0:3])

문제288. 우리반 데이터 이메일을 출력하는데 이메일에서 도메인만 출력하시오!
import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a= emp_list[6].find('@')
    b= emp_list[6].find('.')
    print(emp_list[6][a+1:b])

문제289. 이메일 abc.dfg@naver.com 도 같이 출력하려면 어떻게 해야할까요?
import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a= emp_list[6].find('@')
    b= emp_list[6].rfind('.')
    print(emp_list[6][a+1:b])

문제290. 위의 방법을 이용했을 때 co.kr 에 문제가 생길 수 있습니다. 다른 방법은 어떤 것이 있을까요?
import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    a = emp_list[6].find('@')
    result = emp_list[6][a:]
    b = result.find('.')
    print(result[1:b])
