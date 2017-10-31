---
layout: post
title: leetcode 657. Judge Route Circle
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://leetcode.com/problems/judge-route-circle/description/)

## 문제

```
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:

Input: "UD"
Output: true

Example 2:

Input: "LL"
Output: false
```

---

## 풀이코드

- 풀이 1
```python
def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    location = [0, 0]
    for direction in moves:
        if direction == "R":
            loaction[1] += 1
        if direction == "L":
            loaction[1] -= 1
        if direction == "U":
            loaction[0] += 1
        if direction == "D":
            loaction[0] -= 1
    return True if location.count(0) == 2 else False
```

- 풀이 2
```python
def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    location = [0, 0]
    dic = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [1, 0],
        "D": [-1, 0]
    }
    for direction in moves:
        location = [a+b for a, b in zip(location, dic[direction])]
    return True if location.count(0) == 2 else False
```

## 다른사람풀이
- 간단하다! 앞으로는 좀 쉽게 생각해보자

```python
def judge_circle(moves):
    """
    :type moves: str
    :rtype: bool
    """
    return moves.count("U")==moves.count("D") and moves.count("L")==moves.count("R")
```
