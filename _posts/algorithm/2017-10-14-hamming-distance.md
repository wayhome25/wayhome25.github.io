---
layout: post
title: leetcode 461. Hamming Distance
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://leetcode.com/problems/hamming-distance/description/)

## 문제

```
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2**31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

---

## 풀이코드

```python
def hamming_distance(x, y):
    bin_x = format(x, "032b")
    bin_y = format(y, "032b")
    result = 0
    for i in range(32):
        if bin_x[i] != bin_y[i]:
            result += 1
    return result
```
- format() 함수를 활용 ([참고](https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros-in-python))

```
>>> format(10, '010b')
# '0000001010'
>>> format(10, 'b')
# '1010'
>>> format(10, '#b')
# '0b1010'
```

## 다른사람풀이
- 비트연산자 XOR연산 활용 (XOR연산은 각 자릿수를 비교하여 다르면 1, 같으면 0)
- 비트연산자 참고 ([codecademy](https://www.codecademy.com/ko/courses/python-intermediate-ko-0tdxd/0/1))

```python
def hamming_distance(x, y):
  return bin(x^y).count('1')
```
