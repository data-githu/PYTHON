# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:53:16 2020

@author: Owner
"""

■ 89. 문자열에서 문자 개수 구하기 (count)

문자열 객체의 count() 메소드는 문자열에서 특정 문자의 갯수를 리턴합니다.

예제:
txt = 'A lot of things occur each day. Today is beautiful day'
print(txt.count('day'))

문제280. 안철수 연설문에서 국민이라는 단어가 몇번 나오는지 카운트 하시오!
ahn = open("c:\\data\\ahn.txt",encoding='UTF8')
ahn2 = ahn.read().split()
cnt = 0
for i in ahn2:
    if i.count('국민') == 1:
        cnt = cnt +1 
print(cnt)


ahn = open("c:\\data\\ahn.txt",encoding='UTF8')
ahn2 = ahn.read()
print(ahn2.count('국민'))