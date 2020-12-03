# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:19:35 2020

@author: Owner
"""	

■ 55. 예외처리 이해하기 (① try~except)
프로그램을 작성하다 보면 뜻하지 않은 오류가 발생하는 코드가 있을 수 있습니다. 프로그램이 실행되는 동안 오류가 발생하면 프로그램이 더 이상 진행될 ㅜ 없는 상태가 되는데 이를 예외상황이라고 합니다. 프로그램에 예외가 발생하더라도 프로그램을 중단시키지 않도록 예외에 대한 적절한 처리를 하여 프로그램을 계속 진행 할 수 있도록 하는 구문이 try ~except 입니다.

예제 : 
try:
	문제가 없을 경우 실행할 코드
except:
	문제가 생겼을 때 실행할 코드
	
예제1 : try~except 를 사용해서 예외처리를 하지 않았을 때의 코드
def my_divide():
    x = input('분자의 숫자를 입력하세요~')
    y = input('분모의 숫자를 입력하세요~')
    return int(x)/int(y)

print( my_divide())

예제2 : try~except 를 사용했을 때의 예제
def my_divide():
    try :
        x = input('분자의 숫자를 입력하세요~')
        y = input('분모의 숫자를 입력하세요~')
        return int(x)/int(y)
    except:
        return '당황하셨겠지만 잘못된 값을 입력하셔서 나누기 할 수 없습니다.'
print( my_divide())

설명 : try 와 except 사이의 코드가 잘 실행이 된다면 except 이후의 문장을 실행하지 않고 try 와 except 사이에 코드가 실행이 안된다면 except 이후의 문장을 실행합니다.

문제179. 판다스를 이용해서 emp3.csv 에서 이름과 월급을 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']])

문제180. 이름이 SCOTT 인 사원의 이름과 월급을 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']=='SCOTT'])

문제181. input 함수를 이용해서 이름을 물어보게 하고 이름을 입력하면 해당 사원의 이름과 월급이 출력되게 하시오!
import pandas as pd
x = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']==x])

문제182. 이번에는 소문자로 이름을 입력해도 출력되게 하시오!
import pandas as pd
x = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']==x.upper()])

문제183. 그런데 이번에는 위의 코드를 실행하는데 없는 사원이름을 출력하시오!
import pandas as pd
x = input('이름을 입력하세요~')
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['ename']==x.upper()])

# 이름을 입력하세요~jack
# Empty DataFrame
# Columns: [ename, sal]
# Index: []

문제184. 위의 코드에 예외처리를 해서없는 사원이름을 입력하면 입력하신 이름의 사원 존재하지않습니다. 라는 메시지가 출력되게하시오!

-> 이것은 에러가 아니라서 예외처리가 되지 않습니다.

문자185. 숫자를 입력하면 해당 숫자의 제곱값이 출력되는 코드를 구현하시오!
num = int(input('숫자를 입력하세요'))
print(num**2)

문제186. 위의 코드에서 잘못된 값을 넣으면 '잘못된 값 입력하셨습니다.' 가 출력되게 구현하시오!

def power():
    try:
        num = int(input('숫자를 입력하세요'))
        return num**2
    except:
        return '잘못된 값을 입력하셨습니다.'
print(power())


■ 56. 예외처리 이해하기 (② try~except~else)

어떤 로직을 수행할 때 오류 상황이 아닐 경우에만 어떤 작업을행하는 코드를 작성해야할 때가 있습니다. 이러한 경우에 try~except~else 구문을 활용합니다.

예제:
try:
	실행할 코드 블록	
except:
	예외처리할 코드 블록
else:
	except 절을 만나지 않았을 경우 실행하는 코드 블록


try:
    num = int(input('숫자를 입력하세요'))
    print(num**2)
except:
    print('잘못된 값을 입력하셨습니다.')
else:
    print('결과 출력에 성공했습니다.')


설명 : try ~ except 사이의 코드에 에러가 없었다면 else: 이후 문장을 실행합니다.

문제187. 아까 했던 나누기 프로그램을 수정해서 나누기가 성공하면 성공적으로 나누기를 하였습니다. 라는 메시지가 출력되게 하세요.
try :
    x = int(input('분자의 숫자를 입력하세요~'))
    y = int(input('분모의 숫자를 입력하세요~'))
    print(x/y)
except:
    print('당황하셨겠지만 잘못된 값을 입력하셔서 나누기 할 수 없습니다.')
else:
    print('성공적으로 나누기 하였습니다.')

■ 57. 예외처리 이해하기 (③ try~except~finally)
오류 발생 유무와 상관없이 어떤 코드를 무조 실행 시키려면 try~except~finally 구문을 활용합니다. 무조건 실행시키는 코드는 finally 부분에 작성하면 됩니다.

예 :
try :
	print('안녕하세요')
except:
	print('예외가 발생했습니다.')
finally:
	print('저는 무조건 실행됩니다.')
	
문제188. 나누기하는 프로그램을 실행할 때 오류가 나던 오류가 나지 않던 무조건 '송종미가 만든 프로그램입니다.' 가 출력되게 하시오!
try :
    x = int(input('분자의 숫자를 입력하세요~'))
    y = int(input('분모의 숫자를 입력하세요~'))
    print(x/y)
except:
    print('당황하셨겠지만 잘못된 값을 입력하셔서 나누기 할 수 없습니다.')
finally:
    print('송종미가 만든 프로그램입니다.')