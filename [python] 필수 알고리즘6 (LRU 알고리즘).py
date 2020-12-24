# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 13:56:43 2020

@author: Owner
"""



■ 157. 필수 알고리즘6 (LRU 알고리즘)
LRU : Least Recent Used
LRU 알고리즘이란? Oracle DATABASE 의 메모리 관리를 효율적으로 하기 위해 고안된 대표적인 알고리즘으로 최신 데이터를 메모리에 유지시키고 오래 데이터는 ㅗ리에서 내보내게 하는 알고리즘

한번 디스크에서 읽은 데이터를 메모리에 올려놓고 메모리에서 빠르게 데이터를 조회할 수 있도록 LRU 알고리즘을 구현해서 만든 소프트웨어 입니다. 그런데 이 메모리 공간이 한정된 공간이다 보니 무한히 데이터를 올릴 수 없어서 오래된 데이터는 메모리에서 빠져나가게 되고 최신 데이터가 그 빠져나간 자리에 올라가게 됩니다.
최근에 내가 검색한 데이터는 다시 검색할 확률이 높은 데이터이므로 메모리에 오래 두도록 하고 예전에 검색한 데이터는 메모리에서 빠져나가게 합니다.

스택 : 후입선출
큐 : 선입선출

*LRU 알고리즘 문제를 파이썬으로 구현하는 순서
	
1.1 도시이름은 대소문자를 구분하지 않게 만든다.

코딩예제 : 아래의 리스트를 모두 소문자가 출력되게 하시오!
cities = ['Jeju','Pangyo','New york', 'new york']

cities = ['Jeju','Pangyo','New york', 'new york']
city=[]
for i in cities:
    city.append(i.lower())
print(city)

위의 코드를 comprehension을 사용해서 간단하게 수행하시오!
cities = ['Jeju','Pangyo','New york', 'new york']
city=[i.lower() for i in cities]
print(city)

※ 위의 코드는 comprehension 코드로 위의 5줄 코드를 3줄로 간소화한 코드입니다.

문법 : [출력 표현식 for 요소 in 입력시퀀스 if 조건식]
           i.lower()    for   i     in cities

예 : 1부터 20까지의 홀수를 담는 리스트를 만드시오.
a = [ i for i in range(1,21) if i%2 == 1]
print(a)


1.2 메모리(cache)를 만들어야 한다. (입력된 숫자만큼 cache 사이즈 구성)
코딩예제 : None이 4개로 채워진 리스트를 생성하세요.
cache = [ None for i in range(1,5) ]
print(cache)

1.3 메모리(cache)에 데이터를 올린다. 
코딩예제1 : 'jeju'를 올리세요.
cache = [ None for i in range(1,5) ]
cache.append('jeju')
del cache[0]
print(cache)

코딩예제2 : 위의 코드에 이어서 'Pangyo'를 올리세요.
cache = [ None for i in range(1,5) ]
cache.append('jeju')
del cache[0]
print(cache)
cache.append('Pangyo')
del cache[0]
print(cache)

코딩예제3 : 위에서 만든 코드를 가지고 함수를 생성하시오.
cities = ['Jeju','Pangyo','New york', 'new york']
def cache_Process(cities, cachesize):
    city = [i.lower() for i in cities]
    cache = [ None for i in range(1,cachesize+1)]
    for i in range(0,len(city)):
        cache.append(city[i])
        del cache[0]
    return cache

print(cache_Process(cities,4))

코딩예제4 : 위의 함수 결과가 cache의 결과가 아니라 수행시간이 되도록 하시오!
cities = ['Jeju','Pangyo','New york', 'new york']

def cache_Process(cities, cachesize):
    cnt = 0
    city = [i.lower() for i in cities]
    cache = [ None for i in range(1,cachesize+1)]    
    for i in city:
        if i in cache:
            cnt = cnt + 1
        else:
            cnt = cnt + 5
            cache.append(i)
            del cache[0]
    return cnt

print(cache_Process(cities,4))

코딩예제5. check 리스트를 만들어 위의 함수가 올바르게 구현했는지 확인하시오!
def cacheProcess(cities, cachesize):
    cnt = 0
    city = [i.lower() for i in cities]
    cache = [ None for i in range(1,cachesize+1)]    
    for i in city:
        if i in cache:
            cnt = cnt + 1
        else:
            cnt = cnt + 5
            cache.append(i)
            del cache[0]
    return cnt


check = []

a = cacheProcess(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],3)
check.append(a)

a = cacheProcess(["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],3)
check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],2)
check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA","SanFrancisco","Seoul","Rome","Paris","Jeju","NewYork","Rome"],5)
check.append(a)

a = cacheProcess(["Jeju","Pangyo",'NewYork','newyork'],2)
check.append(a)

a = cacheProcess(["Jeju","Pangyo","Seoul","NewYork","LA"],0)
check.append(a)

a = cacheProcess(['Jeju', 'Jeju','Jeju'],3)
check.append(a)

correct = [50,21,60,52,16,25,7]

print(check)

for i in range(len(check)) :
    if check[i] != correct[i] :
        print("%i번째 경우가 틀립니다."%i)




