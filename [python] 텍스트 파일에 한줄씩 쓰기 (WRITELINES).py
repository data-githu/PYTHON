# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:29:57 2020

@author: Owner
"""

■ 136. 텍스트 파일에 한줄씩 쓰기 (writelines)
파일 객체의 writelines() 는 텍스트 문자열이나 텍스트 문자열이 요소로 되어있는 리스트를 인자로 받아 파일에 한 줄씩 기록합니다.
리스트가 인자인 경우 writelines() 는 리스트의 요소를 하나의 문자열로 결합하여 파일을 한번에 기록합니다.
※ writelines는 리스트 자료형도 파일에 저장할 수 있습니다.

writeline 예제 : 
data= [] #data라는 비어있는 리스트 생성
while True: #무한루프를 수행합니다.
	text = input('저장할 내용을 입력하세요.')
	if text == '': #text 에 아무것도 입력하지 않으면
		break #break 문을 실행해서 수행
	data.append(text + '\n')
f = open('c:\\data\\mydata99.txt','w')
f.writelines(data)
f.close()

설명 : open() 의 옵션중 w는 그냥 쓰기이고, a는 추가 입니다.
