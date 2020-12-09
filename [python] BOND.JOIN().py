# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:24:53 2020

@author: Owner
"""

■ 92. 문자열을 특정 문자(열)로 결합하기(join)

문자열 객체의 join() 메소드는 split() 와는 반대로 문자열이 요소인 리스트를 인자로 받아 리스트 모든 요소를 특정 문자열로 연결하여 새로운 문자열로 만들어 리턴합니다.

예제 : 
a = ['http:', '', 'www.naver.com', 'news', 'today=20191204']
bond = '/'
url = bond.join(a)
print(url)

문제292. 우리반 데이터에서 이름만 출력하시오!
import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1])

문제293. 위에서 출력된 이름을 a라는 비어있는 리스트에 담고 a리스트를 출력하시오!
import csv
file = open("c:\\data\\emp123.csv",encoding='UTF8')
emp_csv=csv.reader(file)
a=[]
for emp_list in emp_csv:
    a.append(emp_list[1])
print(a)

문제294. a리스트에 담긴 이름을 ',' 로 연결하여 출력하시오.
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
a=[]
for emp_list in emp_csv:
    a.append(emp_list[1])
bond=','
result = bond.join(a)
print(result)

문제295. 위의 결과가 ㄱ,ㄴ,ㄷ,ㄹ 순서대로 출력되게 하시오!
import csv
file = open("c:\\data\\emp122.csv",encoding='UTF8')
emp_csv=csv.reader(file)
a=[]
for emp_list in emp_csv:
    a.append(emp_list[1])
a.sort()
bond=','
result = bond.join(a)
print(result)

