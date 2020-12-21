# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:17:58 2020

@author: Owner
"""


■ 149. 파이썬과 mySQL 연동
현업에서는 오라클도 많이 쓰지만 mySQL도 많이 사용합니다.
오라클은 비용이 비싸서 중요한 데이터는 오라클에 저장하고 상대적으로 덜 중요한 데이터는 mySQL에 저장합니다.

*mySQL 설치하고 사용하는 방법
mysql > create database orcl;
mysql > use orcl;

mysql 에서 emp 테이블 생성하는 스크립트 파일
Create table emp
(empno int(4) not null,
Ename varchar(10),
Job varchar(9),
Mgr int(4),
Hiredate date,
Sal int(7),
Comm int(7),
Deptno int(4) );

create table dept
(deptno int(2),
dname varchar(20),
loc varchar(20) );

INSERT INTO dept VALUES (10,'ACCOUNTING','NEW YORK');
INSERT INTO dept VALUES (20,'RESEARCH','DALLAS');
INSERT INTO dept VALUES (30,'SALES','CHICAGO');
INSERT INTO dept VALUES (40,'OPERATIONS','BOSTON');

INSERT INTO emp VALUES (7839,'KING','PRESIDENT',NULL,'81-11-17',5000,NULL,10);
INSERT INTO emp VALUES (7698,'BLAKE','MANAGER',7839,'81-05-01',2850,NULL,30);
INSERT INTO emp VALUES (7782,'CLARK','MANAGER',7839,'81-05-09',2450,NULL,10);
INSERT INTO emp VALUES (7566,'JONES','MANAGER',7839,'81-04-01',2975,NULL,20);
INSERT INTO emp VALUES (7654,'MARTIN','SALESMAN',7698,'81-09-10',1250,1400,30);
INSERT INTO emp VALUES (7844,'TURNER','SALESMAN',7698,'81-08-21',1500,0,30);
INSERT INTO emp VALUES (7900,'JAMES','CLERK',7698,'81-12-11',950,NULL,30);
INSERT INTO emp VALUES (7521,'WARD','SALESMAN',7698,'81-02-23',1250,500,30);
INSERT INTO emp VALUES (7902,'FORD','ANALYST',7566,'81-12-11',3000,NULL,20);
INSERT INTO emp VALUES (7369,'SMITH','CLERK',7902,'80-12-09',800,NULL,20);
INSERT INTO emp VALUES (7788,'SCOTT','ANALYST',7566,'82-12-22',3000,NULL,20);
INSERT INTO emp VALUES (7876,'ADAMS','CLERK',7788,'83-01-15',1100,NULL,20);
INSERT INTO emp VALUES (7934,'MILLER','CLERK',7782,'82-01-11',1300,NULL,10);
commit;


문제458. 월급이 3000 이상인 사원들의 이름과 월급을 출력하시오
mysql> select ename, sal
    -> from emp
    -> where sal >=3000 ;


문제459. 직업이 SALESMAN인 사원들의 이름과 월급과 직업을 출력하는데 월급이 높은 사원부터 출력하시오!
mysql> select ename, sal, job
    -> from emp
    -> where job = 'SALESMAN'
    -> order by sal desc;

문제460. 이름과 부서위치를 출력하시오!
mysql> select e.ename, d.loc
    -> from emp e, dept d
    -> where e.deptno = d.deptno;


문제461. 존보다 월급을 더 많이 받는 사원의 이름과 월급을 출력하시오!
mysql> select ename, sal
    -> from emp
    -> where sal > (select sal from emp where ename = 'JONES');


문제462. 이름, 월급, 순위를 출력하시오!
mysql> select ename, sal, dense_rank() over (order by sal desc)
    -> from emp;


■ Oracle과 MySQL 함수 비교

         Oracle      vs       MySQL
	1. nvl                       ifnull
	2. sysdate                 sysdate()
	3. month_between     period_add
	4. decode                 if
	5. rollup                  with rollup
	6. listagg                  group_concat
	
	
문제463. 이름, 커미션을 출력하는데 커미션이 null 인 사람들은 모두 0으로 출력하시오!
mysql> select ename, ifnull(comm,0)
    -> from emp;


문제464. 오늘날짜를 출력하시오!
mysql> select sysdate()
    -> ;


문제465. 부서번호, 부서번호별 토탈월급을 출력하시오!
mysql> select deptno, sum(sal)
    -> from emp
    -> group by deptno;


문제466. 위의 결과를 다시 출력하는데 맨 아래에 전체 토탈월급이 출력되게하세요!
mysql> select deptno, sum(sal)
    -> from emp
    -> group by deptno with rollup;


문제467. scott의 월급을 0으로 변경하세요.
mysql> update emp
    -> set sal = 0
    -> where ename = 'SCOTT';

※ mysql 은 오라클과는 다르게 기본 자동커밋이 활성화 되어있습니다. 
자동 커밋이 되어서 rollback을 실행할 수 없습니다.


문제468. 자동 커밋이 활성화 되어져 있는지 확인해보세요.
select @@autocommit;

설명 : 숫자가 1이면 autocommit 이 켜있는 것입니다.


문제469. 자동커밋 기능을 끄세요.
mysql> set autocommit = FALSE;

설명 : 숫자가 0이면 자동 커밋기능이 비활성화 된 것입니다.


문제470. king의 월급을 0으로 바꾸세요.
mysql> update emp
    -> set sal = 0
    -> where ename = 'KING';

rollback;

문제471. 오라클의 listagg 함수와 같은 기능인 group_concat 을 이용해서 부서번호, 부서번호별로 속한 사원들의 이름을 가로로 출력하시오!
mysql> select deptno, group_concat(ename)
    -> from emp
    -> group by deptno;


문제472. mySQL과 파이썬을 연동해서 mySQL의 emp 테이블을 파이썬에서 출력하시오!

먼저 아나콘다 프롬프트 창을 열고 pymysql을 설치하세요.
conda install pymysql

import pymysql,pandas as pd
conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select * from emp"
curs.execute(sql)
rows = curs.fetchall()
colname = curs.description
col = []
for i in colname:
    col.append(i[0].upper())
emp = pd.DataFrame(list(rows),columns=col)
print(emp[['ENAME', 'SAL']] )


문제473. 직업, 직업별 토탈월급을 출력하시오
import pymysql,pandas as pd
conn = pymysql.connect(host="localhost", user="root",password="oracle", db="orcl",charset="utf8")

curs = conn.cursor()
sql = "select job, sum(sal) from emp group by job"

curs.execute(sql)
rows = curs.fetchall()

emp = pd.DataFrame(rows)
print(emp)


