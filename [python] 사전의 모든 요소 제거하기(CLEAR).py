# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:08:23 2020

@author: Owner
"""

■ 123. 사전의 모든 요소 제거하기(clear)
사전의 모든 요소를 제거하여 빈 사전으로 만드는 방법은 clear를 이용하면 됩니다.

예제:
dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}
dict.clear()
print(dict) #{}

문제359. 위와 같이 딕셔너리의 요소를 지우는게 아니라 딕셔너리 자체를 메모리에서 지우려면 어떻게 해야하는가?
dict = {'소녀시대':['다시만난세계','Gee'],'방탄소년단':['DNA','Fire']}
del dict
print(dict) #<class 'dict'>