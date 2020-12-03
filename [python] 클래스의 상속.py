# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:18:48 2020

@author: Owner
"""

■ 54. 클래스 상속 이해하기

클래스는 상속이라는 특성을 가지고 있는 이름 공간입니다.
클래스에서 상속이란 어떤 클래스가 가지고 있는 멤버(변수)나 메소드(함수)를 상속받는 클래스가 모두 사용할 수 있도록 해주는 것입니다.
상속을 해주는 클래스를 부모 클래스 또는 슈퍼 클래스라고 하고 상속을 받는 클래스를 자식 클래스 또는 서브 클래스라고 합니다. 부모 클래스로 부터 상속을 받아 자식 클래스를 정의하는 방법은 다음과 같습니다.

예제 : 팀장님이 만든 카드 class #카드설계도
	1. 카드가 발급되었을때 0원이 충전되게 하는 기능
	2. 카드를 충전하는 기능
	3. 카드를 쓰는 기능


class Card():
    def __init__(self):
        self.cash = 0
        print('카드가 발급되었습니다.')
        
    def charge(self,num):
        self.cash += num
        print(num, '원이 충전되었습니다.')
        
    def consume(self,num):
        if self.cash >= num:
            self.cash -= num
            print(num, '원이 사용되었습니다.')
        else:
            print('잔액이 부족합니다.')
            
yys_card1 = Card()
yys_card1.charge(10000)
yys_card1.consume(8000)

문제169. 충전한 금액보다 더 많은 금액을 소비하면 어떻게 되는지 테스트 하시오!
class Card(): #부모클래스
    def __init__(self):
        self.cash = 0
        print('카드가 발급되었습니다.')
        
    def charge(self,num):
        self.cash += num
        print(num, '원이 충전되었습니다.')
        
    def consume(self,num):
        if self.cash >= num:
            self.cash -= num
            print(num, '원이 사용되었습니다.')
        else:
            print('잔액이 부족합니다.')
            
yys_card1 = Card() #카드가 발급되었습니다.
yys_card1.charge(10000) #10000 원이 충전되었습니다.
yys_card1.consume(12000) #잔액이 부족합니다.

문제170. 팀장님이 만든 Card() 클래스를 상속받아 영화할인 카드를 생성하시오!
(영화할인 카드 클래스 : Movie_Card() )
class Card():
    def __init__(self):
        self.cash = 0
        print('카드가 발급되었습니다.')
        
    def charge(self,num):
        self.cash += num
        print(num, '원이 충전되었습니다.')
        
    def consume(self,num):
        if self.cash >= num:
            self.cash -= num
            print(num, '원이 사용되었습니다.')
        else:
            print('잔액이 부족합니다.')
            
            
            
class Movie_card(Card):
    pass
m_card1 = Movie_card()
m_card1.charge(100000)
m_card1.consume(8000)


문제171. 이번에는 제대로 영화관에서 사용하면 할인이 될 수 있도록 영화 클래스를 생성하시오!
class  Card(): # 부모 클래스
    def  __init__(self):
       self.cash = 0
       print  ('카드가 발급되었습니다.')
    
    def  charge(self, num):
        self.cash += num
        print ( num, '원이 충전되었습니다.')

    def  consume(self, num):
        if  self.cash >= num:  # 잔액이 소비하는 돈보다 커야지만 쓸 수있게
            self.cash -= num
            print ( num, '원이 사용되었습니다.')
        else:
            print ('잔액이 부족합니다')
            

class  Movie_Card( Card ): # 부모에게 받은 consume는 내가 만든 consume로 덮어쓰기 됩니다.
    def  consume(self, num, place):
        if  place=='영화관':
            num = 0.8 * num
            if  self.cash >= num:
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        else:
            if  self.cash >= num:
                self.cash -= num
                print ( place, '에서', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')

m_card1 = Movie_Card()
m_card1.charge(20000)
m_card1.consume(12000,'영화관')
m_card1.consume(2000,'편의점') 


문제172. 위의 영화할인 카드에 할인 장소를 추가해서 주유소에서도 20% 할인될 수 있도록 코드를 수정하시오!
class  Card(): # 부모 클래스
    def  __init__(self):
       self.cash = 0
       print  ('카드가 발급되었습니다.')
    
    def  charge(self, num):
        self.cash += num
        print ( num, '원이 충전되었습니다.')

    def  consume(self, num):
        if  self.cash >= num:  # 잔액이 소비하는 돈보다 커야지만 쓸 수있게
            self.cash -= num
            print ( num, '원이 사용되었습니다.')
        else:
            print ('잔액이 부족합니다')
            

class  Movie_Card( Card ):
    def  consume(self, num, place):
        if  place in ('영화관','주유소'):
            num = 0.8 * num
            if  self.cash >= num:
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        else:
            if  self.cash >= num:
                self.cash -= num
                print ( place, '에서', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(2000,'편의점')

문제173. (점심시간 문제) 영화관과 주유소에서는 20% 할인되게 하고 스타벅스에서는 10% 할인되게 하시오
class  Card(): # 부모 클래스
    def  __init__(self):
       self.cash = 0
       print  ('카드가 발급되었습니다.')
    
    def  charge(self, num):
        self.cash += num
        print ( num, '원이 충전되었습니다.')

    def  consume(self, num):
        if  self.cash >= num:  # 잔액이 소비하는 돈보다 커야지만 쓸 수있게
            self.cash -= num
            print ( num, '원이 사용되었습니다.')
        else:
            print ('잔액이 부족합니다')
            

class  Movie_Card( Card ):
    def  consume(self, num, place):
        if  place in ("영화관,주유소"):
            num = 0.8 * num
            if  self.cash >= num:
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        elif place == '스타벅스':
            num = 0.9 * num
            if  self.cash >= num:
                self.cash -= num
                print( place, '에서 ', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')
        else:
            if  self.cash >= num:
                self.cash -= num
                print ( place, '에서', num, '원이 사용되었습니다.')
            else:
                print('잔액이 부족합니다')

m_card1 = Movie_Card()
m_card1.charge(100000)
m_card1.consume(12000,'영화관')
m_card1.consume(30000,'주유소')
m_card1.consume(6000,'스타벅스')
m_card1.consume(2000,'편의점')