# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:10:48 2020

@author: Owner
"""

■ 154. 필수 알고리즘3 (버블정렬)
인접한 두수를 비교해서 큰 수를 뒤로 보내는 정렬 방법

문제502. 아래의 리스트를 만들고 첫번째 요소와 두번째 요소의 순서를 변경하시오!
a = [10, 5, 20, 9, 8]

a = [10, 5, 20, 9, 8]
temp = a[1]
a[1] = a[0]
a[0] = temp
print(a)

문제503. 아래의 a 리스트의 첫번째 요소와 두번재 요소의 크기를 비교해서 첫번째 요소의 숫자가 두번째 요소의 숫자보다 크다면 두개를 바꿔치기하시오.
a = [5, 4, 20, 9, 8]
if a[0] > a[1]:
    temp = a[1]
    a[1] = a[0]
    a[0] = temp
    print(a)
else:
    print(a)

문제504. 문제503번 코드에 for loop 문을 넣어서 버블 정렬하시오!
a = [5, 4, 3, 2, 1, 8, 7, 10]
for i in range(0, 5):
    if a[i] > a[i+1]:
        temp = a[i+1]
        a[i+1] = a[i]
        a[i] = temp
        print(a)
    else:
        print(a)

문제505. (필수알고리즘3) 위의 코드를 이용해서 버블정렬을 하는 함수를 생성하시오.
a = [5, 4, 3, 2, 1, 8, 7, 10]
def bubble_sort(a):

    for k in range(len(a)):
        cnt =0
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i+1]
                a[i+1] = a[i]
                a[i] = temp
                cnt = 1
        if cnt == 0:
            break
    return a
print(bubble_sort(a))