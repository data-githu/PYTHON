# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:21:23 2020

@author: Owner
"""

■ 116. 리스트 요소 무작위로 섞기(shuffle)
파이썬 기본 모듈인 random은 난수를 발생하는 모듈입니다.
이 모듈은 제공하는 shuffle 은 리스트의 요소를 무작위로 섞는데 활용됩니다.

예제 : 
from random import shuffle
a = [1,2,3,4,5,6,7,8,9,10]
shuffle(a)
print(a)