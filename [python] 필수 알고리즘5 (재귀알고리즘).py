# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:01:35 2020

@author: Owner
"""

■ 156. 필수 알고리즘 5 (재귀알고리즘)

	1. 재귀함수란?
	반복문 + 스택구조 (후입선출 - 나중에 들어간 것이 먼저 나오는 구조)가 결합된 함수
	2. 재귀함수의 특징은?
	재귀함수는 함수 내에서 다시 자기 자신을 호출한 후 그 함수가 끝날때까지 함수 호출 이후의 명령문을 수행하지 않습니다.
	3. 함수내에서 다른 함수를 호출하는 예제 
	def sum(a,b):
		return (a+b)
	
	def gob(a,b):
		return (a*b)
	
	def sum_gob(a,b):
		k = sum(a,b)
		m = gob(a,b)
		return k+m
		
	print(sum_gob(2,3))

	4. 숫자를 입력하면 1부터 해당 숫자까지의 합을 출력하는 함수를 생성하시오!
	num = int(input('숫자를 입력하세요.'))
	
	def add_func():
	    sum =0
	    for i in range(1, num+1):
	        sum  = sum + i
	    return sum
	
	print(add_func())

	5. 위의 add_func 함수를 재귀함수로 구현하시오!
	def add_func(n):
	    if n == 0:
	        return 0
	    else:
	        return n + add_func(n-1)
	print(add_func(5))
	

문제512. factorial 함수를 만드시오!
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

문제513. 위의 factorial 함수를 재귀를 이용하지 말고 for loop 문으로 구현하시오!
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = i * result
    return result
print(factorial(5))

※ 재귀를 이용하면 2가지 장점?
	1. loop 문을 복잡하게 사용하지 않아도 됩니다.
	2. 코드가 더 간결해집니다.

문제514. 오라클의 power 함수를 파이썬으로 구현하시오!
def power(a,b):
    result = 1
    for i in range(1,b+1):
        result = result*a
    return result

print(power(2,3))

문제515. 위의 power 함수를 재귀함수로 구현하시오!
def power(a,b):
    if b == 0:
        return 1
    else:
        return power(a,b-1)*a

print(power(2,3))

문제516. 구구단 2단을 아래와 같이 출력하는 함수를 생성하시오!
def multi_table_2(num):
    for i in range(1,num+1):
        print( '2 x',i,'=' ,2*i)

multi_table_2(9)

문제517. 두 숫자의 최대공약수를 구하는 함수를 구현하시오!
def gcd (a,b):
    result = []
    for i in range(1,max(a,b)):
        if a % i == 0 and b % i == 0:
            result.append(i)
    return max(result)
print(gcd(16,24))                

#%%
def gcd(n1, n2):
    for i in range(min(n1,n2),0,-1):
        if n1 % i == 0 and n2 % i == 0:
            return i

print(gcd(16,24))

문제518. (필수 알고리즘 5번째) 재귀함수를 이용하여 최대공약수를 구하는 함수를 구현하시오!
def gcd (a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
print(gcd(16,24))

문제519. 구구단 2단을 재귀함수로 출력하시오!
def multi_table_2(num):
    if num == 0:
        return 1
    else:
        print( '2 x',10-num,'=' ,2*(10-num))
        return multi_table_2(num-1)

multi_table_2(9)


