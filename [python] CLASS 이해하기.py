# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:11:56 2020

@author: Owner
"""


■ 49. 클래스 이해하기 (class)
객체 지향 프로그램에서 중요한 단어가 바로 클래스 입니다.
클래스는 프로그래머가 지정한 이름을 만든 하나의 독립된 공간이며 이름공간(name space) 이라 부릅니다.
클래스를 구성하는 주요요소는 클래스에서 변수 역할을 하는 클래스 멤버와 함수와 동일한 역할을 하는 클래스 메소드 입니다

클래스는 설계도이고 객체는 설계도를 바탕으로 만든 제품
예 : 
총 설계도                      vs                   총
(클래스)                                            (객체)


예제1. 총 클래스(설계도)를 생성하시오
class Gun():
    def charge(self, num): # 총알을 충전하는 함수
        self.bullet = num
    
    def shoot(self, num): #총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('탕!')
                self.bullet -= 1
            elif self.bullet == 0:
                print('총알이 없습니다.')
                break

예제2. 위에서 만든 총설계도를 가지고 총을 한정 만드시오!
gun1 = Gun()

예제3. gun1 이라는 제품에 총알 10발 충전합니다.
gun1.charge(10)

예제4. 총을 쏴보세요.
gun1.shoot(3)

탕!
탕!
탕!

gun1.shoot(10)

탕!
탕!
탕!
탕!
탕!
탕!
탕!
총알이 없습니다.

설명 : 파이썬 클래스를 만들때 self 키워드는 필수 입니다.

총 생산하는 명령어 -- > gun1 = Gun( )
                                gun2 = Gun( )
                                gun3 = Gun ( )

준혁이 gun1 총을 사서 다음과 같이 충전했습니다.
gun1.charge(100)
실제로 총설계도에는 charge(self, num) 이라고 해서 입력 매개변수가 2개인데 총을 사용할 때 충전할 때는 gun1.charge(100) 이렇게 매개변수 하나에 값을 입력했습니다.
그러면 self 입력매개변수에는 자동으로 gun1 이 들어갑니다.

class.Gun( ): #클래스 이름은 첫번째 철자는 대문자 나머지는 소문자로 구성합니다.

문제157. 총설계도를 수정해서 총알을 아래와 같이 충전하면 몇발 충전되었습니다. 라는 메시지가 출력되게하시오!
gun1 = Gun()
gun1.charge(10)

10발이 충전되었습니다.


class Gun():
    def charge(self, num): # 총알을 충전하는 함수
        self.bullet = num
        print('%d발이 충전되었습니다.' %num)
    
    def shoot(self, num): #총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('탕!')
                self.bullet -= 1
            elif self.bullet == 0:
                print('총알이 없습니다.')
                break

gun1 = Gun()
gun1.charge(10)

문제158. 이번에는 총을 쏘면 총알이 탕! 탕! 하면서 아래쪽에 몇발 남았습니다. 라는 메시지가 출력되게하시오!
class Gun():
    def charge(self, num): # 총알을 충전하는 함수
        self.bullet = num
    
    def shoot(self, num): #총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('탕!')
                self.bullet -= 1
                
            elif self.bullet == 0:
                print('총알이 없습니다.')
                break
        print('%d발 남았습니다.'%self.bullet)
gun1 = Gun()
gun1.charge(10)
gun1.shoot(10)


문제159. 총을 처음 생산했을때 총알이 반드시 0발 장전되게 하시오!
class Gun():
    def __init__(self): # 설계도를 가지고 제품을 처음 만들때 자동으로 작동죄는 함수
        self.bullet = 0
        print('총이 만들어졌습니다.', self.bullet, '발 장전되었습니다.')
    def charge(self, num): # 총알을 충전하는 함수
        self.bullet = num
    
    def shoot(self, num): #총을 쏘는 함수
        for i in range(num):
            if self.bullet > 0:
                print('탕!')
                self.bullet -= 1
                
            elif self.bullet == 0:
                print('총알이 없습니다.')
                break
        print('%d발 남았습니다.'%self.bullet)
        
gun1 = Gun() #총이 만들어졌습니다. 0 발 장전되었습니다.

문제160. 총클래스를 이용해서 카드 클래스를 만들고 아래와 같이 카드를 충전하고 사용하시오!
class Card():
    def __init__(self):
        self.money = 0
        print('카드가 만들어졌습니다. %d원이 충전되어있습니다.' %self.money)
        
    def charge(self, num):
        self.money  = num
        print('%d원이 충전되었습니다.' %num)
        
        
    def consume(self, num):
            if self.money > 0:
                self.money -= num
                print('%d원이 사용되었습니다.' %num)
                print('잔액이 %d원 남았습니다.' %self.money)
            elif self.money == 0:
                print('잔액이 없습니다.')


■ 51. 클래스 메소드(함수) 이해하기
card 클래스의 charge 와 consumer 는 메소드 기능입니다.

예 : 
a= [1,2,3,4]
print(type(a))

설명 : 리스트가 클래스라고 출력됩니다. 리스트가 class 라는 말은 리스트 클래스 안에도 분명이 메소드(기능)이 존재할  것입니다.
a = [1,2,3,4]
a.append(5)
print(a)

*리스트 객체의 유용한 메소드
	메소드          설명
	1. append() : 리스트 맨 끝에 새로운 요소를 추가할 때 사용
	2. count() : 리스트에서 특정 요소의 갯수를 카운트할 때 사용
	3. insert() : 리스트의 특정위치에 요소를 입력할 때 사용
	4. remove() : 리스트의 특정 요소를 제거할 때 사용
	5. sort() : 리스트의 요소를 순차적으로 정렬할 때 사용
	6. reverse() : 리스트의 요소를 역순으로 정렬할 때 사용
	7. index() : 리스트의 특정 요소의 위치를 출력할 때 사용

예 :
a = [1,2,3,1,2,2,2,3,4]
print(a.count(2)) # 4




