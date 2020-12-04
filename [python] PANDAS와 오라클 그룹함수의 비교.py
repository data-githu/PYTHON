# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:30:04 2020

@author: Owner
"""


■ 67. Pandas 와 오라클 그룹함수의 비교 
예 : emp 테이블의 최대월급을 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp['sal'].max())


설명:
emp['sal'].max() : 최대월급
emp['sal'].min() : 최소월급
emp['sal'].avg() : 평균월급

문제213. 아래의 SQL을 판다스로 구현하시오!
SQL>
select max(sal)
	from emp
	where deptno = 20;

PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp['sal'][emp['deptno'] == 20].max())


문제214. 아래의 SQL을 판다스로 구현하시오!
SQL>
select min(sal)
	from emp
	where job = 'SALESMAN';


PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
print(emp['sal'][emp['job'] == 'SALESMAN'].min())

문제216. 우리반에서 최소나이를 출력하시오!
import pandas as pd
emp12 = pd.read_csv("c:\\data\\emp122.csv")
print(emp12['AGE'].min())

문제217. 아래의 SQL 을 판다스로 구현하시오!
SQL>
select job, max(sal)
	from emp
	group by job;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('job')['sal'].max().reset_index()
print(type(result))# <class 'pandas.core.frame.DataFrame'>
print(result)

※ 설명 : reset_index() 키워드는 series(컬럼) 로 출력하는게 아니라 DataFrame(테이블) 으로 출력하는 키워드 입니다.

문제218. 아래의 SQL을 판다스로 구현하시오!
SQL> 
select deptno, sum(sal)
	from emp
	group by deptno;
	
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].sum().reset_index()
print(result)

문제219. 아래의 SQL을 PANDAS로 구현하시오!
SQL>
select deptno, sum(sal)
	from emp
	where deptno != 20
	group by deptno;
	
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
result = emp.groupby('deptno')['sal'].sum().reset_index()
print(result[['deptno','sal']][result['deptno'] != 20])



