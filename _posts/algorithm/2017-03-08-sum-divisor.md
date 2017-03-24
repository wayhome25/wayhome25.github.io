---
layout: post
title: level 1. 약수의 합
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 약수의 합
> [출처](http://tryhelloworld.co.kr/challenge_codes/2)

## 문제
어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요. 예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

## 풀이 (python)
```python
def sumDivisor(num):
    divisors = [num]
    t_num = int(num / 2)
    while t_num >=1:
        if num % t_num == 0:
            divisors.append(t_num)
        t_num -= 1
    return sum(divisors)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))
```

## 다른사람 풀이
```python
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
```

## 배운점
- sum() 함수를 통해 배열의 모든 요소를 더할 수 있다.
