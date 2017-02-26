---
layout: post
title: python 주요 메소드 목록 (업데이트 중)
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

## enumerate()
### 설명
이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
(※ 보통 enumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.)

### 예시
```python
list = [1, 2, 3, 4, 5]
for i, v in enumerate(list):
    print('index : {} value: {}'.format(i, v))
```

## .format()
### 설명
문자열의 format 함수를 이용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

### 예시
```python
>>> number = 3
>>> "I eat {} apples".format(number)
'I eat 3 apples'
```
