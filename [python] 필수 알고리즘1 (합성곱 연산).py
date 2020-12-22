# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:52:00 2020

@author: Owner
"""

■ 152. 필수 알고리즘1 (합성곱 연산)

프로그래머스 사이트에 여러 알고리즘 문제들이 올라와 있습니다.
하루에 하나씩 꾸준히 풀면서 실력을 천천히 쌓아 올리면 됩니다.

*합성곱 연산 알고리즘?
딥러닝의 필수 알고리즘(퍼셉트론, 합성곱 연산 알고리즘)
이미지의 형상을 무시하지 않고 이미지를 그대로 인공 신경망이 학습할 수 있게 해준 수학 행렬 연산입니다.
합성곱에서 원본 이미지는 학습해야할 데이터(사진)이고 필터(filter)는 원본이미지에서 특징을 잡아내는데 사용되는 행렬입니다.
특징을 잡아서 feature map을 생성하여 원본 이미지의 형태를 이해하는 것을 합성곱 연산이라고 합니다.

문제481. 아래의 두 행렬을 만들고 덧셈 연산을 하시오!
a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

import numpy as np
a2 = np.array(a)
b2 = np.array(b)

print( a2+b2 )

문제482. 두 행렬의 원소의 곱을 구하시오!
a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

import numpy as np
a2 = np.array(a)
b2 = np.array(b)

print( a2*b2 )

문제483. 위에서 원소들의 곱으로 출력된 결과인 3X3 행렬의 요소들을 모두 다 더하시오!
a = [[1,2,3],[0,1,2],[3,0,1]]
b = [[2,0,1],[0,1,2],[1,0,2]]

import numpy as np
a2 = np.array(a)
b2 = np.array(b)

result = a2*b2
print(np.sum(result)) #행렬안의 원소들의 합을 출력합니다.

설명 : numpy란?
python 언어에서 기본적으로 지원하지 않는 배열(array) 혹은 행렬(matrix) 의 계산을 쉽게해주는 라이브러리 입니다. 머신러닝에서 많이 사용하는 선형대수학에 관련된 수식들을 python 에서 쉽게 프로그래밍 할 수 있게 해줍니다.

문제484. 아래의 4X4 행렬을 만드시오!
import numpy as np
a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2 = np.array(a)
print(a2)

문제485. 아래의 4x4 행렬에서 행을 0-3, 열을 0-3 까지만 출력하시오!
import numpy as np
a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2 = np.array(a)
print(a2[0:3,0:3])

문제486. a의 4x4 행렬에서 지정한 영역의 숫자들만 출력하시오!
[[2 3 0]
 [1 2 3]
 [0 1 2]]

import numpy as np
a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2 = np.array(a)
print(a2[0:3,1:4])

문제487. a의 4x4 행렬에서 지정한 영역의 숫자들만 출력하시오!
[[0 1 2]
 [3 0 1]
 [2 3 0]]

import numpy as np
a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2 = np.array(a)
print(a2[1:4,0:3])

문제488. a의 4x4 행렬에서 지정한 영역의 숫자들만 출력하시오!
[[1 2 3]
 [0 1 2]
 [3 0 1]]

import numpy as np
a = [[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2 = np.array(a)
print(a2[1:4,1:4])

문제489. 위의 4개의 영역의 숫자들을 for loop 문을 이용해서 모두 출력하시오!
import numpy as np
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
for i in range(2):
    for j in range(2):
        print(a2[i:i+3,j:j+3])

문제490. 위에서 선택한 4개의 행렬(3x3) 과 아래의 filter 행렬(3x3) 과의 원소의 곱을 출력하시오!
import numpy as np
f=[[2,3,4],[1,2,3],[2,0,1]]
filter = np.array(f)
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
for i in range(2):
    for j in range(2):
        print(a2[i:i+3,j:j+3]*filter)

문제491. 위에서 출력된 3x3 행렬 4개에 대한 원소들의 합이 각각 출력되게 하시오.
import numpy as np
f=[[2,3,4],[1,2,3],[2,0,1]]
filter = np.array(f)
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
for i in range(2):
    for j in range(2):
        print(np.sum(a2[i:i+3,j:j+3]*filter))


문제492. 위에서 출력된 4개의 숫자로 2x2 행렬을 만드시오!
import numpy as np
f=[[2,3,4],[1,2,3],[2,0,1]]
filter = np.array(f)
a=[[1,2,3,0],[0,1,2,3],[3,0,1,2],[2,3,0,1]]
a2=np.array(a)
result = []
for i in range(2):
    for j in range(2):
        result.append(np.sum(a2[i:i+3,j:j+3]*filter))

result2 = np.array(result).reshape(2,2)
print(result2)

설명 : a2라는 원본이미지(개사진)에 filter(랜덤으로 생성한 이미지) 를 가지고 원본이미지를 스트라이드 (양옆위아래로 스캔) 하면서 특징을 잡아내어 특징 이미지를 추출(result2) 하는 것을 합성곱이라고 합니다.

문제493. 아래의 원본 이미지 행렬 (5x5) 행렬에서 필터행렬(4x4)로 스트라이딩해서 합성곱해서 특징(3x3) 을 추출하시오!
import numpy as np
f=[[3,1,4,1],[2,3,3,4],[5,1,2,1],[6,1,3,4]]
filter=np.array(f)
result=[]
a=[[2,3,1,4,7],[3,1,6,4,3],[2,1,5,3,1],[6,2,4,1,2],[7,3,1,2,3]]
a2=np.array(a)
for i in range(0,2):
    for j in range(0,2):
        result.append(np.sum(a2[i:i+4,j:j+4]*filter))
result2=np.array(result).reshape(2,2)
print(result2)
