---
layout: post
title: level 4. 숫자의 표현
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---
> [문제출처](http://tryhelloworld.co.kr/challenge_codes/41)

## 문제
수학을 공부하던 민지는 재미있는 사실을 발견하였습니다. 그 사실은 바로 연속된 자연수의 합으로 어떤 숫자를 표현하는 방법이 여러 가지라는 것입니다. 예를 들어, 15를 표현하는 방법은
(1+2+3+4+5)
(4+5+6)
(7+8)
(15)
로 총 4가지가 존재합니다. 숫자를 입력받아 연속된 수로 표현하는 방법을 반환하는 expressions 함수를 만들어 민지를 도와주세요. 예를 들어 15가 입력된다면 4를 반환해 주면 됩니다.

## 풀이

```python
def expressions(num):
    answer = 1
    for i in range(1,num//2+1):
        test_sum = i
        for j in range(i+1, num//2+2):
            test_sum += j
            if test_sum > num:
                continue
            if test_sum == num:
                answer += 1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
```

## 다른사람 풀이

```python
def expressions(num):
    answer = 0
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));
```

## 배운점
- for문의 중첩보다 for문 안에 while문을 사용하면 속도가 더 빠른 것 같다.
