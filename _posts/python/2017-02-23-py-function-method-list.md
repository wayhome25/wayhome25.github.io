---
layout: post
title: python 주요 메소드, 내장함수 목록 (업데이트 중)
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
# [내장함수 (built-in function)](https://wikidocs.net/32)
> 파이썬 내장 함수들은 외부 모듈과는 달리 import를 필요로 하지 않는다.

## enumerate()
이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
(※ 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.)

### 예시
```python
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('index : {} value: {}'.format(i, v))
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

# 메소드(method)

# 문자열(string)

## .format()
문자열의 format 함수를 이용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

### 예시
```python
>>> number = 3
>>> "I eat {} apples".format(number)
'I eat 3 apples'
```

# [리스트(list)](https://wikidocs.net/14)

## .pop()
pop()은 리스트의 맨 마지막 요소를 돌려 주고 그 요소는 삭제하는 함수이다.

### 예시
```python
>>> a = [1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
```

pop(x)는 리스트의 x번째 요소를 돌려 주고 그 요소는 삭제한다.

### 예시
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

## list.sort( ) / ## list.reverse( )
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
