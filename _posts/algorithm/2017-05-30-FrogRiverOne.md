---
layout: post
title: codility 4-1. FrogRiverOne
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/4-counting_elements/)

예전에 2시간을 고민하고도 풀지 못했던 문제였다.     
한달이 지나고 나서 다시 풀어보았는데,
시간복잡도 O(N^2)로 풀었다가 시간복잡도 O(N)으로 성능 개선하는데 성공했다. 너무 뿌듯하다!! :)

---

## 문제
```
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given a zero-indexed array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)
that, given a non-empty zero-indexed array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Assume that:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).

```

## 풀이코드

### 첫번째 시도
- 시간복잡도 : O(N ** 2)
- for loop 안에서 A in B 검색을 사용해서 O(N**2) 시간복잡도

```python
def solution(X, A):
    check = [False] * X
    for idx, val in enumerate(A):
        check[val-1] = True
        if not False in check:
            return idx
    return -1   
```

### 두번째 시도
- 시간복잡도 : O(N)
- A in B 검색을 사용하지 않기 위해서 별도의 check_sum 변수를 활용

```python
def solution(X, A):
    check = [0] * X
    check_sum = 0
    for i in range(len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            check_sum += 1
            if check_sum == X:
                return i
    return -1
```
