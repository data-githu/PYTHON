# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:50:24 2020

@author: Owner
"""

■ 115. 리스트 요소 정렬하기 ② sorted

파이썬 내장함수 sorted()를 이용하여 리스트를 정렬할 수도 있습니다.
리스트 객체의 sort() 메소드와 다른점은 리스트 객체의 sort()는 원본리스트를 정렬한 형태로 변경하지만 sorted()는 원본 리스트는 그대로 두고 정렬한 결과만 리턴합니다.

예제 : 
a = [2,1,3,5,4]
a.sort()
print(a) #[1, 2, 3, 4, 5]

a = [2,1,3,5,4]
b = sorted(a)
print(b) #[1, 2, 3, 4, 5]
print(a) #[2, 1, 3, 5, 4]
