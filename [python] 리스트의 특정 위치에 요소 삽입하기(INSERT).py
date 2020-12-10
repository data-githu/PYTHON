# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:39:12 2020

@author: Owner
"""

■ 107. 리스트의 특정 위치에 요소 삽입하기(insert)


리스트 객체의 inser() 메소드는 리스트의 특정 위치의 새로운 요소를 입력합니다.

예제 :
list_a = ['a','b','c','d','e']
list_a.append('f') # append 메소드는 무조건 맨 뒤쪽에 요소를 추가합니다.
print(list_a) 

list_a.insert(3,'k')
print(list_a)

설명 : list_a.inser(3,'k') 는 list_a 리스트의 인덱스 번호 3번으로 k를 구성하시오

문제319. 아래의 a리스트의 요소 화성 다음에 소행성을 요소를 입력하시오!
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
a.insert(a.index('화성')+1,'소행성')
print(a)