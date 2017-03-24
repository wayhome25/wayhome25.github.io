---
layout: post
title: level 1. 피보나치 수
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 피보나치 수
> [출처](http://tryhelloworld.co.kr/challenge_codes/5)

## 문제
피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 예를 들어 n = 3이라면 2를 반환해주면 됩니다.

## 풀이 (python)
```python
def fibonacci(num):
    l = []
    a, b = 0, 1
    while len(l) != num+1:
        l.append(a)
        a, b = b, a+b
    return l[-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))
```

## 다른사람 풀이
```python
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a
```

## 배운점
- a, b = 0, 1 같이 2개의 변수에 값을 한꺼번에 담을 수 있다.
