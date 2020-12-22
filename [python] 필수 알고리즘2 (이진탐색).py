# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:52:40 2020

@author: Owner
"""

■ 153. 필수 알고리즘2 (이진탐색)

문제494. 아래의 리스트에서 숫자 3이 있는지 순차 탐색으로 구현하시오! 있으면 숫자 3이 있습니다. 라는 메시지가 출력되게 하세요!
a = [15,11,1,3,8]
for i in a:
    if i == 3:
        print('숫자 3이 있습니다.')
        break
    else:
        print('숫자 3이 없습니다.')

문제495. 위의 코드를 수정해서 숫자를 물어보게 하고 숫자를 입력하면 해당 숫자가 있는지 없는지 확인하시오!
a = [15, 11, 1, 3, 8]
num = int(input('숫자를 입력하세요~'))
for i in a:
    if i == num:
        print('숫자',num, '가 있습니다.')
        break
    else:
        print('숫자',num, '가 없습니다.')

문제496. 아래의 a리스트에서 중앙값을 찾으시오
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]

import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n = np.array(a)
print(np.median(a_n))

문제497. a 리스트에서 첫번째 숫자부터 중앙값에 해당하는 숫자까지만 검색하시오!
import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n = np.array(a)
a_m = np.median(a_n)
print(a[0:a.index(a_m)+1])

문제498. 위의 a 리스트에서 문제 497번에서 선택된 숫자들을 중앙값까지 포함해서 다 지우고 아래의 결과만 출력되게 하시오!
[51, 64, 67, 77, 139, 672, 871]

import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n = np.array(a)
a_m = np.median(a_n)
del(a[0:a.index(a_m)+1])
print(a)

문제499. 위의 결과로 출력된 아래의 리스트에서 중앙값을 출력하시오!
import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n = np.array(a)
a_m = np.median(a_n)
del(a[0:a.index(a_m)+1])
a_m2 = np.median(a)
print(a_m2)

문제500. 위에서 출력된 중앙값이 내가 검색하고자 하는 숫자 67 보다 크다면 아래의 결과 리스트만 출력되게 하시오!
import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
a_n = np.array(a)
a_m = np.median(a_n)
del(a[0:a.index(a_m)+1])
a_m2 = np.median(a)
if a_m2 > 67:
    del(a[a.index(a_m2):])
else:
    del(a[0:a.index(a_m2)])
print(a)

문제501. ebs에 나온 영상대로 이진탐색을 구현하시오!
import numpy as np
a = [1,7,11,12,14,23,33,47,51,64,67,77,139,672,871]
num = int(input('a 리스트에서 검색할 숫자를 입력하세요.'))
a_n = np.array(a)
a_m = np.median(a_n)
cnt = 0
if num not in a:
    print(num,'은 a 리스트에 없습니다.')
else:
    for i in range(1,100):
        if a_m > num:
            del(a[int(len(a)/2): ])
            cnt = cnt + 1
            a_n = np.array(a)
            a_m = np.median(a_n)
            print(a)

        elif a_m < num:
            del(a[0 : int(len(a)/2)])
            cnt = cnt + 1
            a_n = np.array(a)
            a_m = np.median(a_n)
            print(a)
            
        else:
            break
    print(num,'은 ', cnt, '번 만에 검색되었습니다.' )
