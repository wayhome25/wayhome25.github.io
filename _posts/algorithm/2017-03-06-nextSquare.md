---
layout: post
title: level 1. 정수제곱근판별하기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 정수제곱근판별하기
> [출처](http://tryhelloworld.co.kr/challenge_codes/121)

## 문제
nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.

## 풀이 (python)
```python
# 풀이 1
import math
def nextSqure(n):
    return pow(math.sqrt(n)+1, 2) if int(math.sqrt(n)) == math.sqrt(n) else 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));

# 풀이 2
def nextSqure(n):
    for i in range(1,n//2):
        if i * i == n:
            return (i + 1) ** 2
        if i * i > n:
            return 'no'

# 풀이 3
def nextSqure(n):
    t = int(pow(n, 0.5))
    return (t+1)**2 if t**2==n else 'no'

# 참고 - 제곱근을 구하는 여러가지 방법
# n ** 5
# pow(n, 0.5)
# math.sqrt(n)
```

## 다른사람 풀이

```python
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
```

```python
def nextSqure(n):
    sqrt = pow(n, 0.5)
    return pow(sqrt + 1, 2) if sqrt == int(sqrt) else 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
```

## 배운점
- 파이썬 삼항 연산자 (conditional expressions)을 활용하니 짧게 코드를 짤 수 있었다.
- 제곱근을 구하려면 `import math` 를 통해서 모듈을 임포트하고 `math.sqrt()` 함수를 통해서 제곱근을 구할 수 있다.
- int() 를 통해서 주어진 인수를 정수로 변환할 수 있다.
- `pow(4,2)`과 `4 ** 2` (=16) 을 통해서 제곱 연산을 할 수 있다.
- 반대로 `pow(4,0.5)`과 `4 ** 1/2` (=2) 을 통해서 제곱근을 구할 수 있다.
