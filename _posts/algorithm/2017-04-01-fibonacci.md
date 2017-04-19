---
layout: post
title: 피보나치 수열 구하기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---
> [문제출처](http://codingdojang.com/scode/461?langby=python)

## 문제
피보나치 수열이란, 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때, 이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다.

예) 0, 1, 1, 2, 3, 5, 8, 13

인풋을 정수 n으로 받았을때, n 이하까지의 피보나치 수열을 출력하는 프로그램을 작성하세요

## 풀이

```python
def fib(n):
    array = [0, 1]
    i = 0
    while array[i] + array[i+1] < n:
        array.append(array[i]+array[i+1])
        i += 1
    return array
```
