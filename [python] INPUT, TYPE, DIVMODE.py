# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:23:34 2020

@author: Owner
"""


■ 60. 값 입력받기(input)

파이썬 내장 함수 input 은 사용자가 키보드로 입력한 값을 문자열로 리턴합니다.
input() 의 인자는 사용자 입력을 돕기위한 안내 문구나 힌트 등을 표시하는 문자열이 됩니다.

예 : 
name = input('사원의 이름을 입력하세요~')
num = int(input('숫자값을 입력하세요~'))

문제198. 없는 사원 이름을 입력하면 해당 사원은 없습니다. 라는 메시지가 출력되게 하시오!
import pandas as pd


try:
    emp = pd.read_csv("c:\\data\\emp3.csv")
    name = input('이름을 입력하세요~')
    result = emp[['ename','sal']] [emp['ename']==name.upper()].values[0]
    print(emp[['ename','sal']] [emp['ename']==name.upper()])
except LookupError:
    print('해당 사원은 없습니다.')

설명 :  emp[['ename','sal']] [emp['ename']==name.upper()].values[0] 이 코드에서 values[0] 을 사용하면 series(컬럼)가 아니라 값으로 출력이 되어서 result에 담기게 됩니다. 없는 사원이름을 입력하면 result 에 값이 입력되지 않게 되므로 LookupError 예외처리가 되어서 해당사원은 없습니다. 라는 메시지가 출력되는 겁니다.

문제199. 직업을 물어보게 하고 직업을 입력하면 해당 사원의 이름과 직업과 월급이 출력되게 하는 코드를 작성하는데 없는 직업을 입하면 해당 직원은 사원 테이블에 없습니다. 라는 메시지가 출력되게 하세요!
import pandas as pd

try:
    emp = pd.read_csv("c:\\data\\emp3.csv")
    name = input('직업을 입력하세요~')
    result = emp[['ename','job','sal']] [emp['job']==name.upper()].values[0]
    print(emp[['ename','job','sal']] [emp['job']==name.upper()])
except:
    print('해당 직원은 사원 테이블에 없습니다.')


■ 61. 자료형 확인하기(type)
파이썬의 자료형은 하나의 클래스입니다.
파이썬은 숫자나 문자, 문자열, 리스트, 튜플, 사전, 함수 등을 각각의 하나의 클래스로 취급합니다. 코드를 작성하다가 변수 이름만 보고 이자료가 어떤 자료형인지 확인해야하는 경우가 있습니다. 이때 파이썬의 내장함수인 type()을 활용하면 자료형을 쉽게 확인할 수 있습니다.
예 : 
numdata = 57
print(type(numdata)) #<class 'int'>

numdata2 = 57.2
print(type(numdata2)) #<class 'float'>

문제200. 딕셔너리 자료형을 만들고 타입을 확인하시오!
a={'사과':'apple', '배':'pear'}
print(type(a)) #<class 'dict'>

■ 62. 나눗셈에서 나머지만 구하기(%)

"나누기 연산에서 나머지만 구하는 연산을 % 로 구합니다."
예 :
print(12%3) #0
print(11%5) #1

문제201. 아래와 같이 두개의 숫자를 각각 물어보게 하고 아래의 메시지가 출력되게하세요.
x=int(input('첫번째 숫자를 입력하세요'))
y=int(input('두번째 숫자를 입력하세요'))

print( x,'를 ', y, '로 나누면 ', x%y, '가 남습니다.')


■ 63. 몫과 나머지 구하기(divmod)

예제 : 
result1, result2 = divmod(1113,23)
print(result1, result2)

result = divmod(1113,23)
print(result)

문제202. 아래와 같이 실행되게 코드를 수행하시오!
첫번째 숫자를 입력하시오~ 1113
두번째 숫자를 입력하시오~ 23

1113을 23으로 나눈 몫은 48 이고 나머지는 9 입니다.

try:
    x=int(input('첫번째 숫자를 입력하세요~'))
    y=int(input('두번째 숫자를 입력하세요~'))
    result1, result2 = divmod(x,y)
    print( '%d를 %d로 나눈 몫은 %d 이고 나머지는 %d 입니다.' %(x,y,result1,result2))
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다.')

