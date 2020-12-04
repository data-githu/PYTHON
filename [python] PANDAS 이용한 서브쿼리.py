# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:26:52 2020

@author: Owner
"""


■ 66. Pandas 를 이용한 서브쿼리 

예제 : JONES 보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하시오!
SQL>
select ename, sal
	from emp 
	where sal > (select sal from emp where ename = 'JONES');
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")


jsal = emp['sal'][emp['ename']=='JONES'].values[0]
print(emp[['ename','sal']][emp['sal']> jsal])


문제211. 아래의 서브쿼리를 PANDAS 로 구현하시오!
SQL>
select ename, sal
	from emp
	where job = (select job from emp where ename = 'SCOTT');
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")


sjob = emp['job'][emp['ename']=='SCOTT'].values[0]
print(emp[['ename','sal']][emp['job'] == sjob])


문제212. 아래의 서브쿼리의 결과를 PANDAS 로 수행하시오!
SQL>
select ename, sal
	from emp
	where job = (select job from emp where ename = 'SCOTT' )
	and ename != 'SCOTT';

PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")


sjob = emp['job'][emp['ename']=='SCOTT'].values[0]
print(emp[['ename','sal']][(emp['job'] == sjob ) & (emp['ename'] != 'SCOTT')])

설명 : 판다스에서 and는 & 이고 or 는 | 입니다.
& 와 | 를 쓸때는 괄호로 묶어줘야합니다.
