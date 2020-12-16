# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:58:37 2020

@author: Owner
"""

■133. 텍스트 파일을 읽고 출력하기(read)

텍스트 파일을 읽고 그 내용을 화면에 출력하고자 하면 제일 먼저 텍스트 읽기 모드로 파일을 엽니다.
텍스트 파일을 오픈하면 텍스트 파일을 읽어 내용을 화면에 출력하면 됩니다.

예 : 
f = open('c:\\data\\jobs.txt', encoding = 'UTF8')
data = f.read()
print(data)
f.close()

설명 : 스티븐 잡스 연설문은 길지 않으니 한번에 읽어와도 관계 없습니다. 텍스트 파일의 용량이 매우 클 경우 read() 로 한꺼번에 파일의 내용을 읽어들이는 것은 메모리 문제를 야기시킬 수 있습니다.

웹에서 스크롤링한 데이터를 분석하고자 할 때 위와 같이 open 함수를 이용해서 파이썬으로 데이터를 불러옵니다.

문제399. 중앙일보에서 인공지능으로 검색한 기사인 mydata3.txt 를 파이썬으로 불러서 출력하시오!
f = open('c:\\data\\mydata3.txt', encoding = 'UTF8')
data = f.read() #파일을 한번에 전부 읽어오는 함수입니다.
print(data)
f.close() #파일을 닫는다. 닫는 코드를 안쓰면 스파이더를 실행하고 있으면 계속 파일이 열려있게 됩니다. 파일을 계속 열면 메모리를 계속 차지하고 사용하고 있게 됩니다.

문제400. 위의 중앙일보 기사에서 빅데이터라는 단어가 몇번 나오는지 count 하시오!
f = open('c:\\data\\mydata3.txt', encoding = 'UTF8')
data = f.read()
print(data.count('빅데이터')) #11
f.close()