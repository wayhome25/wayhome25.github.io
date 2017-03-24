---
layout: post
title: level 2. 자연수를 뒤집어 리스트로 만들기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 2. 자연수를 뒤집어 리스트로 만들기
> [출처](http://tryhelloworld.co.kr/challenge_codes/117)

## 문제
digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.

## 풀이 (python)
```python
def digit_reverse(n):
    list = [int(i) for i in str(n)]
    list.reverse()
    return list

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(digit_reverse(12345)));
```

## 다른사람 풀이
```python
# 풀이1
def digit_reverse(n):
    return [int(i) for i in str(n)][::-1]

# 풀이2
def digit_reverse(n):
    return list(map(int, reversed(str(n))))    
```

## 배운점
- .reverse() 메소드를 통해서 리스트 요소의 순서를 뒤집을 수 있다. 하지만 결과값을 리턴하지는 않는다.
- map(function, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴한다.
- reversed() 함수를 통해 리스트 요소의 순서를 뒤집은 객체를 리턴한다.
