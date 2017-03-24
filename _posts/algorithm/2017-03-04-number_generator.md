---
layout: post
title: level 1. x만큼 간격이 있는 n개의 숫자
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. x만큼 간격이 있는 n개의 숫자
> [출처](http://tryhelloworld.co.kr/challenge_codes/135)

## 문제
number_generator함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.
[2,4,6,8,10]

4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.
[4,8,12]

이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.

## 풀이 (python)

### python

```python
def number_generator(x, n):
    # 함수를 완성하세요
    return list(range(x, x*n+1, x))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))
```
