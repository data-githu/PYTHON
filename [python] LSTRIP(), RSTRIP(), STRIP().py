# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:53:55 2020

@author: Owner
"""

■ 88. 문자열에서 좌우 공백 제거하기 (lstrip, rstrip, strip)
함수        설명
lstrip       문자열에서 존재하는 왼쪽 공백을 제거
rstrip       문자열에서 존재하는 오른쪽 공백을 제거
strip        문자열에서 존재하는 양쪽 공백을 제거

예제: 
txt7 = '            양쪽에 공백이 있는 문자열 입니다.                        '
print(txt7.lstrip())
print(txt7.rstrip())
print(txt7.strip())

문제279. 스티븐 잡스 연설문에서 정관사 the 가 몇번 나오는가?
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split()
cnt = 0
for i in stev2:
    if i.lower().strip() == 'the': #양쪽에 공백이 있을지 모르므로 확실하게 해주는 코드
        cnt = cnt + 1
print(cnt)
