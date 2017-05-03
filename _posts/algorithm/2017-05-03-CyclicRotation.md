---
layout: post
title: codility - CyclicRotation
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/2-arrays/cyclic_rotation/)

## 문제

```
A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

Write a function:

def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
```


## 풀이과정
- 인자로 받은 리스트 A와 동일한 길이를 가진 배열 result를 정의
- 리스트 A 를 순회하면서 기존의 index 에 K를 더하여 new_idx 변수에 담는다.
  - 만약 new_idx 가 리스트 A의 길이보다 크거나 같다면,
  - 리스트 A의 길이 (len(A))로 나눈 나머지를 new_idx 에 다시 담는다
-  new_idx를 사용하여 배열 result를 재정의 한다.

## 풀이코드

```python
def solution(A, K):
    result = [0] * len(A)
    for idx, val in enumerate(A):
        new_idx = idx + K

        if new_idx >= len(A):
            new_idx = new_idx % len(A)

        result[new_idx] = val
    return result
```

##  다른사람 코드
- 리스트 슬라이싱 기능을 사용하면 더 간단하게 해결 가능하다.


```python
def solution(A, K):
    if len(A) == 0:
        return A

    return A[len(A)-(K%len(A)):] + A[:len(A)-(K%len(A))]
```
