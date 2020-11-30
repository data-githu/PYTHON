# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:25:31 2020

@author: Owner
"""

■ 32. 멤버체크 이해하기 (in)
listdata = [1,2,3,4]

a = 1 in listdata
print(a) #True

b=5 in listdata
print(b) #False

문제107. 모평균이 30이고 모표준편차가 7인 모집단을 구성하시오!
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
print(population)
print(len(population))

설명 : np.random.randn(숫자) 를 쓰면 이 숫자만큼 가우시안 정규분표에 따르는 난수들이 숫자만큼 생성됩니다.

문제108. 위의 모집단의 모평균을 출력하시오!
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
print(np.mean(population)) #30.006525705643746

문제109. 아래의 SQL을 판다스로 구현하시오!
SQL>
select ename, job
	from emp
	where job in ('SALESMAN','ANALYST');
	
PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','job']][emp['job'].isin(['SALESMAN','ANALYST'])])

문제110. 아래의 SQL을 판다스로 구현하시오!
SQL>
select ename, job
	from emp
	where job not in ('SALESMAN', 'ANALYST');
	
PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','job']][~emp['job'].isin(['SALESMAN','ANALYST'])])
	



■ 33. 문자열 이해하기

문자열은 문자나 기호 순서로 나열되어 있는 시퀀스 자료입니다.

※ 문자열을 선언하는 방법 3가지
	1. '문자열' : 싱글 쿼테이션 마크
	2. "문자열" : 더블 쿼테이션 마크
	3. """문자열""" : 더블 쿼테이션 마크를 3번

문자에 아래와 같이 싱글 쿼테이션 마크(')가 포함되어져 있으면 위의 두번째의 더블 쿼테이션 마크를 사용하면 됩니다.

a = "My son's name is john"
print(a)

문자에 아래와 같이 더블 쿼테이션 마크가 있으면 위의 세번째인 """  """ 더블 3개를 사용하면 됩니다.

b = """My son's name is "john" """
print(b)


문제111. 아래와 같은 글씨가 출력되게 하시오!
"모집단"의 모평균은 
"모집단"의 모분산은
"모집단"의 모표준편차는

a = """ "모집단"의 모평균은 """
b = """ "모집단"의 모분산은 """
c = """ "모집단"의 모표준편차는 """

print(a)
print(b)
print(c)


문제112. 모평균이 30이고 모표준편차가 7인 모집단 1000000의 모평균과 모분산과 모표준편차를 아래와 같이 출력하시오!
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
print(""" "모집단"의 모평균은 """, np.mean(population))
print(""" "모집단"의 모분산은 """ ,np.var(population))
print(""" "모집단"의 모표준편차는 """, np.std(population))

문제113. 모평균이 30이고 모표준편차가 7인 모집단(1000000개)에서 표본을 49개 추출하시오!
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
print(np.random.choice(population,49))



문제114. 위의 결과의 평균을 출력하세요.
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
print(np.random.choice(population,49).mean())

설명 : numpy의 random 안에 choice 함수를 이용해서 모집단에서 49개를 표본추출하고 그 표본의 평균값을 출력하였습니다.

문제115. 위에서 출력한 표본의 평균값을 하나가 아니라 100개가 출력되게하시오!
import numpy as np

avg = 30
std = 7
N = 1000000

population= np.random.randn(N) * std+avg
for i in range(1,101):
    print(np.random.choice(population,49).mean())

문제116. 이번에는 100개를 출력하지 말고 비어있는 리스트 a 에 담으시오.
import numpy as np

avg = 30
std = 7
N = 1000000
a=[]

population= np.random.randn(N) * std+avg
for i in range(1,101):
    a.append(np.random.choice(population,49).mean())

문제117. 위에서 구한 표본평균의 평균값과 표준편차를 아래와 같이 출력하시오!
 "표본평균" 의 평균값은 ? 
 "표본평균" 의 표준편차는 ? 


import numpy as np

avg = 30
std = 7
N = 1000000
a=[]

population= np.random.randn(N) * std+avg
for i in range(1,101):
    a.append(np.random.choice(population,49).mean())
print(""" "표본평균" 의 평균값은 ?""", np.mean(a))
print(""" "표본평균" 의 표준편차는 ?""",np.std(a))

■ 34. 문자열 포맷팅 이해하기

문자열 포맷팅에서는 변하는 값을 나타내기 위해 사용하는 기호를 '포맷 문자열'이라고 합니다.

포맷문자열
%S                    문자열에 대응됨
%C                    문자나 기호 한 개에 대응됨
%F                     실수에 대응됨
%D                     정수에 대응됨
%%                     %라는 기호 자체를 표시함

예제 : 
txt1 = '자바'
txt2 = '파이썬'
num1 = 5
num2 = 10
print('나는 %s보다 %s에 더 익숙합니다.', %(txt1,txt2))
print('나는' ,txt1, '보다',txt2, '에 더 익숙합니다.' )


문제118. 아래의 변수를 이용해서 아래와 같이 결과가 출력되게 하시오!
num1 = 5
num2 = 10
print('%d는 %d 보다 작습니다.' %(num1,num2))

문제119. 문제117번의 결과가 아래와 같이 출력되게 하시오!
import numpy as np

avg = 30
std = 7
N = 1000000
a=[]

population= np.random.randn(N) * std+avg
for i in range(1,101):
    a.append(np.random.choice(population,49).mean())
print('표본평균의 평균값은 %f 이고 분산값은 %f 이고 표준편차는 %f 입니다.' %(np.mean(a),np.var(a),np.std(a)))

문제120. 위의 결과가 소수점 두번째 자리까지만 나오게 하시오!
import numpy as np

avg = 30
std = 7
N = 1000000
a=[]

population= np.random.randn(N) * std+avg
for i in range(1,101):
    a.append(np.random.choice(population,49).mean())
print('표본평균의 평균값은 %f 이고 분산값은 %f 이고 표준편차는 %f 입니다.' %(round(np.mean(a),2),round(np.var(a),2),round(np.std(a),2)))
---------------------------------------------------------------------------------------------------------
import numpy as np

avg = 30
std = 7
N = 1000000
a=[]

population= np.random.randn(N) * std+avg
for i in range(1,101):
    a.append(np.random.choice(population,49).mean())
print('표본평균의 평균값은 %.2f 이고 분산값은 %.2f 이고 표준편차는 %.2f 입니다.' %(round(np.mean(a),2),round(np.var(a),2),round(np.std(a),2)))


문제121. (통계를 코드로 구현 문제 4번의 링크2) 오늘의 마지막 문제
어느 비행기 탑승객의 짐의 무게는 평균이 18kg 이고 표준편차가 3인 정규분표를 따른다고 한다. 이 비행기 탑승객 중에서 36명을 임의추출할 때, 짐의 평균 무게가 17kg 이상일 확률을 구하여라
import random
import numpy as np

avg = 18
std = 3
N = 1000000
cnt = 0

population= np.random.randn(N) * std+avg
for i in range(1,10001):
    result =  np.random.choice(population,36).mean()
    if result >= 17 :
        cnt = cnt + 1
print(cnt/10000)


