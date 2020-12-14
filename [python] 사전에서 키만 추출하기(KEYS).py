# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:47:19 2020

@author: Owner
"""

■ 124. 사전에서 키만 추출하기(keys)
아래의 사전에서 key만 추출하고 싶으면 사전이름.keys() 라고 하면 됩니다.

예제 : 
sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
print(sol.keys())

문제360. 위의 sol 사전에 있는 키를 추출해서 아래와 같이 결과를 출력하시오!
태양,수성,금성,지구,화성
sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
bond = ','
print(bond.join(sol.keys()))

