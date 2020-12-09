# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:57:02 2020

@author: Owner
"""

■ 104. 리스트 합치기(+)
두개의 리스트를 연결하여 새로운 리스트를 만드는 방법은 + 연산자를 이용해 두개의 리스트를 더하면 됩니다.

예제 : 
listdata1 = ['a','b','c','d']
listdata2 = ['f','g','h','i']
listdata3 = listdata1 + listdata2
print(listdata3)

문제312. 아래와 같이 엄마와 아기가 함께하는 수영교실 나이 리스트를 파이선 코드로 작성하시오!
[34,34,34,34,34,34,34,34,34,34,2,2,2,2,2,2,2,2,2,2]

list1 = [34]*10
list2 = [2]*10
print(list1+list2)