# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:49:00 2020

@author: Owner
"""
■ 127. 사전 정렬하기 (sorted)
파이썬 내장함수 sorted()는 사전 자료를 인자로 입력받아 정렬할 수 있습니다.
사전의 각 요소는 키:값 으로 되어져 있습니다.
sorted()함수에 사전을 인자로 입력하면 기본적으로 사전의 키를 오름차순으로 정렬한 결과를 리스트로 반환합니다.

예제 : 
dict2 = {'소녀시대' : '소원을 말해봐', '방탄소년단':'DNA', '오마이걸':'살짝 설랬어'}
	1. 위의 dict2에서 key만 추출
	dict2 = {'소녀시대' : '소원을 말해봐', '방탄소년단':'DNA', '오마이걸':'살짝 설랬어'}
	print(dict2.keys())
	
	2. 위의 dict2 의 키값을 아래와 같이 정렬해서 출력하시오!
	dict2 = {'소녀시대' : '소원을 말해봐', '방탄소년단':'DNA', '오마이걸':'살짝 설랬어'}
	result = dict2.keys()
	print(sorted(result))
	
문제371. 위의 결과를 reverse 되게 해서 출력하시오!
dict2 = {'소녀시대' : '소원을 말해봐', '방탄소년단':'DNA', '오마이걸':'살짝 설랬어'}
result = dict2.keys()
print(sorted(result, reverse = True))

문제372. 우리반 데이터(emp1222.csv)에서 이름과 통신사를 출력하시오!
import csv
file = open("c:\\data\\emp1222.csv",encoding = 'CP949')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5])

* defaultdictionary 를 이용해서 딕셔너리의 값을 리스트로 구성하는 코드

from  collections  import  defaultdict 
gini = defaultdict(list)
gini['kt'].append('허혁')
gini['kt'].append('정다희')
gini['sk'].append('박혜진')
gini['sk'].append('김승순')
print( gini ) # defaultdict(<class 'list'>, {'kt': ['허혁', '정다희'], 'sk': ['박혜진', '김승순']})

문제373. 우리반 데이터에서 통신사를 key 로 하고 학생이름을 값으로 해서 defaultdict를 생성하시오!
from  collections  import  defaultdict 
telecom = defaultdict(list)

import csv
file = open("c:\\data\\emp1222.csv",encoding = 'CP949')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    telecom[emp_list[5]].append(emp_list[1])
print(telecom)

문제374. 위에서 구성한 telecom 딕셔너리에서 통신사가 kt 인 학생들을 출력하는데 이름을  ㄱㄴㄷㄹ 순으로 정렬해서 출력하시오!
from  collections  import  defaultdict 
telecom = defaultdict(list)

import csv
file = open("c:\\data\\emp1222.csv",encoding = 'CP949')
emp_csv = csv.reader(file)

for emp_list in emp_csv:
    telecom[emp_list[5]].append(emp_list[1])

result = telecom['kt']
print(sorted(result))

