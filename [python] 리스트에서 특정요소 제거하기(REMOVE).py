# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:57:34 2020

@author: Owner
"""


■ 109. 리스트에서 특정 요소 제거하기(remove)

예제 : 아래의 a 리스트에서 목성을 지우시오!
a = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
a.remove('목성')
print(a)


문제321. 아래의 빨간공 2개와 파란공 3개가 들어있는 주머니에서 공을 하나 랜덤으로 빼면 그 공이 주머니에서 지워지게 하시오!

import random
box = ['red', 'red', 'blue', 'blue', 'blue']
result = random.choice(box)
if result =='red':
	box.remove('red')
else:
	box.remove('blue')
print(box)