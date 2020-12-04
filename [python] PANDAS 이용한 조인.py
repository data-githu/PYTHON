# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:29:20 2020

@author: Owner
"""


■ 65. pandas 를 이용한 조인

예제 : 이름과 부서위치를 출력하시오!
SQL> 
select e.ename, d.loc
	from emp e, dept d
	where e.deptno = d.deptno;
	
Pandas>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno')
print(result)
print(result[['ename','loc']])

문제205. DALLAS에서 근무하는 사원들의 이름과 부서위치를 출력하시오!
SQL>
select e.ename, d.loc
	from emp e, dept d
	where e.deptno = d.deptno and d.loc = 'DALLAS';
	
Pandas>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno')
print(result[['ename','loc']][result['loc']=='DALLAS'])

문제206. 월급이 3000이상인 사원들의 이름과 부서위치를 출력하시오!
SQL>
select e.ename, e.sal, d.loc
	from emp e, dept d
	where e.deptno = d.deptno and e.sal >= 3000;
	
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno')
print(result[['ename','sal','loc']][result['sal']>=3000])

문제207. 부서번호가 10번, 20번인 사원들의 이름과 부서위치와 부서번호를 출력하시오!
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno')
print(result[['ename','loc','deptno']][result['deptno'].isin ([10,20]) ])

문제208. 월급이 1000에서 3000 사이인 사원들의 이름과 월급과 부서위치를 출력하시오!
SQL>
select e.ename, e.sal, d.loc
	from emp e, dept d
	where e.deptno = d.deptno and e.sal between 1000 and 3000;
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno')
print(result[['ename','sal','loc']][result['sal'].between(1000,3000) ])

문제209. 아래의 SQL을 PANDAS로 구현하시오!
SQL>
select e.ename, d.loc
	from emp e, dept d
	where e.deptno  (+) = d.deptno;
	
PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno',how='right')
print(result[['ename','loc']])

문제210. 아래의 SQL을 pandas로 구현하시오!
SQL> 
select e.ename, d.loc
	from emp e full outer join dept d
	on(e.deptno = d.deptno);

PANDAS>
import pandas as pd
emp = pd.read_csv("c:\\data\\emp3.csv")
dept = pd.read_csv("c:\\data\\dept3.csv")
result = pd.merge(emp, dept, on='deptno',how='outer')
print(result[['ename','loc']])

