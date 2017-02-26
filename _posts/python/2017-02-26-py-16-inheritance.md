---
layout: post
title: 파이썬 파트16. 상속과 다형성
category: python
tags: [python, 파이썬, 상속, inheritance]
comments: true
---
# 파이썬 파트16. 상속과 다형성
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## 상속 (inheritance)

  <center>
  <figure>
  <img src="/assets/post-img/python/inheritance.png" alt="">
  <figcaption>클래스의 상속(inheritance)</figcaption>
  </figure>
  </center>

- 부모클래스 : 상속하는 클래스
- 자식클래스 : 상속받는 클래스
- 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것

```python
class Animal():
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')


class Human(Animal): # 상속 : 클래스 괄호 안에 다른 (부모)클래스를 넣는 것
    def wave(self):
        print('손을 흔든다')

class Dog(Animal): # Animal의 내용을 상속받는다
    def wag(self):
        print('꼬리를 흔든다')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()
```

## 단순 오버라이드 (Override)
- 부모클래스와 같은 이름을 가진 메소드를 덮어쓰기 한다.

```python
class Animal():
    def walk(self):
        print('걷는다')

    def eat(self):
        print('먹는다')

    def greet(self):
        print('인사한다')

class Cow(Animal):
    '''소'''

class Human(Animal): # 상속 : 클래스 괄호 안에 다른 (부모)클래스를 넣는 것
    def wave(self):
        print('손을 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wave()

class Dog(Animal): # Animal의 내용을 상속받는다
    def wag(self):
        print('꼬리를 흔든다')

    def greet(self): # 부모 클래스의 greet 메소드를 덮어쓰기 한다.
        self.wag()

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()
```

## super()
- 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
- super().부모클래스내용

```python
class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name ) # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )
```


## 내 예외 만들기
- 사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
- 파일을 하나 만들어 예외를 정의
- `Exception 클래스`를 상속받아 만든다

<center>
<figure>
<img src="/assets/post-img/python/exception_class.png" alt="">
<figcaption>Exception 클래스 상속</figcaption>
</figure>
</center>

### 코드 예시 1 (my_exception_list.py)

```python
class UnexpectedRSPValue(Exception):
    ''' 가위 바위 보 가운데 하나가 아닌 경우에 발생하는 에러 '''
```

### 코드 예시 2 (my_exception.py)

```python
# 다른파일의 클래스를 불러온다
from my_exception_list import UnexpectedRSPValue

value = input('가위, 바위, 보 중 하나를 선택하세요 >')
try:
    if value not in ['가위', '바위', '보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('입력 값이 올바르지 않습니다.')
```
