# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:04:50 2020

@author: Owner
"""


오라클 배울때는 오라클 개발자가 만들어준 함수를 사용했지만 파이썬을 배울때는 우리가 직접 함수를 생성합니다.
파이썬에서도 파이썬 개발자가 미리 만들어 놓은 함수들이 있습니다. 파이썬도 무료이고 전세계인이 사용하는 프로그램이다 보니 각국의 뛰어난 개발자들이 파이썬 함수를 직접 만들어서 공유를 해줍니다.
우리는 import 명령어로 불러와서 사용할 수 있습니다.


오라클 함수            vs                        파이썬 함수
upper                                                 upper()
lower                                                lower()
initcap                                              만들어서 써야함
substr                                                만들어서 써야함
replace                                            replace()
length                                                   len()
rtrim                                                    rstrip()
ltrim                                                    lstrip()
rpad                                              만들어서 써야함                                lpad                                              만들어서 써야함
instr                                              만들어서 써야함
round                                                 round()
trunc                                                   trunc()    
mod                                                       %
power                                                  pow
to_char                                                   str
to_number                                             int, float
to_date                                           datatime.strptime()
nvl                                              만들어서 써야함
decode/case                                            if문


예제 : 아래의 SQL을 파이썬으로 구현하시오!
SQL > 
select lower(ename)
	from emp

PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    print(i.lower())

문제131. (점심시간 문제) 아래의 SQL을 파이썬으로 구현하시오!

SQL > 
select lower(ename), lower(job)
	from emp

PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i, k in zip(emp['ename'],emp['job']):
    print(i.lower(), k.lower())


*함수를 생성하는 방법

def add_number(n1,n2):
    result = n1 + n2
    return result

*위의 함수 실행하는 방법
print(add_number(1,2))

*콜론을 끝을 맺는 경우 4가지

	1. if 문 종료시
	예 : if 조건:
	2. for문 종료시
	예 : for i in range(1,11):
	3. 함수 생성시
	예 : def 함수이름 ( 입력매개변수):
	4. 클래스 생성시
	예 : class  클래스 이름 : 

문제132. 1-10까지 출력하시오!
for i in range(1,11):
    print(i)

문제133. 1-10까지 더한 값을 출력하시오!
sum = 0
for i in range(1,11):
    result = i
    sum = sum + i
print(sum)

문제134. 위의 코드를 이용해서 함수를 생성하는데 아래와 같이 숫자를 입력하고 함수를 실행하면 해당 숫자까지 1부터 다 더한 값이 출력되게하시오!
def all_add(n1):
    sum = 0
    for i in range(1, n1+1):
        sum = sum + i
    return sum
print(all_add(10))

문자135. 다음의 문자열 변수를 생성하고 문자열 변수의 문자를 소문자로 출력하시오!
a='SCOTT'
print(a.lower())
print('SCOTT'.lower())

문자136. 아래의 문자열을 대문자로 출력하시오!
a='scott'
print(a.upper())
print('scott'.upper())

문제137. 아래의 문자열에서 첫번째 철자만 출력하시오!
a='scott'
print(a[0])

문제138. 위에 출력한 첫번째 철자를 대문자로 출력하시오!
a='scott'
print(a[0].upper())

문제139. 아래의 문자열 변수에서 cott 만 출력하시오!
a='scott'
print(a[1:])

문제140. 아래의 함수를 생성하시오!
def initcap(char1):
    return(char1[0].upper()+char1[1:].lower())
print(initcap('scott'))


■ 40. 함수 인자 이해하기
인자란 위에서 사용한 입력 매개변수를 말합니다.

예:
def add_text(t1,t2):
    return t1 + ' ' + t2
print(add_text('파이썬','자바'))

*매개변수에 아무것도 입력하지 않고 실행하면 기본값이 출력되게 함수를 생성하는 방법
def add_text(t1, t2='최고'):
	return t1+' '+t2
print(add_text('파이썬','자바')) #파이썬 자바
print(add_text('파이썬')) #파이썬 최고

설명 : t2에 값을 아무것도 안넣었더니 기본값으로 지정한 '최고'가 출력되었습니다.

■ 41. 지역변수와 전역변수 이해하기(global)
변수는 자신이 생성된 범위 안에서만 유효합니다.
함수 안에서 만든 변수는 함수 안에서 살아있다가 함수 코드의 실행이 종료되면 그 생명을 다합니다.
이것을 '지역변수'라고 합니다.

예 : 스타벅스 내에서의 머그컵

이와 반대로 함수 외부에서 만든 변수는 프로그램이 살아있는 동안에 함께 살아있다가 프로그램이 종료되면 같이 소멸됩니다.
이렇게 프로그램 전체를 유효범위로 가지는 변수를 '전역변수' 라고 합니다.

예 : 개인용 텀블러

예제1:
strdata = '전역변수'

def func1():
	strdata2 = '지역변수'
	return strdata2
print(func1()) # 지역변수
	
설명 :  대부분 많은 코드들이 지역변수를 사용합니다.
그러면 전역변수를 사용하는 경우는 언제 일까요?

프로그램 전체에서 공통적으로 사용되고 잘 변하지 않는 데이터는 전역변수로 사용합니다.

예제:
pi =3.141592653

def cycle_func1(num1):
	global pi # 전역변수 pi를 함수내부로 가져올 수 있습니다. 
	return pi * num1 * num1

def cycle_func2(num1):
	global pi
	return 1/4 * pi * num1 * num1

print(cycle_func1(5))
print(cycle_func2(5))
	
	
■ 42. 함수 리턴값 이해하기(return)
모든 함수는 이름을 갖고 있습니다. 이 이름을 불러주면 파이썬은 그 이름 아래에 정의되어있는 코드를 실행합니다.
이때 함수를 부르는 코드를 호출자라고 합니다.
함수가 호출자에게 결과를 돌려주는 것을 반환(return) 이라고 합니다.

pi =3.141592653

def cycle_func1(num1):
	global pi 
	return pi * num1 * num1

print(cycle_func1(5)) #함수를 호출하는 호출자 코드입니다.

*절대값을 출력하는 함수(무조건 양수로 출력하는 함수)
print(abs(-9))
print(abs(9))

문제141. abs 함수를 사용하지말 if 문을 이용해서 절대값을 출력하는 my_abs 라는 함수를 생성하시오!
def my_abs(num1):
    if num1 >= 0 :
        return num1
    else:
        return -num1
    
print(my_abs(-9))
print(my_abs(9))
