# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:01:53 2020

@author: Owner
"""

■ 122. 사전의 특정 요소 제거하기(del)
사전 dict 에서 특정요소 key:value 를 제거하는 방법은 다음과 같습니다.

예제 : 
sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
del sol['태양']
print(sol)

문제358. 아래의 딕셔너리에서 다시만난세계의 값만 지우시오!
dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}

del dict['소녀시대'][0]
print(dict)