# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:22:58 2020

@author: Owner
"""

■ 58. 예외처리 이해하기 ④ (try~except Exception as e)


http://docs.python.org/3/library/exception/html

설명 : 위의 사이트에 접속하면 여러가지 다양한 에러에 대해서 미리 에러 처리를 할 수 있도록 정의 해놓은 예외들을 확인할 수 있습니다.

예제1: 
try:
	x=int(input('분자의 숫자를 입력하시오.'))
	y=int(input('분모의 숫자를 입력하시오.'))
	print(x/y)
except:
	print('잘못된 값을 입력하셔서 나누기가 실행되지 않았습니다.')

설명 : 위의 경우에는 분모값을 입력할 때 숫자 0을 입력했을 때와 문자 a를 입력했을때 똑같이 '잘못된 값을 입력하셔서 나누기가 실행되지 않았습니다.'가 출력되게 했습니다. 좀 더 구체화 해서 분모값으로 0을 입력하면 '0으로 나눌수 없습니다' 가 나오고 분모값으로 a를 입력하면 '잘못된 값을 입력하셨습니다' 가 나오게 하고 싶다면 어떻게 해야할까요?

예제2: 
try:
	x=int(input('분자의 숫자를 입력하시오.'))
	y=int(input('분모의 숫자를 입력하시오.'))
	print(x/y)
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('잘못된 값을 입력하셨습니다.')


문제191. 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자만큼 1번부터 출력되게하는 코드를 작성하세요!
x=int(input('숫자를 입력하세요'))

for i in range(x):
    print(i+1)

문제192. 위의 코드를 예외처리 해서 숫자를 물어볼때 문자를 입력하면 잘못된 값을 입력하셨습니다. 라고 메시지가 출력되게 하시오.
try:
    x=int(input('숫자를 입력하세요'))
    for i in range(x):
        print(i+1)
except:
    print('잘못된 값을 입력하셨습니다.') 

try:
    x=int(input('숫자를 입력하세요'))
    for i in range(1, x+1):
        print(i)
except:
    print('잘못된 값을 입력하셨습니다.') 

설명 : 위의 코드의 경우에는 숫자를 입력할 때 알파벳 a 를 넣으면 예외처리가 되어서 잘못된 값을 입력하셨습니다. 라는 말만 나오고 에러에 대한 정확한 원인 파악이 어렵습니다.
try:
    x=int(input('숫자를 입력하세요'))
    for i in range(1, x+1):
        print(i)
except Exception as e:
    print('잘못된 값을 입력하셨습니다.') 
    print(e) # 에러가 난 이유를 출력해줍니다.

■ 59. 예외처리 이해하기 ⑤ (try~except 특정 예외)

파이썬 입장에서 봤을 때 오류가 아닌데 프로그래머가 오류라고 정의하고 프로그램이 실행되지 않고 오류메시지를 출력하는 경우에 사용합니다.

설명 : 금융권 프로그램에서는 금액이 안맞는 프로그램이 있다면 사고로 이어지게 되므로 금액이 안맞으면 프로그램을 종료하라는 예외처리를 할 수 있습니다.

문제193. 판다스를 이용해서 emp3.csv 의 데이터를 로드하는데 이름을 물어보게 하고 이름을 입력하면 해당 사원의 이름과 월급이 출력되게 하시오!
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
name = input('이름을 입력하세요~')

print(emp[['ename', 'sal']] [emp['ename']==name.upper()])


문제194. 위의 결과에서 월급만 출력하시오!
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
name = input('이름을 입력하세요~')

result = emp['sal'] [emp['ename']==name.upper()].values[0]
print(result)

문제195. 위의 코드에 사용자 정의 예외처리 해서 월급이 고소득자는 해당상원의 월급을 볼 수 없습니다. 라는 메시기자 출력되게 하세요.
(월급은 3000 이상이면 고소득자)
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
name = input('이름을 입력하세요~')

result = emp['sal'] [emp['ename']==name.upper()].values[0]
if result >= 3000:
    raise Exception('해당 사원의 월급은 볼 수 없습니다.')
print(emp[['ename','sal']] [emp['ename']==name.upper()])

문제196. 위의 코드를 수정해서 이름을 물어보게 하고 이름과 직업을 출력하는 코드를 작성하는데 직업이 SALESMAN이면 해당 사원의 정보는 볼 수 없습니다. 라는 메시지가 출력되면서 프로그램이 종료되게 하시오!
import pandas as pd

emp = pd.read_csv("c:\\data\\emp3.csv")
name = input('이름을 입력하세요~')

result = emp['job'] [emp['ename']==name.upper()].values[0]
if result == 'SALESMAN':
    raise Exception('해당 사원의 정보는 볼 수 없습니다.')
print(emp[['ename','job']] [emp['ename']==name.upper()])
