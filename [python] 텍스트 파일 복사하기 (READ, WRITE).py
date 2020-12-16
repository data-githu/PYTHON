# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:31:08 2020

@author: Owner
"""

■ 137. 텍스트 파일 복사하기 (read, write)
텍스트 파일을 복사하는 방법은 파이썬으로 구현하려면 read와 write 를 이용하면 됩니다. read() 로 텍스트 파일을 읽고 write() 로 쓰고 다른 파일 이름으로 저장하면 됩니다.

예제 : 
f = open('c:\\data\\mydata.txt',"r")
f = open('c:\\data\\mydata_copy.txt',"w")
data = f.read()
h.write(data)
f.close()
h.close()