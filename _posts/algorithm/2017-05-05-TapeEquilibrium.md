---
layout: post
title: codility 3-3. TapeEquilibrium
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/3-time_complexity/)

## 문제

```
A non-empty zero-indexed array A consisting of N integers is given.
Array A represents numbers on a tape.
Any integer P, such that 0 < P < N,
splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
In other words, it is the absolute difference between
the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7

Write a function: def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the minimal difference that can be achieved.
For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Assume that:
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N),
beyond input storage (not counting the storage required for input arguments).
```

## 풀이코드
- Detected time complexity: O(N * N)
- `list slice 후, sum() 을 통해서 합계를 구하는 부분이 O(N^2)의 시간 복잡도를 가진다.`

```python
def solution(A):
    li = []
    for P in range(1,len(A)):
        sum1 = sum(A[:P]) # O(N^2)
        sum2 = sum(A[P:])
        diff = sum1 - sum2 if sum1 >= sum2 else sum2 - sum1
        li.append(diff)
    return min(li)
```

## 다른사람 풀이
- Detected time complexity: O(N)
- `abs()` 내장 함수를 통해서 숫자의 절대값을 구할 수 있다. abs(-3) >> 3, abs(1,2) >> 1.2  
- list slice를 사용하지 않는다.
- min_difference 변수에 None을 담아서 시작한다.

```python
def solution(A):
    sum_of_part_one = 0
    sum_of_part_two = sum(A)
    min_difference = None

    for i in range(1, len(A)):
        sum_of_part_one += A[i-1]
        sum_of_part_two -= A[i-1]
        difference = abs(sum_of_part_one - sum_of_part_two)

        if min_difference == None:
            min_difference = difference
        else:
            min_difference = min(min_difference, difference)

    return min_difference
```
