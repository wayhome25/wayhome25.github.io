---
layout: post
title: level 1. 최솟값 만들기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 최솟값 만들기
> [출처](http://tryhelloworld.co.kr/challenge_codes/182)

## 문제
자연수로 이루어진 길이가 같은 수열 A,B가 있습니다. 최솟값 만들기는 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱한 값을 누적하여 더합니다. 이러한 과정을 수열의 길이만큼 반복하여 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다.

예를 들어 A = [1, 2] , B = [3, 4] 라면
1. A에서 1, B에서 4를 뽑아 곱하여 더합니다.
2. A에서 2, B에서 3을 뽑아 곱하여 더합니다.

수열의 길이만큼 반복하여 최솟값 10을 얻을 수 있으며, 이 10이 최솟값이 됩니다.
수열 A,B가 주어질 때, 최솟값을 반환해주는 getMinSum 함수를 완성하세요.

## 풀이 (python)
```python
def getMinSum(A,B):
    A = sorted(A)
    B = sorted(B)
    B.reverse()
    return sum([a * b for a, b in list(zip(A, B))])

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))
```

## 다른사람 풀이
```python
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
```

## 배운점
- `sorted(B, reverse=True)` 를 통해서 B를 내림차순으로 정렬할 수 있다.
- zip() 함수 : zip(iterable*)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

```shell
>>> list(zip([1, 2, 3], [4, 5, 6]))  
# [(1, 4), (2, 5), (3, 6)]
>>> list(zip("abc", "def"))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]

```
