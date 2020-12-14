# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:11:34 2020

@author: Owner
"""

■ 130. 문자열로 된 식을 실행하기 (eval)
코드를 작성하다 보면 파일에서 읽은 수식이나 문자열을 그대로 실행해야하는 경우가 있습니다. 예를 들어 '2+3' 과 같이 두개의 숫자를 더하는 문자열을 텍스트 파일에서 읽어 이를 실행하여 이수식의 결과인 5를 구하는 경우입니다.

예제 : 
a = '2+3'
print(a) #2+3
print(eval(a)) #5


문제378. eval을 이용하여 아래의 결과를 출력하시오!
34+256-71*34 = -2,124 

a= '34 + 256 - 71 * 34'
print(a,'=',eval(a))


문제379. 아래의 리스트의 숫자를 뽑아내서 아래의 문자열을 생성하시오!
a = [34,22,45,27,31,33,55]
결과 : 34+22+45+27+31+33+55

a = [34,22,45,27,31,33,55]
b=[]
bond='+'
for i in a:
    b.append(str(i))
result = bond.join(b)
print(result)

문제380. eval 을 이용하여 아래의 리스트를 가지고 아래의 결과를 출력하시오!
a = [34,22,45,27,31,33,55]
결과 : 34+22+45+27+31+33+55 =?

a = [34,22,45,27,31,33,55]
b=[]
bond='+'
for i in a:
    b.append(str(i))
result = bond.join(b)
print(result,'=',eval(result))

문제381. 우리반 데이터 (emp1222.csv) 에서 나이를 읽어들여 아래와 같이 결과가 출력되게하시오!
결과 : 29+31+35+29+28+28+25+28+27+27+27+26+33+30+27+27+25+28+29+24+24+29+36+26+26+26+44+28+29+28 = 859

import csv
file = open("c:\\data\\emp1222.csv",encoding = 'CP949')
emp_csv = csv.reader(file)
age = []
bond='+'
for emp_list in emp_csv:
    age.append(str(emp_list[2]))
result = bond.join(age)
print(result,'=',eval(result))
