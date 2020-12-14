# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:23:06 2020

@author: Owner
"""

■ 119. 리스트 요소가 모두 참인지 확인하기 (all, any)
리스트의 모든 요소가 참인지 또는 모든 요소가 거짓인지 판단해야하는 경우 파이썬의 내장함수 all() 이나 any()를 사용하면 됩니다.
all()은 인자로 입력되는 리스트의 모든 요소가 참인 경우에만 True 를 리턴하고 거짓이 하나라도 포함되어져 있으면 False 를 리턴합니다.
any()는 인자로 입력되는 리스트의 모든 요소가 거짓인 경우에만 False 를 리턴하고 참이 하나라도 존재하면 True를 리턴합니다.

예 : 
listdata1 = [True, True, True]
listdata2 = [True, False, True]

print(all(listdata1)) #True
print(all(listdata2)) #False

print(any(listdata1)) #True
print(any(listdata2)) #True

예제1:
listdata1 = [1,1,1]
listdata2 = [1,0,1]

print(all(listdata1)) #True
print(all(listdata2)) #False

print(any(listdata1)) #True
print(any(listdata2)) #True

설명 : True는 숫자로는 1이고 False는 숫자로는 0 입니다.

문제353. whlie loop문을 이용해서 무한 루프문을 수행하시오!
while True:
	print('aaaaaaaaaaaaa')
	
	
문제354. 이번에는 위의 True 대신에 숫자 1을 넣고 무한 루프문을 수행하시오!
while 1:
print('aaaaaaaaaaaaa')