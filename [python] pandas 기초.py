# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:44:34 2020

@author: Owner
"""


■ 25. 판다스(pandas) 사용법

*pandas 란?
	1. 데이터 분석을 위한 파이썬 모듈
	2. 엑셀의 스프레드 시트와 같은 관계형 데이터베이스와 데이터 처리 능력이 뛰어남
	3. 판다스는 dataframe 이라는 기본 자료구조를 사용
	(오라클의 테이블과 판다스의 dataframe 이 서로 유사합니다.)

예제1. emp3.csv를 파이썬을 이용해서 pandas의 데이터프레임으로 만드시오!

지금 카페에 올린 emp3.csv 와 dept3.csv 를 c드라이브 밑에 data라는 폴더를 만들고 그밑에 복사해 둡니다.

import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp)

설명 : 판다스의 read_csv 함수는 os의 csv 파일을 읽어서 파이썬에서 판다스 데이터 프레임으로 만들겠다는 의미입니다.

SQL ----> 데이터에서 정보를 얻어내기 위해서 (데이터 검색) 
파이썬의 판다스 ----> 데이터를 검색하는 모듈

문제76. SQL ----> 판다스 문법 사원 테이블에서 이름과 월급을 출력하시오!

SQL >select ename, sal
		from emp;
	
PANDAS >
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']])


문제77. 아래의 SQL을 판다스로 구현하시오!
SQL >select ename, sal, job, hiredate
		from emp;
	

PANDAS >
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal','job','hiredate']])


문제78. 아래의 SQL 을 판다스로 구현하시오!

SQL >select ename, sal
		from emp
		where job = 'SALESMAN';


PANDAS >
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['job'] == 'SALESMAN'])

문제79. 월급이 3000이상인 사원들의 이름과 월급을 출력하시오!
SQL >select ename, sal
		from emp
		where sal >=3000;

PANDAS >
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['sal']>= 3000 ] )


문제80. 아래의 SQL을 판다스로 구현하시오!

SQL > select ename, sal
		from emp
		where sal between 1000 and 3000;

PANDAS >
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['sal'].between(1000,3000) ] )

문제81. 월급이 1000에서 3000 사이가 아닌 사원들의 이름과 월급을 출력하시오!
SQL > select ename,sal
		from emp
		where sal not between 1000 and 3000;

PANDAS >
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][~emp['sal'].between(1000,3000) ] )


■ 오라클의 기타 비교 연산자와 파이썬 판다스의 비교


          오라클                vs                   판다스
	1. between .. and                           emp['sal'].between(1000,3000)
	2. in                                            emp['job'].isin('SALESMAN','ANALYST')
	3. is null                                       emp['comm'].isnull()
	4. like                                          apply함수
	


문제82. 직업이 CLERK, SALESMAN 인 사원들이 이름과 직업을 출력하시오!
SQL >
select ename, job
	from emp
	where job = 'CLERK' or job = 'SALESMAN';
	
PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][emp['job'].isin(['SALESMAN','CLERK'])])


문제83. 직업이 CLERK, SALESMAN 이 아닌 사원들의 이름과 직업을 출력하시오!
SQL >

select ename, job
	from emp
	where job not in ( 'CLERK','SALESMAN');

PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','sal']][~emp['job'].isin(['SALESMAN','CLERK'])])

문제84. 커미션이 null 인 사원들의 이름과 커미션을 출력하시오!
SQL >
select ename,comm
	from emp
	where comm is null;
	
PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','comm']][emp['comm'].isnull()])



문제85. 커미션이 null 이 아닌 사원들의 이름과 커미션을 출력하시오!

SQL > 
select ename, comm
	from emp
	where comm is not null;

PANDAS>
import pandas as pd
emp=pd.read_csv("c:\\data\\emp3.csv")
print(emp[['ename','comm']][~emp['comm'].isnull()])





