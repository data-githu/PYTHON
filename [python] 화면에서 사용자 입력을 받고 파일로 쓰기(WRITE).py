# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:43:22 2020

@author: Owner
"""

■ 135. 화면에서 사용자 입력을 받고 파일로 쓰기(write)
사용자로 부터 입력받은 텍스트를 파일로 저장하려면 파일을 텍스트 쓰기 모드로 오픈하고 파일 객체의 write() 를 이용해 데이터를 파일에 기록합니다.

예제 : 
text = input('파일에 저장할 내용을 입력하세요~')
f = open('c:\\data\\mydata.txt', 'w')
f.write(text)
f.close()

설명 : 위에 w는 write 의 약자입니다. c 드라이브 밑에 data 밑에 mydata.txt 파일로 쓰겠다는 뜻입니다.

설명 : 위의 코드는 웹에서 스크롤링한 데이터를 파일로 저장할 때 응용되게 됩니다.