# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 00:16:44 2021

@author: Owner
"""

■ 158. 필수 알고리즘7 (자카드 유사도 알고리즘)
자카도 유사도는 두 문장을 각각의 집합으로 만든 뒤 두 집합을 통해 유사도를 측정하는 알고리즘 입니다.


설명 : 두 문장의 교집합이 6개, 합집합이 24개이므로 자카드 유사도는 6/24 = 0.25 가 됩니다.

예제1. 다음 A집합과 B집합의 자카드 유사도를 구하시오!
A = {1,2,3}
B = {2,3,4}

A∩B ={2,3}
A∪B = {1,2,3,4}

J(A,B) = 2/4 = 0.5 


예제2. FRANCE, FRENCH 가 주어졌을때 자카도 유사도는?
A = {FR, RA, AN, NC, CE}
B = {FR, RE, EN, NC, CH}

A∩B ={FR,NC}
A∪B = {FR, RA, AN, NC, CE, RE, EN, CH}

J(A,B) = 2/8 = 0.25 



■ 파이썬으로 합집합과 교집합 구현하기
a = {1,2,3,4}
b = {2,4,5}

#1. a와 b의 합집합 구하기
result1 = a.union(b)
print(result1)  # {1, 2, 3, 4, 5}

#2. a와 b의 교집합 구하기
result2 = a.intersection(b)
print(result2) # {2, 4}

#3. a와 b의 자카드 유사도를 구하기
result3 = len(result2)/len(result1)
print(result3) # 0.4

■ 리스트로 합집합과 교집합 구하기
a = [1,2,3,4]
b = [2,4,5]

# 1. a와 b의 합집합 구하기
result1 = set(a+b)
print(result1) # {1, 2, 3, 4, 5}

#2. a와 b의 교집합 구하기
result2 = []
for i in a:
    if i in b:
        result2.append(i)
print(result2) # [2, 4]


■ 자카드 유사도 알고리즘 문제를 파이썬으로 구현하는 방법 순서
	1. 문제를 2번 읽으면서 문제를 정확하게 파악한다.
	질문 : FRANCE, FRENCH 의 두 단어의 자카드 유사도는?
	관련 알고리즘(자카드 유사도)의 정확한 이해가 있어야 합니다.
	
	2. 문제를 해결하기 위해서 순서대로 해결 방법을 기술한다.
	2.1 두 문장을 받아서 두개의 철자로 분리하여 리스트에 저장한다. 
		문자로 된 글자 쌍만 유효하다.  ( 함수이름 str_split 로 생성한다)
		예 : FRANCE, FRENCH 를 받아서 아래의 리스트를 만듭니다.
		a = [FR, RA, AN, NC, CE]
		b = [FR, RE, EN, NC, CH]
		
		str1 = input('문자열을 입력하세요~').upper()
		str2 = input('문자열을 입력하세요~').upper()
		
		def str_split(string):
		    res = []
		    for i in range(len(string)-1):
		        if string[i].isalpha() and string[i+1].isalpha():
		            res.append(string[i:i+2])
		    return res
		
		print(str_split(str1))
		print(str_split(str2))
	
	2.2  a와 b의 교집합을 구한다.
		a = ['FR', 'RA', 'AN', 'NC', 'CE']
		b = ['FR', 'RE', 'EN', 'NC', 'CH']
		
		intersection = []
		for i in a:
		    if i in b:
		        intersection.append(i)
		
		print(intersection) # ['FR', 'NC']
		
	2.3  a와 b의 합집합을 구한다.
		a = ['FR', 'RA', 'AN', 'NC', 'CE']
		b = ['FR', 'RE', 'EN', 'NC', 'CH']
		
		union = set(a+b)
		print(union)
	
	2.4  a와 b의 자카드 유사도를 구한다. (결과에 65536을 곱해서 출력)
		a = ['FR', 'RA', 'AN', 'NC', 'CE']
		b = ['FR', 'RE', 'EN', 'NC', 'CH']
		
		import  math 
		
		len_i = len(intersection)
		len_u = len(union) 
		print (  math.trunc( len_i / len_u *  65536) )  

문제521. 지금까지의 코드를 함수로 만들어서 아래와 같이 실행되게하시오

print( Jaccard()  )

문자열을 입력해주세요. : FRANCE
문자열을 입력해주세요. : french

16384

import  math 

def  str_split(string):           
    res =[]
    for  i  in  range( len(string) -1 ):
        if  string[i].isalpha()  and  string[i+1].isalpha():   
            res.append( string[ i : i+2] )
    return res

def Jaccard():

    str1 = input('문자열을 입력하세요 ~').upper()
    str2 = input('문자열을 입력하세요 ~').upper() 
    
    a = str_split(str1)
    b = str_split(str2)
    
    intersection = [] 
    for  i  in  a:
        if  i  in  b:
            intersection.append(i)
    
    union = set( a + b )
    
    len_i = len(intersection)
    len_u = len(union) 
    return (  math.trunc( len_i / len_u *  65536) )  


print( Jaccard()  )
	2.5  a와 b가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 J(A,B) = 1로 정의한다.
	3. 순서대로 정한 해결방법을 파이썬 코드로 구현합니다.        

문제522. 지금까지 만든 Jaccard 함수에 아래의 내용을 코드 추가하시오! (a와 b가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 J(A,B) = 1로 정의한다.)

print( Jaccard()  )

문자열을 입력해주세요. : E=M*C^2
문자열을 입력해주세요. : e=m*c^2         

65536


import  math 

def  str_split(string):           
    res =[]
    for  i  in  range( len(string) -1 ):
        if  string[i].isalpha()  and  string[i+1].isalpha():   
            res.append( string[ i : i+2] )
    return res

def Jaccard():
    str1 = input('문자열을 입력하세요 ~').upper()
    str2 = input('문자열을 입력하세요 ~').upper() 
    
    a = str_split(str1)
    b = str_split(str2)
    
    intersection = [] 
    for  i  in  a:
        if  i  in  b:
            intersection.append(i)
    
    union = set( a + b )
    
    len_i = len(intersection)
    len_u = len(union) 
    
    if len(a)==0 and len(b)==0:
        return 1 *65536

    else:
        return math.trunc( len_i / len_u *  65536)

print( Jaccard()  )


문제523.  set 을 이용하지 말고 아래의 A 와 B 두개의 리스트의 합집합  { 1, 1, 1, 2, 2 ,3, 4, 5 } 로 출력되게하시오 !
A = [1, 1, 1, 2, 2, 3]
B = [1, 1, 2, 2, 4, 5]

intersection=[]
for  i  in  A:
    if  i  in  B:
        intersection.append(i)
print(intersection)   # 교집합을 구한다.  [1, 1, 1, 2, 2]

s = A + B  
print(s)  # [1, 1, 1, 2, 2, 3, 1, 1, 2, 2, 4, 5]
diff = []
for  i  in  s:
    if  i  not  in  intersection: 
        diff.append(i)
print(diff)  # [3, 4, 5]

union = diff + intersection
print(union)

# 교집합을 제대로 나오게 하려면 ~~ (준환이 제공)

A = [1, 1, 1, 2, 2, 3]
B = [1, 1, 2, 2, 4, 5]
intersection=[]
for  i  in  A:
    if  i  in B:
        B.remove(i)
        intersection.append(i)
        
print(intersection) 


위의 코드는 합집합은 맞지만 교집합이 이상하므로 한결이가 구현한 collections 으로 구현하면 다음과 같습니다. 맞는지 확인하세요 ~

import collections
a = [1,1,1,2,2,3]
b = [1,1,2,2,4,5]
                 
intersection = []
result = collections.Counter(a) & collections.Counter(b) # 교집합
intersection = list(result.elements()) # 요소만 리스트로 빼내오기

result2 = collections.Counter(a) | collections.Counter(b) # 합집합
union = list(result2.elements())       # 요소만 리스트로 빼내오기 
print(intersection)  # [1, 1, 2, 2]
print(union)  # [1, 1, 1, 2, 2, 3, 4, 5]

문제524. collections 를 이용해서  자카드 유사도를 구현하세요.                            
문자열을 입력하세요 ~handshake   
문자열을 입력하세요 ~shake hands    

65536
                                              
문자열을 입력하세요 ~FRANCE     
문자열을 입력하세요 ~french        
                                       
16384                                          

import math
import collections    # intersection 용
def str_split(string):
    string = string.upper()
    res = []
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha(): # 문자라면,
            res.append(string[i:i+2])
    return res
def Jaccard(str1,str2):
    
    # intersection 수정했습니다.
 
    intersection = []
    result = collections.Counter(str_split(str1)) & collections.Counter(str_split(str2))
    intersection = list(result.elements())       # 교집합 &
 
    # union 합집합 수정했습니다.
    result2 = collections.Counter(str_split(str1)) | collections.Counter(str_split(str2))
    union = list(result2.elements())             # 합집합 |
 
    if len(union) != 0:
        return math.trunc(len(intersection)/len(union) * 65536)
    else:
        return 65536
 
 
print(Jaccard('FRANCE','french'))
print(Jaccard('handshake','shake hands'))
print(Jaccard('aa1+aa2','AAAA12'))
print(Jaccard('E=M*C^2','e=m*c^2'))

