# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:54:44 2020

@author: Owner
"""



■ 직접 모듈 생성하기

지금 현재 작성한 코드가 어느 디렉토리에  어떤 이름으로 저장되어 있는지 확인하는 방법?

c:\User\Owner\untitled.3.py
c:\User\Owner\my_cal.py

def add_number(n1,n2):
	result =  n1 + n2
	return n1 + n2
	
위의 함수 스크립트를 c:\User\Owner\my_cal.py 라는 이름으로 저장을 합니다.

메뉴에 새로운 창을 여세요.

import my_cal #my_cal 모듈을 임폴트합니다.
print(my_cal.add_number(1,2)) #my_cal 모듈안에 add_number 함수를 실행하시오.

설명 : 이번 창에서는 def 로 add_number 함수를 만드는 코드는 없습니다.
my_cal.py 모듈안에 있는데 그 모듈을 이 창에서 사용할 수 있도록 import를 했습니다.

문제148. my_cal.py 모듈 스크립트 안에 곱하기를 하는 아래의 함수를 추가하시오!
def gob_number(n1,n2):
	result = n1*n2
	return result
	

문제149. 다른 새로운 창에서 my_cal 모듈을 임폴트하고 gob_number 함수를 실행하시오!
import my_cal
print(my_cal.gob_number(1,2))

문제150. 이번에는 나누기를 하는 함수를 my_cal.py에 저장하고 다른 새로운 창에서 아래와 같이 import 하고 실행 될 수 있도록 하시오!
def devide(n1,n2):
    result = n1/n2
    return result

import my_cal
print(my_cal.devide(10,2)) #5
