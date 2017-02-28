---
layout: post
title: django 02. 파이썬 기초
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 02. 파이썬 기초
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## 오브젝트란?

### 객체지향 프로그램
- 프로그래밍으로 문제해결을 더 쉽게하기 위해
- 큰 프로그램의 유지보수를 편하게 하기 위해
- 막장을 미연에 방지하기 위해 사용하는 개발 방법론이다.

### 오브젝트 = 객체
- Object is a thing
- 실생활에 존재하는 어떤 것
- 상태와 행동을 가짐

### 클래스
- 오브젝트를 생성하기 위한 틀 (템플릿)
- 상태(state)와 행동(behavior)를 가짐
- 객체는 클래스의 `인스턴스`다.

### Django와 Object
- Django는 많은 부분에 객체를 활용한다.
- Models
- Class-based View
- MTV (Model - Template - View)

### 요약
- 클래스 : 메소드와 값을 가지는 사용자 정의 데이터 타입
- 객체 : `클래스를 인스턴스화` 한 것

## 오브젝트 실습

```python
class Text:
    # pass # 아무것도 안하겠다는 의미
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class: " + self.text

t = Text("hi")
print(t) # Text Class: hi
print(t.text) # hi
```

## 클래스 변수와 인스턴스 변수

- [관련 포스트 링크](https://medium.com/python-with-askdjango/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%EC%9D%98-%EC%98%AC%EB%B0%94%EB%A5%B4%EA%B2%8C-instance-variable-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0-5668e399bd0e#.pq5vlqa79)
- `클래스 변수` : 모든 클래스의 인스턴스간에 값을 공유하는 변수
- `인스턴스 변수` : 인스턴스마다 개별적으로 다른 값을 가지는 변수 (메소드 안에서 self와 함께 정의)

```python
class User:
  num_users = 0 # class 변수
  def __init__(self, name):
      self.name = name # instance 변수 (메소드 안에서 self라는 키워드를 사용해서 선언하는 변수)
      User.num_users += 1

u = User('monkey')
print(User.num_users, u.name) # 1 monkey
u2 = User('sunshine')
print(User.num_users, u2.name) # 2 sunshine
print(User.num_users, u.num_users, u2.num_users) # 2, 2, 2
# 클래스 변수는 모든 인스턴스들 간에 값을 공유한다.
# class User의 인스턴스 u, u2 모두 똑같은 num_users 값을 가진다.
```

## 오브젝트 실습 2

```python
class Text:
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class: " + self.text

class User:
    numUsers = 0 # 클래스 변수
    def __init__(self, name):
        self.numArticle = 0 # 인스턴스 변수로 초기화
        self.name = name
        self.articles = [] # 인스턴스 변수
        User.numUsers += 1

    def write(self, text):
        self.articles.append(text)
        self.numArticle += 1

    def __str__(self):
        return "User class: %s, %s" % (self.name, ' / '.join(str(p) for p in self.articles)) #방법 1
        # return 'User class : %s, %s' % (self.name, [str(p) for p in self.articles]) 방법 2


t = Text('This is some text')
t2 = Text('This is some text2')
user = User('monkey')
user.write(t)
user.write(t2)

# print([t][0])
print(t) # Text Class: This is some text
print(user,',',user.numArticle)
#monkey, Text Class: This is some text / Text Class: This is some text2, 2
```

## 오브젝트 실습 3
- 장고에서 `__str__` 메소드 오버라이딩과 `클래스 상속`은 자주 사용한다.   
  (상속받는 클래스에서 함수를 재구현하는 것을 메서드 오버라이딩(Overriding) 이라고 부른다.)

```python
class Text:
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class " + self.text

    def getLength(self):
        return len(self.text)

class Article(Text): #Article 클래스(자식클래스)는 Text 클래스(부모클래스, 슈퍼클래스)를 상속 받았다.
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __str__(self):
        return 'Article Class %s %s' % (self.title, self.text)

class User:
    numUsers = 0 # 클래스 변수
    def __init__(self, name):
        self.numArticle = 0 # 인스턴스 변수로 초기화
        self.name = name
        self.articles = [] # 인스턴스 변수
        User.numUsers += 1

    def write(self, text):
        self.articles.append(text)
        self.numArticle += 1

    def __str__(self):
        return "%s, %s" % (self.name, ' / '.join(str(p) for p in self.articles))

t = Article('hello', 'This is some text') 
t2 = Article('hello2', 'This is some text2')
user = User('monkey')
user.write(t)
user.write(t2)

# print([t][0])
print(t,', ',t.getLength()) # Article Class hello This is some text ,  17
print(user,',',user.numArticle)
# monkey, Article Class hello This is some text / Article Class hello2 This is some text2 , 2
```
