# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:28:28 2020

@author: Owner
"""


■ 64. Pandas 를 이용한 데이터 검색
SQL과 PANDAS 를 자유롭게 사용할 수 있어야 합니다.
SQL --> PANDAS
PANDAS --> SQL

예제 : emp[['ename','sal']][emp['ename']=='SCOTT']
		컬럼                     조건

문제203. dept3.csv 를 판다스로 로드해서 dept 데이터 프레임 전체를 출력하시오!
import pandas as pd 

dept = pd.read_csv("c:\\data\\dept3.csv")
print(dept)

문제204. 부서위차가 DALLAS 의 부서번호와 부서명을 출력하시오!
import pandas as pd 

dept = pd.read_csv("c:\\data\\dept3.csv")
print(dept[['deptno','dname']][dept['loc']=='DALLAS'])
