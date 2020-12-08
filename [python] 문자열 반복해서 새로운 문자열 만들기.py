# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:47:55 2020

@author: Owner
"""


■ 80. 문자열을 반복해서 새로운 문자열로 만들기(*)
예제 : 
print('★' *10)

문제264. for loop 문을 이용해서 숫자 1-5까지 출력하시오!
1
2
3
4
5

for i in range(1:6):
	print(i)

문제265. 숫자를 물어보게하고 숫자를 입력하면 해당 숫자까지 숫자가 출력되게하세요!
a = int(input('숫자를 입력하세요'))
for i in range(1,a+1):
    print(i)

문제266. 위의 코드를 수정해서 숫자를 물어보게 하고 아래와 같이 ★가 출력되게 하세요.
a = int(input('숫자를 입력하세요'))
for i in range(1,a+1):
    print('★'*i)

문제267. (알고리즘 22번) 아래와 같이 사각형이 출력되게 하세요.
가로의 숫자를 입력하세요~
세로의 숫자를 입력하세요~
a = int(input('가로의 숫자를 입력하세요~'))
b = int(input('세로의 숫자를 입력하세요~'))
for i in range(1,b+1):
    print('★'*a)
