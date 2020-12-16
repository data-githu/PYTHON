# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:32:37 2020

@author: Owner
"""

■ 138. 바이너리 파일 복사하기(read, write)
이미지나 동영상도 파이썬으로 복사 붙여넣기 할 수 있습니다.
이미지나 동영상을 복사 붙여넣기 할 때는 파일의 크기가 크므로 한번에 읽어들일 수 없고 일부분만 일정한 크기로 읽으면서 복사 붙여넣기를 합니다.

예제 : 
bufsize = 1024 #1kb 크기의 버퍼 사이즈를 지정합니다.
f = open("c:\\data\\lena.png","rb") # rb는 read.binary의 약자입니다.
h = open("c:\\data\\lena_copy.png","wb") # wb 는 write binary 의 약자입니다.
data = f.read(bufsize) # 이미지를 1kb 을 읽어서 data 에 저장합니다. 
while data: # data 에 data 가 발견되는 동안에 루프문을 수행합니다. 
	h.write(data) #  lena_copy.png 에 1kb 의 데이터씩 write 합니다. 
	data = f.read(bufsize) # lena.png 에서 1kb 의 데이터를 read 합니다. 
f.close()
h.close()

설명 : lena.png 의 총크기가 334kb 이므로 1kb 읽어들여서 쓰는 총 344번 수행합니다.