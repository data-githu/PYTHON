# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:59:02 2020

@author: Owner
"""

■ 128. 문자 코드값 구하기(ord)
파이썬 내장함수 ord()는 문자를 컴퓨터가 인식하는 코드값으로 변환합니다.

예제 : A -------------> 65
             encoding : 사람이 알아볼 수 있는 언어를 컴퓨터가 알아볼 수 있는 숫자로 변환
print(ord('A')) # 65

문제375. 알파벳 대문자 출력하시오!
import string
print(string.ascii_uppercase) #ABCDEFGHIJKLMNOPQRSTUVWXYZ

문제376. 위의 코드와 ord() 함수를 이용해서 아래의 결과를 출력하시오!
import string
for i in string.ascii_uppercase:
    print(i,'-------->', ord(i))