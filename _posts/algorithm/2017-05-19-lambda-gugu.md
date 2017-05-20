---
layout: post
title: lambda함수 를 활용한 구구단 생성
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

## 문제
람다함수와 리스트 컴프리헨션을 사용해 한 줄로 구구단의 결과를 갖는 리스트를 생성해본다.

## 풀이코드

```python
[(lambda x,y : '{}x{}={}'.format(x, y, x*y))(x, y) for x in range(2,10) for y in range(1,10)]
```

- (람다함수)(인자)처럼 람다함수 뒤에 인자를 바로 할당 할 수 있다.

```python
# 쉬운 예시
>>> (lambda x,y: x*y)(2,3) # 6
```
