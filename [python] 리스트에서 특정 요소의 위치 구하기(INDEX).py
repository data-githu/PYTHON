# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:26:20 2020

@author: Owner
"""

■ 98. 리스트에서 특정 요소의 위치구하기(index)

리스트 객체의 index() 메소드는 리스트에서 요소의 값을 알고 있을때 그 요소가 최초로 나타나는 위치의 인덱스를 리턴합니다.

예제 : 
a = [1,2,'a','b','c',[1,2,3]]
print(a.index(2)) #1
print(a.index('a')) #2

문제303. 아래의 리스트에서 숫자 4의 인덱스 번호를 출력하시오!
print(a.index(4)) #ValueError: 4 is not in list

답 : 리스트 안에 있는 리스트의 인덱스 번호 출력못합니다.
