---
layout: post
title: codility 5-2. PassingCars
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/5-prefix_sums/passing_cars/)

## 문제

```
A non-empty zero-indexed array A consisting of N integers is given.
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars.
We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty zero-indexed array A of N integers,
returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1),
beyond input storage (not counting the storage required for input arguments).
```

## 풀이코드
- Detected time complexity: O(N)
- 조합 가능한 (0,1) pair의 갯수를 찾는다
- 조건
	- 0의 index < 1의 index
	- pair의 갯수가 100만이 넘으면 -1 리턴
	- 시간 복잡도 O(N)

```python
def solution(A):
    temp_li_p = []
    temp_li_q = []
    for idx, val in enumerate(A):
        if val == 0:
            temp_li_p.append(idx)
        else:
            temp_li_q.append(idx)

    result = 0
    for idx, val in enumerate(temp_li_p):
        result += (len(A)-val) - (len(temp_li_p)-idx)

    if result > 1000000000:
        return -1
    return result
```

## 다른사람 풀이
- 리스트를 역으로 순회하면서, 1의 갯수를 누적해서 더하고, 0을 만나면 누적 값을 total에 합산한다
- range(4, -1, -1) = range(시작, 끝, 증가값) = 4, 3, 2, 1, 0

```python
def solution(A):
    total = 0
    count_one = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 1:
            count_one += 1
        elif A[i] == 0:
            total += count_one
    if total > 1000000000:
        return -1
    return total
```
