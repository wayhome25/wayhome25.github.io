---
layout: post
title: python 주요 메소드, 내장함수, 외장함수 목록 (업데이트 중)
category: python
tags: [python, 메소드, method, 함수]
comments: true
---
<!----------------- 탬플릿
## forEach
### 설명

### 문법
```python

```
### 예시
```python

```
------------------->

추가 내용은 [구글독스](https://docs.google.com/spreadsheets/d/1T91SzL2NgWiMOK99CAlJJSDvciCzlYhWMvNMlOXtIG4/edit#gid=0)에 정리

# [내장함수 (built-in function)](https://wikidocs.net/32)
> 파이썬 내장 함수들은 외부 모듈과는 달리 import를 필요로 하지 않는다.

## enumerate()
이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
(※ 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.)

```python
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('index : {} value: {}'.format(i, v))
```
## str()
str(object)은 문자열 형태로 객체를 반환하여 리턴하는 함수이다.

```python
>>> str(3)
'3'
>>> str('hi')
'hi'
>>> str('hi'.upper())
'HI'
```
## join() / split()
리스트를 문자열로 / 문자열을 리스트로 변환하는 함수.

### 구분자.join(리스트) - 리스트(List)를 특정 구분자를 포함해 문자열(String)으로 변환

```python
animals = ['사자', '코끼리', '기린', '원숭이', '바나나원숭이']

print ",".join(animals)
# >> 사자,코끼리,기린,원숭이,바나나원숭이

print "\n".join(animals)
# >> 사자
# >> 코끼리
# >> 기린
# >> 원숭이
# >> 바나나원숭이

print "/".join(animals)
# >> 사자/코끼리/기린/원숭이/바나나원숭이
```
### 문자열.split(구분자) - 문자열(String)을 특정 '구분자'를 기준으로 리스트(List) 로 변환

```python
animals = ['사자', '코끼리', '기린', '원숭이', '바나나원숭이']

animal_string = "/".join(animals)
# >> 사자/코끼리/기린/원숭이/바나나원숭이

animal_split = animal_string.split("/") print animal_split
# >> ["사자", "코끼리", "기린", "원숭이", "바나나원숭이"]
```

## zip()
zip(iterable*)은 `동일한 개수로 이루어진 자료형`을 묶어 주는 역할을 하는 함수이다.

```python
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```
--------
# [외장함수](https://wikidocs.net/33)
> 이제 파이썬 프로그래밍 능력을 높여 줄 더 큰 날개를 달아 보자. 전 세계의 파이썬 사용자들이 만든 유용한 프로그램들을 모아 놓은 것이 바로 파이썬 라이브러리이다. "라이브러리"는 "도서관"이라는 뜻 그대로 원하는 정보를 찾아보는 곳이다. 모든 라이브러리를 다 알 필요는 없고 어떤 일을 할 때 어떤 라이브러리를 사용해야 한다는 정도만 알면 된다. 그러기 위해 어떤 라이브러리들이 존재하고 어떻게 사용되는지 알아야 할 필요가 있다. 자주 사용되고 꼭 알아두면 좋은 라이브러리들을 중심으로 하나씩 살펴보자.
(※ 파이썬 라이브러리는 파이썬 설치 시 자동으로 컴퓨터에 설치가 된다.)



## random
random은 난수(규칙이 없는 임의의 수)를 발생시키는 모듈이다

```python
>>> import random
>>> random.random() # 0.0에서 1.0 사이의 실수 중에서 난수값을 리턴
0.53840103305098674

>>> random.randint(1, 10) #1에서 10 사이의 정수 중에서 난수값을 리턴한다.
6
```

random.choice 함수는 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다.
리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 이용하면 된다.

```python
>>> import random
>>> data = [1, 2, 3, 4, 5]
>>> random.shuffle(data)
>>> data
[5, 1, 3, 4, 2]
```

---------
# 메소드(method)

# 문자열(string)

## 문자열 포매팅 - %s
 %s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있다.

```python
>>> number = 10
>>> day = "three"
>>> "I ate %s apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
>>> "I have %s apples" % 3
'I have 3 apples'
```
## .format()
문자열의 format 함수를 이용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

```python
>>> number = 3
>>> "I eat {} apples".format(number)
'I eat 3 apples'
```
---------

# [리스트(list)](https://wikidocs.net/14) 메소드

## .pop()
pop()은 리스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수이다.

```python
>>> a = [1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
```

pop(x)는 리스트의 x번째 요소를 돌려 주고 그 요소는 삭제한다.

```python
>>> a = [1,2,3]
>>> a.pop(1)
2
>>> a
[1, 3]
```

## list.index( value )
값을 이용하여 위치를 찾는 기능
```python
>>> list1 = ['a', 'b', 'q', 'f']
>>> list1.index('b')
1
```

## list.extend( [value1, value2] )
extend(x)에서 `x에는 리스트만` 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
a.extend([4,5])는 a += [4,5]와 동일 (.extend() > '+'연산자 보다 성능이 좋음)
```python
>>> list1 = ['a', 'b', 'q', 'f']
>>> list2 = [1, 2, 3]
>>> list1.extend(list2)
>>> list1
['a', 'b', 'q', 'f', 1, 2, 3]
```

## list.append
append를 사전에서 검색해 보면 "덧붙이다, 첨부하다"라는 뜻이 있다. 이 뜻을 안다면 아래의 예가 금방 이해가 될 것이다. append(x)는 리스트의 맨 마지막에 x를 추가시키는 함수이다.
```python
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]

>>> a.append([5,6])
>>> a
[1, 2, 3, 4, [5, 6]]
```

## list.insert( index, value )
원하는 위치에 값을 추가
```python
list1 = ['a', 'b', 'q', 'f', 1, 2, 3]
>>> list1.insert(1, 'hi')
>>> list1
['a', 'hi', 'b', 'q', 'f', 1, 2, 3]
```

## list.sort( ) / list.reverse( )
값을 순서대로 정렬 / 값을 역순으로 정렬
```python
list1 = ['a', 'hi', 'b', 'q', 'f', 1, 2, 3]

>>> list1.sort()
>>> list1
[1, 2, 3, 'a', 'b', 'f', 'hi', 'q']

>>> list1.reverse()
>>> list1
['q', 'hi', 'f', 'b', 'a', 3, 2, 1]
```
