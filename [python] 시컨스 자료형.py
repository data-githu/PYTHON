# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:23:26 2020

@author: Owner
"""

■ 26. 시퀀스 자료형 이해하기

시퀀스 자료형은 어떤 객체가 순서를 가지고 나열되어 있는 것을 말합니다. 예를 들면 문자열 'abcd' 는 문자 a,b,c,d 가 순서를 가지고 차례대로 나열되어 있는 것입니다.
예 : 
a = 'scott'
print(a)

위의 scott 이라는 문자를 담은 a 변수에서 첫번째 요소만 출력하고 싶다면 ?
예 : 
a = 'scott'
print(a[0])

문제87. 위의 SCOTT 을 담은 문자형 변수 a에서 알파벳 O를 출력하시오!
a= 'SCOTT'
print(a[2])

문제88. 아래의 문자형 변수에서 맨 끝의 철자인 h를 출력하시오!
b='smith'
print(b[4])

문제89. 판다스를 사용해서 emp3.csv 에서 이름을 출력하는데 이름의 첫번째 철자만 출력하시오!

SQL>
select substr(ename,1,1)
	from emp;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i[0]) # 문자형만 가능


print(type( emp['ename'])) # 데이터 타입을 알아보는 방법

설명 : type 명령어는 변수가 문자형, 숫자형, 리스트형, 딕셔너리형, 튜플형인지 확인하는 함수입니다.

a='scott'
print(type(a))
print(a[0])

설명 : <class.'str'> 문자형으로 변경해줘야 문자형에서 특정 요소를 가져오는 문법을 사용할 수 있습니다.
예  : a[0]
판다스의 <class'pandas.core.series.Series'> 를 문자형으로 변경하려면 for loop 문을 이용해서 하나씩 가져오면 됩니다.
예 : for i in emp['ename']
	print(i)


문제90. 판다스를 이용해서 emp3.csv 를 가져와서 이름이 끝글자를 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i[-1])

문제91. 위의 결과에서 앞에 이름도 같이 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i,i[-1])

문제92. 이름의 첫번째 철자가 S로 시작하는 사원들의 이름을 출력하시오!
SQL>
select ename
	from emp
	where ename like 'S%';
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    if i[0] == 'S':
        print(i)

문제93. 이름의 끝글자가 T로 끝나는 사원들의 이름을 출력하시오.
SQL>
select ename
	from emp
	where ename like '%T';
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    if i[-1] == 'T':
        print(i)

■ 27. 시퀀스 자료 인덱싱 이해하기

인덱싱이란 시퀀스 자료형에서 인덱스를 통해 해당하는 값을 얻는 방법입니다. 파이썬에서는 인덱스를 0부터 시작하며 음수인 인덱스도 사용가능합니다.
음수인덱스는 끝에서부터 몇번째라는 의미를 갖습니다.

예 : 
a='SALESMAN'
print(a[2]) # L이 출력됩니다.

문제94. 이름의 두번째 철자가 M인 사원의 이름을 출력하시오!
SQL>
select ename
	from emp
	where ename like '_M%';
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
    if i[1] == 'M':
        print(i)


■ 28. 시퀀스 자료 슬라이싱 이해하기

  인덱싱은 인덱스에 해당하는 요소 하나를 취하는 방법이지만
  슬라이싱은 시퀀스 자료에서 일정 범위에 해당하는 부분을
  취하는 방법입니다. 


문제95. 아래의 SQL을 판다스로 구현하시오!
SQL>
select substr(ename,1,3)
	from emp;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i[0:3])


	
문제96. 아래의 SQL을 판다스로 구현하시오!
SQL > 
select substr(ename, -2, 2)
	from emp;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i,i[len(i)-2:len(i)])

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i[-2:])

문제97. 아래의 SQL을 판다스로 구현하시오!
SQL>
select substr(ename, 2,3)
	from emp;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i,i[1:4])

■ 29. 시퀀스 자료 연결 이해하기(+)

자료형이 동일한 두개의 시퀀스 자료는 + 연산자로 순서있게 연결하여 새로운 시퀀스 자료를 만들 수 있습니다.
문자열 + 문자열, 리스트 + 리스트, 튜플 + 튜플 과 같이 두개의 동일한 시퀀스 자료형에 대해 '+' 연산자로 연결이 가능합니다.

예제 : 
a = 'i love ' 
b = 'python'
print(a+b)


문제98. 아래의 두개의 리스트를 연결하여 출력하시오!
a=[2,3,4,5]
b=[9,2,4,8]
print(a+b)


문제99. 아래의 SQL을 판다스로 구현하시오!
SQL>
select ename || sal
	from emp;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i, k in zip(emp['ename'],emp['sal']):
    print(i + str(k))

설명 : zip 함수를 for loop 문에 사용하게 되면 두개의 범위 데이터를 한번에 받아서 loop를 수행할 수 있습니다.
str 함수를 사용한 이유는 문자형 + 문자형은 연결이 가능하지만, 문자형 + 숫자형은 연결이 되지 않습니다. 그래서 숫자형을 문자형으로 변환하기 위해서 str 함수를 사용했습니다.


■ 30. 시퀀스 자료 반복 이해하기(*)

동일한 시퀀스 자료를 반복하여 새로운 시퀀스 자료로 만들고자 하면 별표(*) 를 연산자로 사용합니다.

예제 :
print('a'*7) # 소문자 a를 7번 출력합니다.

print([1,2,3]*5) # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] 

문제100. 주사위의 눈 6개를 100개 담은 리스트 dice100을 만드시오.
dice100=[1,2,3,4,5,6]*100

print(dice100)

문제101. 초등학생 키가 10개 들어있는 아래의 tall 리스트의 요소 10개를 10000개로 증가시켜서 tall10000 리스트에 담고 출력하시오!
tall = [129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000
print(tall10000)

문제102. 위의 모집단의 평균, 분산, 표준편차를 출력하시오!
import numpy as np
tall = [129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000
print(np.mean(tall10000)) #136.66
print(np.var(tall10000)) #23.782399999999985
print(np.std(tall10000)) #4.876720209321013

문제103. 위의 모집단 tall10000에서 표본을 20개를 랜덤으로 추출하시오!
import random
tall = [129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000

for i in range(1,21):
    print( random.choice(tall10000))

문제104. 위의 랜덤으로 추출한 20개의 결과를 비어있는 a 리스트에 넣으시오!
import random
tall = [129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000
a = [ ]
for i in range(1,21):
    result  = random.choice(tall10000)
    a.append(result)
print(a)

문제105. 위의 표본 20개의 평균값을 출력하시오!
import random
import numpy as np
tall = [129.3, 130.2, 132.5, 134.7, 136.3, 137.8, 138.1, 140.2, 142.3, 145.2]
tall10000 = tall*10000
a = [ ]
for i in range(1,21):
    result  = random.choice(tall10000)
    a.append(result)
print(np.mean(a)) #136.46999999999997


■ 31. 시퀀스 자료 크기 이해하기(len)

모든 시퀀스 자료는 고정된 길이 또는 크기를 가지고 있습니다.
시퀀스 자료의 크기는 시퀀스 자료를 구성하는 요소의 갯수입니다.

예제 : 
a='scott'
print(len(a)) #5

b=[2,3,4,8,1]
print(len(b)) #5

문제106. 아래의 SQL을 판다스로 구현하시오!
SQL>
select ename, length(ename)
	from emp;


PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
for i in emp['ename']:
        print(i,len(i))
