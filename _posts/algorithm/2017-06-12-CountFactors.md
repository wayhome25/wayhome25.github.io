---
layout: post
title: codility 10-2. CountFactors
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/10-prime_and_composite_numbers/)


---

## 문제
> A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.
For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

> Write a function:
def solution(N)
that, given a positive integer N, returns the number of its factors.
For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

> Assume that:
N is an integer within the range [1..2,147,483,647].
Complexity:
expected worst-case time complexity is O(sqrt(N));
expected worst-case space complexity is O(1).

## 풀이코드
- 시간복잡도 : O(sqrt(N))
- 1 ~ 루트 N 까지의 숫자만 검색하여 시간복잡도 O(sqrt(N)) 으로 연산

```python
def solution(N):
    i = 1
    result = 0
    while i**2 <= N:
        print(i)
        if i ** 2 == N:
            result += 1
        elif N % i == 0:
            result += 2
        i += 1
    return result
```

## 다른사람 코드

```python
def solution(N):
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has two factors: candidate and N // candidate
        if N % candidate == 0:      
          result += 2

        candidate += 1

    # If N is square of some value.
    if candidate * candidate == N:  result += 1

    return result
```
