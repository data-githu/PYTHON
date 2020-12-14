# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:22:29 2020

@author: Owner
"""

■ 126. 사전 요소를 모두 추출하기(items)
딕셔너리 자료형에서 데이터를 추출하는 방법은 다음과 같습니다.

	1. key만 추출 : dict.keys()
	2. 값만 추출 : dict.values()
	3. 둘 다 추출 : dict.items()

예제 : 
gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
print(gini.keys())
print(gini.values())
print(gini.items())

문제369. 위의 gini 딕셔너리의 요소들의 items 를 뽑아서 리스트에 담으시오!
gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
result = list(gini.items())
print(result)

문제370. 위의 result 에서 음악 첫번재 곡들만 출력하시오!
gini = { '비틀즈' : ['yesterday','imagine'], '아이유' : ['너랑나','마시멜로우'], '마이클잭슨' : ['beat it','smooth criminal'] }
result = list(gini.items())
for i in result:
    print(i[1][0])

