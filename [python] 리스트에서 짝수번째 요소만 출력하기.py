# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:11:41 2020

@author: Owner
"""

■ 101. 리스트에서 짝수번째 요소만 출력하기

리스트에서 짝수번째 요소를 추출하는 방법은 두번째 요소부터 끝까지 스텝 2로 슬라이싱하면 됩니다.

예제 : 
list_a = ['a','b','c','d','e','f','g','h']
print(list_a[1: :2])

문제307. 1-100까지의 숫자중에서 짝수만 list_a에 담아서 출력하시오!
list_a = list(range(2,101,2))
print(list_a)