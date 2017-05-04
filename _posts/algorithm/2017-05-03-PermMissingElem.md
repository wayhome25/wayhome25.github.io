---
layout: post
title: codility 3-1. PermMissingElem
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/)

## 문제

```
A zero-indexed array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)
that, given a zero-indexed array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Assume that:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
```


## 풀이코드
- Detected time complexity: O(N) or O(N * log(N))

```python
def solution(A):
    li = [0] * (len(A) + 1)
    for i in A:
        li[i-1] = 1  
    return li.index(0) + 1
```

##  다른사람 코드
- 와! 이렇게 쉬운 방법이 있었다니..

```python
def solution(A):
  return sum (range(len(A)+2)) - sum(A)
```
