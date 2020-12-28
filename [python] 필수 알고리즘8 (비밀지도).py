# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:29:01 2020

@author: Owner
"""
■ 159. 필수 알고리즘8 (비밀지도)
*알고리즘 문제 풀때 해결하는 순서

	1. 문제를 2번 정독하면서 질문을 정확하게 이해하고 출력이 무엇이 되어야 하는지 정확하게 이해해야 합니다.
	n = 5
	arr1 = [9,20,28,18,11]
	arr2 = [30,1,21,17,28]
	secretmap(arr1,arr2,n)
	
	["#####","# # #", "### #", "# ##", "#####"]
	
	
	2. 풀이를 번호 순서대로 한글로 적는다. (메모)
	2.1 십진수를 이진수 변환한다. 
	2.2 두개의 이진수를 가지고 #과 공백을 나타낸다.
	
	3. 한글 ----> 파이썬으로 번역하시오.
	
문제525. 숫자 9를 이진수로 변환하시오!
결과 : 0b1001
print(bin(9))


문제526. 위의 결과에서 0b는 안나오고 1001만 출력되게하시오
결과 : 1001
print(bin(9)[2:])

문자527 .숫자 30 의 이진수를 아래와 같이 출력하시오!
결과 : 11110
print(bin(30)[2:])

문제528. 위와 같이 출력되는 change 함수를 생성하시오!
def change(num):
    return bin(num)[2:]

print(change(30))

문제529. 위에서 만든 change 함수에서 숫자 9를 넣고 출력해보시오!
def change(num):
    return bin(num)[2:]

print(change(9)) #1001

문제530. change 함수를 실행할때 아래와 같이 입력매개변수를 하나 더 만들어서 입력매개변수의 길이만큼 숫자 0이 채워져서 출력되게 하시오!
def change(num1, num2):
    return bin(num1)[2:].rjust(num2,'0')

print(change(9,5))

설명 : rjust(5,'0')은 출력되는 자리수를 전체 5자리로 잡고 나머지 왼쪽에 '0' 을 채워넣어라

문제531. 카카오 문제의 예제를 가지고 아래의 결과를 출력하시오!
01001 11110
10100 00001
11100 10101
10010 10001
01011 11100

def change(num1, num2):
    return bin(num1)[2:].rjust(num2,'0')

n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]


for i in range(len(arr1)):
    print(change(arr1[i],n),change(arr2[i],n))


문제532. 위에서 출력된 아래의 결과를 이용해서 두 지도의 숫자가 둘다 0이면 공백(" ")을 출력하고 아니면 벽('#')을 출력하시오!
def change(num1, num2):
    return bin(num1)[2:].rjust(num2,'0')

n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
result = []

for i in range(len(arr1)):
    a1 = change(arr1[i],n)
    a2 = change(arr2[i],n)
    f = ' '
    for k in range(n):
        if a1[k] == '0' and a2[k] == '0':
           fi = ' '
           f = f + fi
        else:
            fi = '#'
            f = f + fi
    result.append(f)
print(result)

문제533 위의 코드를 함수로 생성해서 아래와 같이 수행하시오!
 [' ######', ' ###  #', ' ##  ##', '  #### ', '  #####', ' ### # ']

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def change(arr1, n):
    return bin(arr1)[2:].rjust(n,'0')

def secretmap(arr1, arr2, n):
    result = []
    
    for i in range(0,len(arr1)):
        a1 = change(arr1[i],n)
        a2 = change(arr2[i],n)
        f = ' '
        for k in range(n):
            if a1[k] == '0' and a2[k] == '0':
               fi = ' '
               f = f + fi
            else:
                fi = '#'
                f = f + fi
        result.append(f)
    print(result)

secretmap(arr1, arr2, n) 