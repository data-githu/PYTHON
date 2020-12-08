# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:50:42 2020

@author: Owner
"""
■ 84. 문자열이 알파벳인지 검사하기 (isalpha)

문자열은 문자나 숫자, 기호들로 구성이 됩니다. 코드를 작성하다 보면 특정 문자열이 한글이나 알파벳과 같이 사람의 언어를 표현하기 위해 사용되는 문자로만 구성되어 있는지 확인해야하는 경우가 있습니다. 파이썬 문자열 객체가 제공하는 메소드인 isalpha()는 주어진 문자열이 사람의 언어 문자로만 구성되어 있는지 확인해줍니다.
예제 : 
txt1 = 'Warcarftthree'
txt2 = '안녕'
txt3 = '3PO'

print(txt1.isalpha()) #True
print(txt2.isalpha()) #True
print(txt3.isalpha()) #False

문제272. 스티븐 잡스 연설문인 jobs.txt 를 한행 한행씩 출력하시오!
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split('\n')
for i in stev2:
	print(i)
	
설명 : 위의 코드를 실행했을때 cp949 에러가 나면 encoding 에 UTF8 도 써보고 ANSI 도 써보 CP949도 써보세요.

문제273. 위에서 한행씩 출력하고 있는 스크립트를 철자 하나씩 출력하시오!
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split('\n')
for i in stev2:
    for k in i:
        print(k)

문제274. 위에서 출력된 철자가 알파벳이면 cnt를 증가시켜서 스티븐 잡스의 연설문에 알파벳이 몇개가 있는지 출력하시오!
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split('\n')
cnt = 0
for i in stev2:
    for k in i:
        if k.isalpha() == True:
            cnt = cnt + 1
print(cnt)

설명 : 스티븐 잡스 연설문에서 숫자나 공백문자나 마침표와 같은 구두점을 뺀 알파벳 철자만 카운트 했습니다.
데이터 분석 사례 중에 유명한 사례중 하나가 케냐의 은행에서 고객들에게 대출을 해줄때 그 사람의 신용을 확인해서 대출을 해주는데 신용을 확인할 때 SNS의 그사람들에 대한 글을 분석해서 긍정적인 평가가 많은지 부정적인 평가가 많은지를 파악해서 대출심사에 반영을 하니 은행의 대출금 환수가 훨씬 원활해 졌던 사례가 있습니다.



■ 85. 문자열이 숫자인지 검사하기 (isdigit)
문자열 객체의 isdigit() 메소드는 문자열을 구성하는 요소가 모두 숫자인인 체크하고 True 또는 False 로 리턴합니다.

번호     내장함수
1          isalpha()
2          isdigit()
3          isspace()

문제275. 스티븐 잡스 연설문에는 숫자가 몇개가 있는지 출력하시오!
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split('\n')
cnt = 0
for i in stev2:
    for k in i:
        if k.isdigit() == True:
            cnt = cnt + 1
print(cnt)



■ 86. 문자열이 알파벳 또는 숫자인지 검사하기 (isalnum)

알파벳(한글) 과 숫자를 동시에 확인하는 문자열 함수는 isalnum 입니다.
예제 : 
a = 'A story is 2003'
for i in a:
	if i.isalnum() =-True:
		print( i )
		
*케냐 은행의 데이터 분석 사례를 파이썬 코드로 구현해 봅니다.

예제1. 긍정단어 를 파이썬으로 읽어서 한행씩 출력하시오!
positive = open("c:\\data\\positive-words.txt",encoding='UTF8')
pos = positive.read().split('\n')
for i in pos:
    print(i)

예제2. 아래의 pos를 프린트해보세요.
import csv
positive = open("c:\\data\\positive-words.txt",encoding='UTF8')
pos = positive.read().split('\n')
print(pos)

예제3. 아래의 단어가 긍정단어 리스트들 중에 있는지 확인하시오!
if 'wonderful' in ['wonderful', 'wonderfully', 'wonderous', 'wonderously']:
	print('존재합니다.')
else:
	print('존재하지 않습니다.')

예제4. 스티븐 잡스 연설문(jobs.txt)를 읽어서 한 단어씩 출력하시오!
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split()
print(stev2)
for i in stev2:
    print(i)

문제276. 스티븐 잡스 연설문에는 긍정단어가 몇 개 있는지 확인하세요.
positive = open("c:\\data\\positive-words.txt",encoding='UTF8')
pos = positive.read().split('\n')
stev = open("c:\\data\\jobs.txt",encoding='UTF8')
stev2 = stev.read().split()
cnt = 0
for i in stev2:
    if i.lower() in pos:
        cnt = cnt + 1
print(cnt)