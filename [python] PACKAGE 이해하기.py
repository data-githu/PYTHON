# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:08:05 2020

@author: Owner
"""



■ 44. 파이썬 패키지 이해하기
우리가 음악파일을 저장할 때 장르별로 폴더를 만들어서 저장하는 듯이 파이썬 모듈도 음악처럼 갯수가 많아지면 폴더(모듈 꾸러미) 별로 별도로 관리를 해야 관리자가 편해지는데 이 폴더가 바로 '패키지' 입니다.

패키지(폴더)                vs        모듈(폴더 안의 my_cal.py 같은 파이썬 스크립트)

■ 파이썬 패키지를 만드는 단계
	1. 아래의 디렉토리에 my_loc 라는 폴더를 생성합니다.
	c:\\Users\\stu
	c:\\Users\\stu\my_loc
	
	2. my_loc 폴더 안에 my_cal.py 를 옮겨 놓는다.
	(my_cal.py 를 my_loc 폴더에 복사하고 기존에 있던 my_cal.py는 지우시오.)
	3. 이 평범한 폴더가 패키지로 인정을 받으려면 반드시 갖고 있어야하는 파일이 있습니다. 그 파일이 _init_.py라는 파일입니다.
c:\\User\\stu\my.loc
	1) __init__.py 
	2) my_cal.py

	4. 새로운 창에서 아래와 같이 스크립트를 수행합니다.
from my_loc import my_cal # from 패키지 import 모듈
print(my_cal.add_number(1,2))

어제 위와 비슷한 스크립트를 보았습니다.
from scipy.stats import norm # scipy 패키지 안에 stats 라는 패키지에 norm 이라는 모듈을 임폴트하시오.

print(norm.pdf(x,평균,표준편차)) #norm 모듈에 pdf (확률밀도함수)를 실행하시오.
