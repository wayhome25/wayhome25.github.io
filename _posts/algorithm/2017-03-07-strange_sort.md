---
layout: post
title: level 1. 문자열 내 마음대로 정렬하기 - Key Functions, __str__, __repr__
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 문자열 내 마음대로 정렬하기
> [출처](http://tryhelloworld.co.kr/challenge_codes/95)

## 문제
strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.

예를들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 ["car", "bed", "sun"]이 됩니다.
strange_sort함수를 완성해 보세요.

## 풀이 (python)
```python
def strange_sort(strings, n):
    return sorted(strings, key=lambda element:element[n])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
```


## 배운점
- sorted() 함수는 정렬된 결과 값을 바로 리턴한다.
- 대문자는 소문자 보다 우선한다. (['A', 'a', 'ab'])
- Key Functions
- sorting 할때 `key 값을 기준으로 정렬`할 수 있다. [가이드 문서](https://docs.python.org/3/howto/sorting.html?highlight=sorting#key-functions)
  - `list.sort()`, `sorted()` 둘다 정렬시 비교 기준이 되는 key 파라미터를 가질 수 있다.

```shell
# 공백을 기준으로 문자열을 나누어 리스트로 변환한다
# 리스트로 변환시
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```
  - key 파라미터의 값은 하나의 인자를 받고, 정렬 목적을 위한 키를 리턴하는 함수가 되어야 한다.

  - 일반적으로 어떤 객체를 키로 사용하는 복잡한 객체를 정렬할 때 자주 사용된다.

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

  - 이와 같은 테크닉은 이름표가 있는 속성을 가진 객체에서도 자주 사용된다.

```shell
>>> class Student:
...     def __init__(self, name, grade, age):
...         self.name = name
...         self.grade = grade
...         self.age = age
...     def __repr__(self):
...         return repr((self.name, self.grade, self.age))
```

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
