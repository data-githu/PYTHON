# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:58:58 2020

@author: Owner
"""


■ 134. 텍스트 파일을 한줄씩 읽고 출력하기 ① readline
텍스트 파일의 용량이 매우 클 경우 read() 로 한꺼번에 파일의 내용을 읽어들이는 것은 메모리 문제를 야기할 수 있습니다. 이 경우 텍스트 파일 내용을 한 줄 단위로 읽고 작업을 수행하면 됩니다. readline()은 텍스트 파일에서 한 줄을 읽습니다.
한 줄을 읽고 나면 파일을 읽기 시작하는 위치는 그 다음줄의 맨 처음이 됩니다.

예제 : 
f = open('c:\\data\\jobs.txt', encoding = 'UTF8')
data = f.readline()
print(data)
f.close()

설명 : read() 함수는 텍스트 파일 전체를 읽어오는 반면 readline() 은 텍스트 파일에서 한줄만 읽어옵니다.

문제401. 위의 스티븐 잡스 연설문 데이터를 모두 읽어 오시오! (readline() 함수를 이용하세요!)
f = open('c:\\data\\jobs.txt', encoding = 'UTF8')
data = f.readline()
while data:
	print(data)
	data = f.readline()
f.close()

설명 : 맨 위에 data = f.readline() 코드는 처음에 딱 한번만 실행되고 그 다음에는 실행되지 않습니다. 그 다음부터는 while 문 안에 있는 data = f.readline() 가 작동되어서 반복적으로 스티븐 잡스의 연설문을 한줄씩 읽어서 data 수에 넣습니다.

문제402. mydata3 데이터를 한줄씩 읽은 데이터에서 인공지능이라는 단어가 나오면 count 하게 하시오!
f = open('c:\\data\\mydata3.txt', encoding = 'UTF8')
data = f.readline()
while data:
	print(data.count('인공지능'))
	data = f.readline()
f.close()


문제403. 위의 count한 건수를 다 누적시켜서 출력하시오!
f = open('c:\\data\\mydata3.txt', encoding = 'UTF8')
data = f.readline()
cnt = 0
while data:
    cnt = cnt + data.count('인공지능')
    data = f.readline()
print(cnt)
f.close()

문제404. 위의 코드를 수정해서 단어를 물어보게 하고 단어를 입력하면 해당 단어가 몇 번 나오는지 출력되게 하시오!
f = open('c:\\data\\mydata3.txt', encoding = 'UTF8')
data = f.readline()
char = input('단어를 입력하세요~')
cnt = 0
while data:
    cnt = cnt + data.count(char)
    data = f.readline()
print('이 기사에서', char, '단어는', cnt, '번 나왔습니다.')
f.close()
