# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:18:05 2020

@author: Owner
"""


■ 52. 클래스 생성자 이해하기
클래스의 인스턴스 객체가 생성될 때 자동적으로 호출되는 메소드가 클래스 생성자 입니다. 클래스 생성자는 __init__(self): 입니다.

예제 :
class Card():
	def __init__(self):
	self.cash = 0
	print('카드가 발급되었습니다. %d 원이 충전되어있습니다.' %self.cash)
	
yys_card = Card()

문제167. 총 클래스를 생성하는데 총 클래스로 아래와 같이 총(제품)을 생성하면 "총이 만들어졌습니다. 총알은 0발 장전되었습니다." 라는 메시지가 출력되게 총 클래스를 만드시오!
class Gun():
    def __init__(self):
        self.bullet = 0
        print('총이 만들어졌습니다. 총알은 ',self.bullet,'발 장전되었습니다.' )
        
        
yys_gun1 = Gun()

문제168. 문자열 포맷을 이용해서 위의 메시지가 출력되게 하시오!
class Card():
	def __init__(self):
	self.cash = 0
	print('카드가 발급되었습니다. %d 원이 충전되어있습니다.' %self.cash)
	
yys_card = Card()

■ 53. 클래스 소멸자 이해하기
객체가 사라질 때 자동으로 호출되는 함수를 소멸자(__del__) 이라고 합니다.
예 : 총 클래스로 yys_gun1 이라는 총을 만들고 총을 사용하다가 폐기하고 싶으면 del 명령어로 총을 폐기할 수 있습니다.
이때 자동으로 작동되는 메소드(함수)가 소멸자 함수입니다.

예제 : 
class Gun():
    def __init__(self):
        self.bullet = 0
        print('총이 생성되었습니다.')
    def __del__(self):
        print('총이 폐기되었습니다.')

yys_gun1 = Gun()
del yys_gun1


