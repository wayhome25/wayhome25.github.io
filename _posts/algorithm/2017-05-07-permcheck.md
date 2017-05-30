---
layout: post
title: codility 4-2. Perm Check
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/4-counting_elements/)

## 문제

```
A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.
Write a function:
def solution(A)

that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.
For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.
Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage
(not counting the storage required for input arguments).

```

## 풀이코드
### 풀이코드 1
- Detected time complexity: O(N) or O(N * log(N))

```python
def solution(A):
    M = max(A)
    B = list(set(A))
    if len(B) == M and len(A) == len(B) and sum(range(M+1)) == sum(B):
        return 1
    return 0
```

### 풀이코드 2
- Detected time complexity: O(N^2)
- 문제점 : A = [1000000000] 와 같은 인자가 주어지면, sum(range(max(A)+1)) 부분에서 많은 시간이 소요된다.

```python
def solution(A):
    B = list(set(A))
    if len(A) == len(B) and sum(range(max(A)+1)) == sum(B):
        return 1
    return 0
```

### 풀이코드 3
- Detected time complexity: O(N^2)

```python
def solution(A):
    if len(A) == max(A):
        for idx, var in enumerate(A): # O(N)
            if var in A[idx+1:]: # O(N^2)
                return 0
        return 1
    return 0
```

## 다른사람 풀이
- 비트단위 연산을 활용하였다.
- [bitwise 연산자를 공부하자](https://www.codecademy.com/courses/python-intermediate-ko-0tdxd/0/1)

```python
def solution(A):
    N = len(A)

    xorSum = 0
    for i in range(1, N+1):
        xorSum ^= i ^ A[i-1]

    if xorSum == 0:
        return 1
    else:
        return 0
```

- or 연산자 활용


```python
def solution(A):
    if max(A) != len(A) or len(set(A)) != len(A):
        return 0
    return 1
```
