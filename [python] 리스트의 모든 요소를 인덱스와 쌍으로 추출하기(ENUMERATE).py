# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:58:59 2020

@author: Owner
"""

■ 117. 리스트의 모든 요소를 인덱스와 쌍으로 추출하기 (enumerate)

파이썬 내장함수 enumerate()는 시퀀스 자료형을 인자로 받아 각 요소를 인덱스와 함께 쌍으로 추출할 수 있는 반복가능한 자료인 enumerate 객체를 리턴합니다. 
enumerate 객체는 주로 for 문과 함께 자주 사용되고 list() 를 이용해서 리스트 객체를 변환할 수 있습니다.

예제 : 
emp12 = ['김*원', '김*승', '김*비', '권*원']
result = list(enumerate(emp12))
print(result)
#[(0, '김*원'), (1, '김*승'), (2, '김*비'), (3, '권*원')]

예제2:
emp12 = ['김*원', '김*승', '김*비', '권*원']
for i, k in enumerate(emp12):
	print(i,k)
	
#0 김*원
#1 김*승
#2 김*비
#3 권*원


문제342. 아래의 music 리스트에서 음악요소를 하나씩 추출하는데 앞에 인덱스 번호도 같이 출력되게 하시오!
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
for i, k in enumerate(music):
    print(i,k)

문제343. artist 리스트를 가지고 아래와 같이 결과를 출력하시오!
비틀즈 0
비틀즈 1
아이유 2
아이유 3
마이클잭슨 4
마이클잭슨 5

artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
for i, k in enumerate(artist):
    print(k,i)

문제344. 아래의 두개의 리스트를 가지고 아래와 같이 결과를 출력하시오!
비틀즈 yesterday
비틀즈 imagine
아이유 너랑나
아이유 마시멜로우
마이클잭슨 beat it
마이클잭슨 smooth criminal

music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
for i, k in enumerate(artist):
    print(k,music[i])


최종
{ '비틀즈' : ['yesterday',imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }

설명 : 위와 같이 딕셔너리를 구성하려면 그냥 딕셔너리인 중괄호 하나로 { } 비어있는 딕셔너리를 만들면 안되고 defaultdict 를 이용해야 합니다. defaultdict는 collections 패키지에 있어서 아래와 같이 임폴트 해야합니다.

from collections import defaultdict
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
print(gini)
gini['비틀즈'].append('imagine')
print(gini)

문제345. 그럼 위에서 만든 default 딕셔너리에 아이유를 키로 하고 너랑나, 마시멜로우를 값으로 하여 추가하시오!
from collections import defaultdict
gini = defaultdict(list)
gini['비틀즈'].append('yesterday')
gini['비틀즈'].append('imagine')
gini['아이유'].append('너랑나')
gini['아이유'].append('마시멜로우')
print(gini)

문제346. 위와 같이 일일이 손으로 넣지 말고 enumerate 이용해서 gini 딕셔너리를 구현하시오!
from collections import defaultdict
gini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
for i, k in enumerate(artist):
    gini[k].append(music[i])
print(gini)

문제347. 위의 gini 딕셔너리에서 음악만 추출하시오! (딕셔너리의 값만 추출)
딕셔너리에서 키값을 추출할 때는 : 딕셔너리이름.keys()
딕셔너리에서 값만 추출할 때는 : 딕셔너리이름.values()

from collections import defaultdict
gini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
for i, k in enumerate(artist):
    gini[k].append(music[i])
for i in gini.values():
    for k in i:
        print(k)

문제348. 위의 코드 음악들을 비어있는 리스트인 a에 담으시오!
from collections import defaultdict
gini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
a=[]
for i, k in enumerate(artist):
    gini[k].append(music[i])
for i in gini.values():
    for k in i:
        a.append(k)
print(a)

문제349. 아래의 코드를 수행해서 gini.values() 의 요소들을 프린트 해보시오!
from collections import defaultdict
gini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
a=[]
for i, k in enumerate(artist):
    gini[k].append(music[i])
for j in gini.values():
        print(j)

문제350. 아래와 같이 결과를 출력하시오!
yesterday,너랑나,beat it,imagine,마시멜로우,smooth criminal

from collections import defaultdictgini = defaultdict(list)
music = ['yesterday','imagine','너랑나','마시멜로우','beat it','smooth criminal']
artist = ['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
b=[]
c=[]
bond=','
for i, k in enumerate(artist):
    gini[k].append(music[i])
for j in gini.values():
        b.append(j[0])
        c.append(j[1])
result = bond.join(b+c)
print(result)