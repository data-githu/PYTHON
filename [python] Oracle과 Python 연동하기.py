# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:47:20 2020

@author: Owner
"""

■ 148. 오라클과 파이썬 연동하기

                               연동
   오라클 database -------------------- 파이썬
   비즈니스 데이터                         통계구현, 시각화, 머신러닝, 업무자동화
   (정형화된 데이터)

*오라클과 파이썬을 연동하는 이유?
	1. 오라클 데이터 베이스에서 실시간으로 변하는 데이터를 csv 파일로 매번 내리려면 자주 내려야 하므로 바로 연동합니다.
	2. 파이썬의 여러 장점들을 이용해서 데이터 분석을 할 수 있기 때문입니다.
	(통계구현, 시각화, 머신러닝, 업무자동화)
	3. 폐사진을 숫자로 변환해서 오라클 database에 저장합니다.
	이미지를 숫자로 변환해서 오라클 database에 저장합니다.
	db 에 저장하고 관리를 합니다. os에 파일로만 남겨두지 않습니다.
	db 에 저장하면 장점이 백업과 복구를 할 수 있습니다. 그리고 좀 더 효율적으로 data를 관리할 수 있습니다.
	os에 파일로 저장되어 있으면 바이러스에 노출될 수도 있습니다.
	
	
*빅데이터 기사 시험 : 데이터의 구조에 따른 종류 3가지
	1. 정형화 데이터 : rdbms 에 저장된 데이터
	(relational database management system : 관계형 데이터 베이스 관리 시스템)
	2. 반정형 데이터 : html, 웹로그 데이터
	3. 비정형화 데이터 : 텍스트, 동영상, 이미지 데이터


*오라클과 파이썬 연동

	1. 도스창을 열고 리스너의 상태를 확인합니다.
	리스너의 상태 확인하는 명령어 : lsnrctl status

외부에서 오라클에 접속하려면 리스너를 통해야만 접속이 됩니다.
리스너가 접속을 허용해주어야 접속이 됩니다.
리스너가 가지고 있는 정보중 3가지를 확인해야 합니다.
	1) ip주소 (건물주소) : localhost
	2) 포트번호 (건물안의 복도) : 1521
	3) 서비스 이름 (회사 이름) : xe

	2. 우의 정보들을 이용해서 오라클 database 에 접속을 해봅니다.
	C:\Users\Owner>sqlplus sys/oracle as sysdba
	sqlplus system/oracle@localhost:1521/xe
	C:\Users\Owner>sqlplus sys/oracle@localhost:1521/xe as sysdba
	
	3. 아나콘다 프롬프트 창을 열고 cx_Oracle 모듈을 설치합니다.
	conda install cx_Oracle
	
	4. 파이썬에서 오라클과 연동하는 코드를 작성합니다.
	(spyder에서 작성하세요.)
	import cx_Oracle
	import pandas as pd
	   	
	dsn = cx_Oracle.makedsn("localhost",1521,'xe') #오라클 주소를 기입
	db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) #오라클 접속 유저 정보
	cursor = db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언함
	cursor.execute("""select * from emp""") #작성한 쿼리문의 결과가 cursor 메모리에 담긴다.
	row = cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
	emp = pd.DataFrame(row)
	print(emp)
	
	
문제440. 위의 emp 테이블 전체를 select 했는데 전체를 다 select 하지말고 아래의 쿼리의 결과만 select 하시오!

select empno, ename, sal, deptno
	from emp;
	
	
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') #오라클 주소를 기입
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) #오라클 접속 유저 정보
cursor = db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언함
cursor.execute("""select empno, ename, sal, deptno from emp""") #작성한 쿼리문의 결과가 cursor 메모리에 담긴다.
row = cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print(emp)


문제441. dept 테이블의 모든 데이터를 조회하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') #오라클 주소를 기입
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) #오라클 접속 유저 정보
cursor = db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언함
cursor.execute("""select * from dept""") #작성한 쿼리문의 결과가 cursor 메모리에 담긴다.
row = cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
dept = pd.DataFrame(row)
print(dept)


문제442. 우리반 테이블(emp12)를 조회하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') #오라클 주소를 기입
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) #오라클 접속 유저 정보
cursor = db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언함
cursor.execute("""select * from emp12""") #작성한 쿼리문의 결과가 cursor 메모리에 담긴다.
row = cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp12 = pd.DataFrame(row)
print(emp12)


문제443. 월급이 1200 이상인 사원들의 이름과 월급을 출력하세요!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') #오라클 주소를 기입
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) #오라클 접속 유저 정보
cursor = db.cursor() #결과 데이터를 담을 메모리 이름을 cursor로 선언함
cursor.execute("""select ename, sal from emp where sal >= 1200 """) #작성한 쿼리문의 결과가 cursor 메모리에 담긴다.
row = cursor.fetchall() #cursor 메모리에 담긴 결과를 한번에 row 변수에 담는다.
emp = pd.DataFrame(row)
print(emp)


문제444. 이름과 월급으로 막대그래프를 그리시오.
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor() 
cursor.execute("""select ename, sal  from emp""") 
row = cursor.fetchall() 
emp = pd.DataFrame(row)

emp.index = list(emp[0])
emp.plot(kind='bar')


문제445. 위의 그래프의 색깔을 변경하시오.
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor() 
cursor.execute("""select ename, sal  from emp""")row = cursor.fetchall() 
emp = pd.DataFrame(row)

emp.index = list(emp[0])
emp.plot(kind='bar', color = 'red')


문제446. 직업별 최대월급을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA)
cursor = db.cursor() 
cursor.execute("""select job, max(sal)  from emp group by job""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제447. 직업, 직업별 토탈월급을 출력하는데 직업별 토탈월급이 높은 것부터 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select job, max(sal)  from emp group by job order by max(sal) desc""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제448. 이름, 월급, 순위를 출력하는데 순위가 월급이 높은 사원 순서대로 순위를 부여하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select ename, sal, dense_rank() over(order by sal desc)  from emp""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제449. 부서번호, 부서번호별 토탈월급을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select deptno, sum(sal) from emp group by deptno""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제450. 위의 결과를 막대그래프로 시각화 하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select deptno, sum(sal) from emp group by deptno""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
emp.index = list(emp[0])
emp.plot(kind='bar', color = 'blue')


문제451. emp 테이블의 컬럼명을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select * from emp""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
colname = cursor.description
col =[]
for i in colname:
    col.append(i[0].lower())
print(col)


문제452. 위의 col 리스트에 담긴 컬럼명을 위의 데이터에 매핑시키시오.
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select * from emp""")
row = cursor.fetchall() 

colname = cursor.description
col =[]
for i in colname:
    col.append(i[0].lower())
emp = pd.DataFrame(list(row),columns=col)
print(emp)


문제453. 위의 컬럼명을 이용해서 판다스 문법으로 이름과 월급을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select * from emp""")
row = cursor.fetchall() 

colname = cursor.description
col =[]
for i in colname:
    col.append(i[0].lower())
emp = pd.DataFrame(list(row),columns=col)
print(emp[['ename','sal']])


문제454. 월급이 3000이상인 사원들 이름과 월급을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select * from emp""")
row = cursor.fetchall() 

colname = cursor.description
col =[]
for i in colname:
    col.append(i[0].lower())
emp = pd.DataFrame(list(row),columns=col)
print(emp[['ename','sal']][emp['sal'] >= 3000])


문제455. 이름과 부서위치를 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select e.ename, d.loc from emp e, dept d where e.deptno = d.deptno""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제456. 부서위치, 부서위치별 토탈월급을 출력하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select d.loc, sum(e.sal) from emp e, dept d where e.deptno = d.deptno group by d.loc""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)


문제457. 위의 결과를 막대그래프로 시각화 하시오!
import cx_Oracle
import pandas as pd
   	
dsn = cx_Oracle.makedsn("localhost",1521,'xe') 
db = cx_Oracle.connect('system','oracle',dsn,cx_Oracle.SYSDBA) 
cursor = db.cursor()
cursor.execute("""select d.loc, sum(e.sal) from emp e, dept d where e.deptno = d.deptno group by d.loc""")
row = cursor.fetchall() 
emp = pd.DataFrame(row)
print(emp)

emp.index = list(emp[0])
emp.plot(kind='bar', color = 'blue')


