# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:49:10 2020

@author: Owner
"""

■ 81. 문자열에서 특정 문자가 있는지 확인하기 (in)

문자열에서 특정 문자가 있는지 없는지 확인하려면 in 키워드를 이용합니다.

예제 :
txt = 'abcdefghijklmnop'
if 'b' in txt:
    print('존재합니다.')
else:
    print('존재하지 않습니다.')


문제268. emp2.csv 에서 이름을 출력하는데 이름에 S 를 포함하고 있는 사원들의 이름을 출력하시오!

SQL>
select ename
	from emp
	where ename like '%S%';
	
python>
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    if 'S' in emp_list[1]:
        print(emp_list[1])


설명 : 위의 코드는 금융감독원에서 금융사에 요청하는 것 중에 하나가 보험회사의 경우 보험 상담원들이 상담할 때 적절한 보험용어를 써서 고객을 응대를 해야해서 고객과의 통화를 다 녹음하고 그 녹음된 내용을 text 로 변환해서 그 text 안에 단어들을 일일히 확인하는 작업을 합니다.

문제269. 문제268번을 이용하여 코드를 수정해서 출력하는데 이름에 S자가 포함된 사원의 이름이 몇명인지 출력하시오!
import csv
file = open("c:\\data\\emp2.csv")
emp_csv=csv.reader(file)
cnt = 0
for emp_list in emp_csv:
    if 'S' in emp_list[1]:
        cnt = cnt + 1
print(cnt)


■ 82. 문자열에서 특정 문자열이 있는지 확인하기 (in)

보험회사에서 보험 상담원분들이 상담하실때 상담내용 중에 부적절한 용어가 있는지 없는지를 확인하여 금융감독원에 보고를 해야하는데 이 확인 작업이 상당히 많은 인력과 시간이 들기때문에 파이썬으로 쉽게 할 수 있도록 프로그래밍할 때 문자열에서 문자열이 있는지 확인하는 코드를 작성하면 됩니다.

예제 :  겨울왕국 스크립트에서 elsa 라는 단어(문자열)가 몇번 나오는지 카운트 해봅니다.

예제1. 겨울왕국(winter.txt) 스크립트를 파이썬으로 불러와서 출력하시오!
winter = open('c:\\data\\winter.txt')
print(winter) # <_io.TextIOWrapper name='c:\\data\\winter.txt' mode='r' encoding='cp949'>

winter = open('c:\\data\\winter.txt')
for i in winter:
	print(i)
	
예제2. 출력되는 겨울왕국 스크립트를 모두 소문자로 변경하시오!
winter = open('c:\\data\\winter.txt')
for i in winter:
    print(i.lower())

예제3. 위에서 소문자로 출력된 스크립트 한행을 하나 가져와서 아래와 같이 실행하면 뭐가 나올까요?
if  'elsa' in 'olaf skates and helps elsa coach anna.':
	print('존재합니다.')
else:
	print('존재하지않습니다.')
	
예제4. 겨울왕국 스크립트에 elsa 가 몇번 나오는지 카운트 하시오!
winter = open('c:\\data\\winter.txt')
cnt = 0
for i in winter:
    if 'elsa' in i.lower():
        cnt = cnt + 1
print(cnt)

설명 : 위의 코드는 한 행에 elsa가 두번 나와도 cnt는 1번만 카운트 됩니다. 정확하게 하려 위의 문자열에 elsa 가 2개 나오기때문에 cnt가 2개가 되어야 합니다.

예제5. winter.txt 를 한행씩 읽어서 어절 단위로 출력되게 하세요!
winter = open('c:\\data\\winter.txt')
winter2 = winter.read().split(' ')
for i in winter2:
	print(i)
	
예제6. 위의 어절들이 소문자로 나오게 하세요.
winter = open('c:\\data\\winter.txt')
winter2 = winter.read().split(' ')
for i in winter2:
	print(i.lower())
	
문제270. 겨울왕국 스크립트에는 엘사가 몇번 나오는가?
winter = open("c:\\data\\winter.txt")
winter2 = winter.read().split() #아무것ㄷ 안쓰면 어절별로 나뉜다.

cnt = 0
for i in winter2: #어절별로 분리한 것들을 하나씩 가져오면서
        if 'elsa' in j.lower(): #소문자로 변경하고 elas가 포함되어져 있는 어절을
            cnt +=1 #카운트합니다.
            print(cnt)
