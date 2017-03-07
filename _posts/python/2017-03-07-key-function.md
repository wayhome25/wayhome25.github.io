---
layout: post
title: 파이썬 정렬시 특정 기준으로 정렬하는 방법 - key Fucntion, repr 메소드
category: python
tags: [python, 파이썬, datetime]
comments: true
---

# Key Functions
> `list.sort()`, `sorted()` 를 통한 정렬 시 비교 기준이 되는 key 파라미터를 가질 수 있다.


## sorting 할때 key 값을 기준으로 정렬

- [가이드 문서](https://docs.python.org/3/howto/sorting.html?highlight=sorting#key-functions)
- key 파라미터의 값은 하나의 인자를 받고, 정렬 목적을 위한 키를 리턴하는 함수가 되어야 한다.

```shell
# 공백을 기준으로 문자열을 나누어 리스트로 변환한다
# 리스트로 변환시
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```


## 복잡한 객체를 정렬할 때 자주 사용

```shell
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   
# sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## 이름표가 있는 속성을 가진 객체에서도 자주 사용

```shell
>>> class Student:
...     def __init__(self, name, grade, age):
...         self.name = name
...         self.grade = grade
...         self.age = age
...     def __repr__(self):
...         return repr((self.name, self.grade, self.age))
```

## `__repr__` 메서드의 오버라이딩

- [참고글](http://pinocc.tistory.com/168)
- `__repr__` 메서드를 정의하지 않으면 object 클래스가 가진 기본 `__repr__` 메서드를 사용한다. 이 함수는 클래스 이름과 변수가 위치하고 있는 메모리 주소를 <>안에 써서 반환한다.
- repr() 은 `__repr__` 메소드를 호출하고, str() 이나 print 는 `__str__` 메소드를 호출하도록 되어있는데, `__str__` 은 객체의 비공식적인(informal) 문자열을 출력할 때 사용하고, `__repr__` 은 공식적인(official) 문자열을 출력할 때 사용한다.
- 쉽게 말하면 `__str__` 은 사용자가 보기 쉬운 형태로 보여줄 때 사용하는 것이고, `__repr__` 은 시스템(python interpreter)이 해당 객체를 인식할 수 있는 공식적인 문자열로 나타내 줄 때 사용하는 것이다.


```shell
>>> student_objects = [
...     Student('john', 'A', 15),
...     Student('jane', 'B', 12),
...     Student('dave', 'B', 10),
... ]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
