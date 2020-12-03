# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:21:49 2020

@author: Owner
"""

■ 50. 클래스 멤버와 인스턴스 멤버 이해하기

클래스에서 선언된 변수는 클래스 멤버(변수)와 인스턴스 멤버(변수)가 있습니다.
클래스 멤버는 클래스 메소드 바깥에서 선언되고 인스턴스 멤버는 클래스 메소드 안에서 self와 함께 선언되는 변수입니다.

이름을 출력하는 함수와 월급을 인상하는 함수를 담은 클래스 생성




class  Employees: #괄호 () 를 따로 안 쓴 이유는 밑에 __init__ 함수에 입력 매개변수가 여러 개 이기 때문입니다.
    raise_amount = 1.1  # 클래스 변수(클래스 멤버)
    def __init__(self, first, last, pay): # 객체가 만들어질때 바로 작동되는 함수
        self.first = first               
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
       print  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * self.raise_amount)


emp_chulsu = Employees('chulsu', 'kim', 5000000)
print(emp_chulsu.pay)   # 5000000
emp_chulsu.apply_raise()
print(emp_chulsu.pay)  # 5500000

emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)
emp_chulsu2.raise_amount = 1.2
print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000


class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * Employees.raise_amount)  # 클래스 변수를 사용 


emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

emp_chulsu2.raise_amount = 1.2   # 인스턴스 변수만 변경할 수 있고 클래스 변수는
                                             # 변경할 수 없다. 

print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000


문제174. 위에서 생성한 객체 emp_chulsu의 email 변수에 있는 내용을 출력해보시오!
class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * self.raise_amount)


emp_chulsu = Employees('chulsu', 'kim', 5000000)
print(emp_chulsu.pay)   # 5000000

print(emp_chulsu.email)

문제175. 철수의 월급을 회사규정에 따라 인상시키시오!
emp_chulsu.apply_raise()
print(emp_chulsu.pay)  # 5500000

문제176. 이번에는 새로운 사원 철수2로 emp_chulsu2 객체를 생성하시오!
emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

문제177. 철수2 사원이 월급을 인상시키기 위한 인스턴스 변수를 알아냈습니다. 자기는 월급을 10% 인상이 아니라 20% 인상시키고 싶습니다. 철수2의 월급인상률을 변경하시오!
emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)
emp_chulsu2.raise_amount = 1.2
print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 6000000

문제178. 그래서 위와 같이 악용이 되지 않도록 막는 방법은 무엇입니까?
class  Employees:
    raise_amount = 1.1  # 클래스 변수
    def __init__(self, first, last, pay): # 객체가 만들어질때
        self.first = first               # 바로 작동되는 함수
        self.last  = last
        self.pay   = pay
        self.email = first.lower() + '.' + last.lower() + '@gmail.com'
        self.raise_amount = 1.1  # 인스턴스 변수

    def  full_name(self): #사원의 전체이름을 출력하는 함수
        return  '{} {}'.format(self.first, self.last)

    def  apply_raise(self): # 월급을 인상하는 함수
        self.pay = int( self.pay * Employees.raise_amount)  # 클래스 변수를 사용 


emp_chulsu2 = Employees('chulsu2', 'kim', 5000000)

emp_chulsu2.raise_amount = 1.2   # 인스턴스 변수만 변경할 수 있고 클래스 변수는
                                             # 변경할 수 없다. 

print(emp_chulsu2.pay)   # 5000000
emp_chulsu2.apply_raise()
print(emp_chulsu2.pay)  # 5500000

설명 : 위와 같이 민감한 변수들은 인스턴스 변수가 아니라 클래스 변수(멤버)를 사용해서 계산되게 코딩해야합니다.

클래스내의 변수는 2개가 있는데
	1. 클래스 변수 : 메소드 바깥의 변수
			객체 생성이후에 안의 값을 변경할 수 없다.
	2. 인스턴스 변수 : 메소드 안의 변수 
			객체 생성이후에 안의 값을 변경할 수 있다.