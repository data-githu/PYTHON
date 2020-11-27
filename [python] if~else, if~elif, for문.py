# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:49:11 2020

@author: Owner
"""

■ 9. if문 개념 배우기 ① if else
어떤 조건을 참과 거짓으로 판단할 때 if 문을 사용합니다.
참과 거짓을 구분하여 코드를 실행하면 if ~ else 를 사용합니다.
코드를 작성하다 보면 조건에 따라 수행하는 일이 달리 해야하는 경우가 있습니다.
조건이 참인지 거짓인지 검사를 하고, 참인 경우에는 이 일을 하고 거짓인 경우에는 다른 일을 하시오 라는 식으로 처리가 가능합니다.

예 : if 조건 :
	실행코드1
     else:
	실행코드2
	
예제 : a= int( input('숫자를 입력하세요~') )
	if a%2 == 0:
		print('짝수입니다.')
	else:
		print('홀수입니다.')


문제12. 주사위의 눈을 담은 dice 변수를 만들고 숫자를 물어보게해서 해당 숫자가 주사위의 눈중에 있으면 해당 숫자가 있습니다 라는 메시지가 출력되게 하고 없으면 해당 숫자가 없습니다 라는 메시지가 출력되게 하시오!
a=int(input('숫자를 입력하세요.'))

dice = [1,2,3,4,5,6]
if a == 1 or a== 2 or a== 3 or a== 4 or a== 5 or a== 6:   # if a in dice 도 가능
	print('주사위의 눈에 숫자 ', a ,' 가 있습니다.')
else:
    print('주사위의 눈에 숫자 ', a ,' 가  없습니다.')


문제13. 숫자 두개를 아래와 같이 각각 물어보게하고 아래처럼 메시지가 출력되게하시오!

첫번째 숫자를 입력하세요! 2
두번째 숫자를 입력하세요! 3

2는 3보다 작습니다.

첫번째 숫자를 입력하세요! 3
두번째 숫자를 입력하세요! 3

3는 2보다 큽니다.

a=int(input('첫번째 숫자를 입력하세요!'))
b=int(input('두번째 숫자를 입력하세요!'))

if a > b:
	print('',a,' 은/는 ',b,'보다 큽니다.')
else: 
    print('',a,' 은/는 ',b,'보다 작습니다.')


■ 10. if문 개념 배우기 ② if~ elif

특정 로직을 수행하고자 할 때 if~ elif문을 사용합니다.

예제 :
if 조건1
	실행코드1
elif 조건2
	실행코드2
else
	실행코드3

예제 : 문제 13번을 다시 수행하는데 같은 숫자가 2개가 들어오면 서로 같습니다. 라는 메시지가 출력되게하시오.

a=int(input('첫번째 숫자를 입력하세요!'))
b=int(input('두번째 숫자를 입력하세요!'))

if a > b:
	print('',a,' 은/는 ',b,'보다 큽니다.')
elif a<b:
	print('',a,' 은/는 ',b,'보다 작습니다.')
else: 
    print('',a,' 와 ',b,'는 같습니다.')


■ 11. for 문 개념 배우기 ①for

특정 코드를 반복적으로 수행하기 위해서는 반복문을 사용해야 하는데 파이썬에서는 for문이 반복문을 수행하기 위해 가장 많이 사용되는 문법입니다.

형식 : for 변수 in 범위:
		반복적으로 실행할 코드

	1. 리스트 범위인 경우
for i in [1,2,3]:
	print(i)

	2. 튜플 범위인 경우
for i in (1,2,3):
	print(i)

	3. range() 범위인 경우
for i in range(10):
	print(i)
0
1
2
3
4
5
6
7
8
9


	4. 사전형 범위인 경우
m={'i':'나는','am':'입니다.','boy':'소년'}
for i in m:
	print(i)  #키값만 출력됩니다.
	
	5. 문자형 범위인 경우
for i in 'i am boy':
	print(i)


 for 루프(loop)문의 range 사용법 정리

for i in range(1,6):
	print(i) # 1부터 5까지 출력
for i in range(1,6,2):
	print(i) # 1,3,5를 출력
for i in range(6,1,-1):
	print(i) #6부터 1씩 차감해서 2까지 출력한다.
	
문제 14. ★을 5개 출력하시오!
★★★★★
print('★'*5)


문제 15. (알고리즘 5번 문제) 아래와 같은 결과가 출력되는 파이썬 코드를 작성하시오!

숫자를 입력하세요~ 5
★
★★
★★★
★★★★
★★★★★

a=int(input('숫자를 입력하세요~'))
for i in range(1,a+1):
    print('★'*i)

문제16. 점심시간에는 주사위를 1번만 던졌는데 지금은 주사위를 10번 던져서 출력되는 눈을 확인하시오!
import random
dice = [1,2,3,4,5,6]
for i in range(11):
    print (random.choice(dice))


문제17. 동전을 10번 던지세요
import random
coin = ['앞면', '뒷면']
for i in range(1,11):
	print(random.choice(coin))
	
	
문제 18. 동전을 10번 던졌을때 앞면이 나오는 횟수가 어떻게 되는가?
import random
coin =['앞면','뒷면']
cnt = 0

for i in range(1,11):
    result = random.choice(coin)
    if result == '앞면':
        cnt = cnt +1
print(cnt)

문제 19. 주사위를 100번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오!
import random
dice = [1,2,3,4,5,6]
cnt = 0
	
for i in range(1,101):
	result = random.choice(dice)
	if result == 3:
	       cnt = cnt + 1
print(cnt)

문제 20. 주사위를 1000번 던지고 주사위의 눈이 5가 나올 확률을 구하시오
import random
dice = [1,2,3,4,5,6]
cnt = 0

for i in range(1,1001):
	result = random.choice(dice)
	if result == 5:
	cnt = cnt +1
print(cnt/1000)

문제21. 동전을 10000번 던져서 앞면이 나올 확률을 출력하시오!
import random
coin =['앞면','뒷면']
cnt = 0

for i in range(1,10001):
    result = random.choice(coin)
    if result == '앞면':
        cnt = cnt +1
print(cnt/10000)

문제22. (오늘의 마지막문제) (SQL 알고리즘 13번)
주사위 하나와 동전한개를 동시에 던져서 주사위의 눈은 5가 나오고 동전은 앞면이 나올 확률은 어떻게 되는가?
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

	
