# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:04:57 2020

@author: Owner
"""

■ 100. 리스트에서 특정 구간에 있는 요소 추출하기

예제 : 
list_a = ['a','b','c','d','e','f','g']
print(list_a [0:4])

문제305. 위에서 알파벳 a부터 g까지 담은 리스트를 만들었는데 이번에는 알파벳 a부터 z까지를 담는 리스트를 list_a에 생성하시오~
import string
list_a = []
for i in string.ascii_lowercase:
    list_a.append(i)
print(list_a)

문제306. 위에서 만든 list_a 에서 요소를 검색하는데 맨 끝에 알파벳 z를 빼고 모든 요소를 다 출력하시오!
import string
list_a = []
for i in string.ascii_lowercase:
    list_a.append(i)
print(list_a[:-1])

import string
list_a = []
for i in string.ascii_lowercase:
    list_a.append(i)
print(list_a[0:list_a.index('z')])