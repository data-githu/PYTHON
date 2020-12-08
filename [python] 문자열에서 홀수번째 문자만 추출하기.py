# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:44:48 2020

@author: Owner
"""

■ 77. 문자열에서 홀수번째 문자만 추출하기
주어진 문자열에서 홀수번 문자만 추출하는 방법은 슬라이싱의 스텝을 이용하면 됩니다.

예제 : 
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
result = txt[0:] #0번째 부터 문자열 전체 출력
print(result)
result2 = txt[0::2]
print(result2) #문자열에서 2칸씩 건너뛰면서 출력

문제260. 위의 txt 문자열에서 짝수번째 철자들만 출력하시오!
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
result = txt[1::2]
print(result)