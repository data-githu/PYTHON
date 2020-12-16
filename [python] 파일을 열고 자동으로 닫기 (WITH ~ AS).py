# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:33:18 2020

@author: Owner
"""

■ 139. 파일을 열고 자동으로 닫기 (with~as)
with~as 절을 사용하게 되면 f.close()를 명시하지 않아도 되므로 프로그래머가 실수로 f.close()를 작성하지 않아서 발생하는 메모리 부족 오류를 예방할 수 있습니다.

	1. with~as 절을 사용 안했을 때
f=open("c:\\data\\mydata.txt","r")
data = f.readline()
print(data)
f.close()

	2. with ~ as 절을 사용했을 때
with open("c:\\data\\mydata.txt","r") as f:
data = f.readline()
print(data)

설명 : with ~ as 절을 사용하면 자동으로 파일을 close 해줍니다.