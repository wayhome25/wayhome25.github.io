---
layout: post
title: level 2. 가장 긴 팰린드롬
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](http://tryhelloworld.co.kr/challenge_codes/85)

## 문제

앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
예를들어 s가 "토마토맛토마토"이면 7을 리턴하고 "토마토맛있어"이면 3을 리턴합니다.

## 풀이코드

```python
def longest_palindrom(s):
    list_s = list(s)
    if list_s == list_s[::-1]:
        return len(list_s)

    result = []
    for idx, item in enumerate(list_s):
        if item in list_s[idx+1:]:
            idx2 = list_s[idx+1:].index(item) + idx+2

            if list_s[idx:idx2] == (list_s[idx:idx2])[::-1]:
                result.append(len(list_s[idx:idx2]))

    if len(result) == 0:
        return 1
    return max(result)

print(longest_palindrom("토마토맛토마토")) # 7
print(longest_palindrom("토마토맛있어")) # 3
print(longest_palindrom("맛있어토마토")) # 3
```
