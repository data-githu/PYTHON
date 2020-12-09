# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:12:09 2020

@author: Owner
"""
■ 102. 리스트 요소 순서를 역순으로 만들기 ① reverse
리스트 객체의 reverse() 메소드는 리스트의 모든 요소 순서를 거꾸로 만듭니다.

예제 : 
list_a = ['a','b','c','d','e','f','g']
list_a.reverse()
print(list_a)

문제308. 우리반 테이블에서 이름을 출력하는데 ㅎ부터 ㄱ까지 출력될 수 있도록 하시오.
import csv
file=open('c:\\data\\emp122.csv',encoding='UTF8')
emp_122 =csv.reader(file)
a=[]
for emp_list in emp_122:
    result=(emp_list[1] + '('+ emp_list[2] +')' )
    a.append(result)
a.sort()
a.reverse()
result = ','.join(a)
print(result)

문제309. emp.csv 에서 이름과 월급을 출력하시오!
import csv
file=open('c:\\data\\emp3.csv',encoding='UTF8')
emp =csv.reader(file)
for emp_list in emp:
    print(emp_list[2],emp_list[6])

문제310. 위의 데이터 중 월급을 비어있는 리스트 a에 담으시오!
import csv
file=open('c:\\data\\emp3.csv',encoding='UTF8')
emp =csv.reader(file)
a=[]
for emp_list in emp:
    a.append(emp_list[6])
print(a)

문제311. 위의 a 리스트에 있는 월급을 월급이 높은 순서대로 정렬해서 a리스트에 담으시오!
import csv
file=open('c:\\data\\emp3.csv',encoding='UTF8')
emp =csv.reader(file)
a=[]
for emp_list in emp:
    a.append(emp_list[6])
a.sort()
a.reverse()
print(a)


■ 103. 리스트 요소 순서를 역순으로 만들기 ②reversed
리스트 요소 순서를 역순으로 만드는 또 다른 방법은 파이썬 내장 함수인 reversed() 를 이용하는 방법입니다.
reverse() 는 인자로 입력된 시퀀스 자료형의 요소 순서를 역순으로 새로운 시퀀스 자료형을 만들어 리턴합니다.
reverse : 원본 데이터를 역순으로 만듭니다.
resversed : 역순으로 만들지만 원본 데이터를 역순으로 만들지 않습니다.

예제 : 
list_a = ['a','b','c','d','e']
list_a.reverse()
print(list_a)#['e', 'd', 'c', 'b', 'a']

list_b =  ['a','b','c','d','e']
result = reversed(list_b)
print(list(result)) #['e', 'd', 'c', 'b', 'a']
print(list_b) #['a', 'b', 'c', 'd', 'e']
