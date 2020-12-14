# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:47:43 2020

@author: Owner
"""
■ 125. 사전에서 값만 추출하기 (values)
아래의 사전형에서 값에 해당하는 부분만 추출하려면 사전형 이름을 사용하면 됩니다.
sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
print(sol.values()) #dict_values(['sun','mercury','venus','earth','mars'])

문제362. 아래의 sol 딕셔너리에서 값들만 아래와 같이 출력되게 하시오!
sun,mercury,venus,earth,mars

sol = {'태양': 'sun', '수성': 'mercury', '금성': 'venus', '지구': 'earth', '화성': 'mars'}
bond = ','
print(bond.join(sol.values()))

문제363. 아래의 gini 딕셔너리에서 값만 출력하시오!
gini = {'비틀즈': ['yesterday', 'imagine'], '아이유': ['너랑나', '마슈멜로우'], '마이클 잭슨': ['beat it', 'smooth criminal']}
결과 : 
['yesterday', 'imagine']
['너랑나', '마시멜로우']
['beat it', 'smooth criminal']


gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
for i in gini.values():
    print(i)

문제364. 위의 결과를 다시 출력하는데 결과 리스트 3개 중에 0번째 요소만 출력하시오!
결과:
yesterday
너랑나
beat it

gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
for i in gini.values():
    print(i[0])

문제365. gini 딕셔너리에서 음악만 출력하는데 아티스트별로 노래가 겹치지 않도록 출력하시오.
import random

gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
b=[]
c=[]
bond=','
for j in gini.values():
        b.append(j[0])
        c.append(j[1])
result = bond.join(b+c)
print(result)

문제 366. 아래의 gini 딕셔너리의 값들의 리스트를 아래의 결과처럼 리스트에 담으시오!
[['yesterday', 'imagine'], ['너랑나', '마시멜로우'], ['beat it', 'smooth criminal']]

gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
gini2 = list(gini.values())
print(gini2)

문제367. 위에서 출력된 gini2 리스트의 요소들을 shuffle로 섞어보시오!
import random
from random import shuffle
gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
gini2 = list(gini.values())
shuffle(gini2)
print(gini2)

문제368. 위의 gini2를 이용해서 코드를 수행할 때마다 곡이 무작위로 섞여서 출력되게 하시오! (단, 조건은 아티스트 별로 노래가 겹치면 안됩니다. 각 음악의 옆에는 다른 아티스트의 노래가 나와야 합니다.)
import random
from random import shuffle
gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
gini2 = list(gini.values())
shuffle(gini2)
b=[]
c=[]
bond=','
for i in gini2:
    b.append(i[0])
    c.append(i[1])
result = bond.join(b+c)
print(result)
