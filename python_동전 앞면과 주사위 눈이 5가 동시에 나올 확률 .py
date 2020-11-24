# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:41:58 2020

@author: Owner
"""

import random
dice = [1,2,3,4,5,6]
coin =['앞면','뒷면']
cnt = 0

for i in range(1,100001):
    result1 = random.choice(coin)
    result2 = random.choice(dice)
    if result1 == '앞면' and result2 == 5:
        cnt = cnt +1
print(cnt/100000)