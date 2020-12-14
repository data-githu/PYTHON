# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:58:02 2020

@author: Owner
"""

■ 120. 사전에 요소 추가하기

파이썬 책 큰 목차 : 
	1. 문자형과 문자형 함수들
	2. 숫자형과 숫자형 함수들
	3. 리스트형과 리스트형 함수들
	4. 사전형과 사전형 함수들

사전형은 키:값으로 되어진 요소로 구성되어 있습니다.
사전형은 리스트형처럼 인덱스 번호로 요소에 접근하는게 아니라 키값으로 요소의 값에 접근합니다.

예제 : 
sol = { }
sol['태양'] = 'sun'
sol['수성'] = 'mercury'
sol['금성'] = 'venus'
print(sol) #{'태양': 'sun', '수성': 'mercury', '금성': 'venus'}

문제355. 아래의 두개의 리스트를 가지고 sol 딕셔너리를 생성하시오!
sol ={}
sol_eng =[ 'sun','mercury','venus','earth','mars']
sol_kor = ['태양','수성','금성','지구','화성']

for i, k in zip(sol_kor, sol_eng):
    sol[i]=k
print(sol)