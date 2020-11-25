# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:29:11 2020

@author: Owner
"""

■ 데이터 분석가 및 딥러닝 개발자가 되기 위해서 갖추어야 할 기술
	1. SQL
	2. 파이썬

문제23. for loop 문을 이용해서 구구단 2단을 출력하시오!
for i in range(1,10):
     print('2 X', i, '=' ,2*i)

설명 : for loop문은 특정 문장을 반복해서 수행하고 싶을 때 사용하는 파이썬 문법
	위의 문법은 1-9까지 9번 반복하겠다.

문제24. 구구단 전체를 출력하시오!
for i in range(1,10):
     print('2 X', i, '=' ,2*i)
for i in range(1,10):
     print('3 X', i, '=' ,3*i)
for i in range(1,10):
     print('4 X', i, '=' ,4*i)
for i in range(1,10):
     print('5 X', i, '=' ,5*i)
for i in range(1,10):
     print('6 X', i, '=' ,6*i)
for i in range(1,10):
     print('7 X', i, '=' ,7*i)
for i in range(1,10):
     print('8 X', i, '=' ,8*i)
for i in range(1,10):
     print('9 X', i, '=' ,9*i)

■ 중첩 for loop 문
loop 문을 중첩시켜서 수행한다.
loop 문 자체를 반복시킨다.

예 : 
for j in range(1,10):
	for i in range(1,10):
                    print('2 X', i, '=' ,2*i)

설명 : 2단을 9번 나오게 하는게 아니라 2단부터 9단까지 출력해야하므로 다음과 같이 작성해야합니다.
for i in range(2,10):
    for k in range(1,10):
        print(i ,'x', k,'=',k*i)


문제25. 주사위를 10번 던져서 주사위의 눈을 10개 출력하시오!
import random
dice = [1,2,3,4,5,6]
for i in range(1,11):
    print(random.choice(dice))


문제26. 주사위를 10번 던졌을 때 짝수가 나오는 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,11):
    result = random.choice(dice)
    if result%2 == 0:
        cnt = cnt + 1
print(cnt)

문제27. 위의 주사위를 10번 던져서 짝수가 나오는 횟수를 확인하는 작업을 5번 반복해서 짝수가 나오는 횟수가 5개가 나오게 하시오!
import random
dice = [1,2,3,4,5,6]

for j in range(1,6):
    cnt = 0
    for i in range(1,11):
        result = random.choice(dice)
        if result%2 == 0:
            cnt = cnt + 1
    print(cnt)

설명 : 주사위를 10번 던져서 짝수가 나오는 횟수를 확인하는 for loop 문을 5번 반복하기 위해서 그 위에 for loop 문을 쓰고 5번 반복하였다. 그리고 한번에 4칸 이동시키기 위해서 코드를 선택하고 tab 키를 눌러서 한번에 이동시켰다.

문제28. 동전을 100번 던져서 앞면이 나올 확률을 출력하시오!
import random
coin = ['앞면', '뒷면']
cnt = 0

for i in range(1,101):
	result = random.choice(coin)
	if result == '앞면':
		cnt = cnt + 1
print(cnt/100)


문제29. 위의 동전을 100번 던져서 앞면이 나올 확률을 구하는 작업을 50번 반복해서 확률을 50개 출력하시오!
import random
coin = ['앞면', '뒷면']

for j in range(1,51):
    cnt = 0
    for i in range(1,101):
    	result = random.choice(coin)
    	if result == '앞면':
    		cnt = cnt + 1
    print(cnt/100)


문제30. 파이썬 리스트의 append 함수를 이용해서 위의 확률 50개를 리스트에 담으시오.
import random
coin = ['앞면', '뒷면']
a = [ ]

for j in range(1,51):
    cnt = 0
    for i in range(1,101):
    	result = random.choice(coin)
    	if result == '앞면':
    		cnt = cnt + 1
    print(cnt/100)
    a.append(cnt/100)
print(a)

*리스트 append 함수의 기본 문법

a = [ ] #비어있는 리스트 a를 생성합니다.
a.append(7) #a 리스트에 숫자 7을 넣는다.
print(a)
a.append(8) #a 리스트에 숫자 8을 넣는다.
print(a)


문제 31. 2개의 동전을 동시에 300번 던져서 동시에 둘 다 앞면이 나오는 횟수를 출력하시오!
import  random
coin1 =['앞면', '뒷면']
coin2 =['앞면', '뒷면']
cnt = 0

for   i   in   range(1, 301):
    result1 = random.choice(coin1)
    result2 = random.choice(coin2)
    if  result1=='앞면'  and  result2=='앞면':
        cnt = cnt + 1
print (cnt)


문제32. x라는 리스트를 만들도록 x라는 리스트에 위의 문제에서 앞면이 나오는 횟수를 x 리스트에 담은데 위의 둘다 앞면이 나오는 횟수를 출력하는 for loop 문을 1000번 반복해서 x리스트에 1000개를 입력하시오!
import  random
coin1 =['앞면', '뒷면']
coin2 =['앞면', '뒷면']
x= [ ]

for i in range(1,1001):
    cnt = 0
    for   i   in   range(1, 301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if  result1=='앞면'  and  result2=='앞면':
            cnt = cnt + 1
    x.append(cnt)
print(x)



문제 33. 위의 문제의 평균/ 분산/ 표준편차를 구하시오
import  random
import numpy as np

coin1 =['앞면', '뒷면']
coin2 =['앞면', '뒷면']

x= [ ]
for i in range(1,1001):
    cnt = 0
    for   i   in   range(1, 301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if  result1=='앞면'  and  result2=='앞면':
            cnt = cnt + 1
    x.append(cnt)
print(np.mean(x))
print(np.var(x))
print(np.std(x))


문제34. 한 개의 주사위를 360번 던져서 3의 배수의 눈이 나오는 횟수를 구하는 것을 1000번 하고 그 1000개를 X 변수에 넣고 이 변수 X의 평균과 분산과 표준편차를 구하시오! (점심시간문제)
import random
import numpy as np

dice = [1,2,3,4,5,6]
x = []

for j in range(1,1001):
    cnt = 0
    for i in range(1,361):
        result = random.choice(dice)
        if result == 3 or result == 6:
            cnt = cnt +1
    x.append(cnt)
print(np.mean(x))
print(np.var(x))
print(np.std(x))



■ 12. for 문 개념 배우기 ② (for~continue ~ break)

for 반복문 내에서 continue 를 만나면 그 다음 반복 실행으로 넘어가며 break 를 만나면 for 반복문을 완전히 벗어나게 됩니다.

예제 : 
for 변수 in 범위 : 
	실행코드
continue # 이 부분을 그냥 지나치고 다음 루프 실행문을 계속 실행하시오
	실행코드
break

문제35. 숫자 1-10까지 출력하시오!
for i in range(1,11):
        print(i)


문제36. 위의 결과에서 숫자 5만 출력하지않고 나머지 숫자만 출력하시오!
for i in range(1,11):
    if i == 5:
        continue
    print(i)


문제37. (알고리즘 문제2) 1-10 까지의 숫자 중에 짝수만 출력하시오!
for i in range(1,11):
    if i%2==1:
        continue
    print(i)

문제38. (알고리즘 문제1) 1-10까지의 합을 구하시오!
1.
cnt = 0

for i in range(1,11):
    cnt = cnt + i
print(cnt)
    
2.

x = [ ]
for i in range(1,11):
	x.append(i)
print(sum(x))

■ 13. for 문 개념 배우기 ② (for~else)
"루프문을 중단시키는 역할을 하는 키워드"
예제 :
for i in range(1,11):
    print(i)
    if i==3:
        break

문제39. 1부터 100까지 출력하는 for loop 문을 작성하는데 다음와 같이 숫자를 물어보게해서 입력된 숫자까지만 출력되게하시오!
a = int(input('숫자를 입력하세요'))

for i in range(1,101):
    print(i)
    if i == a:
        break


문제40. (알고리즘 문제 19번) 두 숫자를 각각 물어보게 하고 입력받아 두 숫자의 최대공약수를 출력하시오!
a = int(input('첫번째 숫자를 입력하세요'))
b = int(input('두번째 숫자를 입력하세요'))

for i in range(max(a,b),1,-1):
    if a%i == 0 and b%i == 0:
     break
print(a,'와', b, '의 최대공약수는' ,i,'입니다.')


for ~ else 문을 사용해야합니다.
for ~ else 에서 else 뒤에 실행되는 코드는 for 반복문을 성공적으로 수행해야하지만 실행됩니다.

예제 :
for i in range(1,11):
	print(i)
else:
	print('Perfect') 
	

문제41. 숫자를 물어보게하고 숫자를 입력하면 해당 숫자만큼 1번부터 숫자가 출력되게 하시오!
a=int(input('숫자를 입력하세요~'))

for i in range(1, a+1):
    print(i)


문제42. 위의 입력한 숫자까지 다 출력하면 아래의 perfect 라는 단어가 출력도게 하시오!
a=int(input('숫자를 입력하세요~'))

for i in range(1, a+1):
    print(i)
else:
print('perfect')


문제43. 위의 코드를 수정해서 중단할 숫자를 또 물어보게 해서 아래와 같이 실행되게하세요.
a=int(input('숫자를 입력하세요~'))
b=int(input('중단할 숫자를 입력하세요~'))

for i in range(1, a+1):
    print(i)
    if i == b :
        break
else:
    print('perfect')