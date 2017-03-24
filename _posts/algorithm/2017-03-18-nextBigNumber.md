---
layout: post
title: level 3. 다음 큰 숫자
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
> [출처](http://tryhelloworld.co.kr/challenge_codes/173)

## 문제
어떤 수 N(1≤N≤1,000,000) 이 주어졌을 때, N의 다음 큰 숫자는 다음과 같습니다.

N의 다음 큰 숫자는 N을 2진수로 바꾸었을 때의 1의 개수와 같은 개수로 이루어진 수입니다.
1번째 조건을 만족하는 숫자들 중 N보다 큰 수 중에서 가장 작은 숫자를 찾아야 합니다.
예를 들어, 78을 2진수로 바꾸면 1001110 이며, 78의 다음 큰 숫자는 83으로 2진수는 1010011 입니다.
N이 주어질 때, N의 다음 큰 숫자를 찾는 nextBigNumber 함수를 완성하세요.

## 풀이 (python)
```python
def nextBigNumber(n):
    num_of_one = str(bin(n)).count('1')
    for i in range(n+1,1000001):
        if str(bin(i)).count('1') == num_of_one:
            return i


#아래 코드는 테스트를 위한 출력 코드입니다.
print(nextBigNumber(78))
```

## 풀이과정
1. 인자 N을 2진수로 변환
2. 1의 갯수를 확인
3. 10진수 N < x <= 1,000,000 사이의 숫자를 하나씩 2진수로 바꾸어 1의 갯수가 위의 2와 같다면, x를 리턴한다.


## 배운점
- bin(), oct(), hex() 내장함수를 통해 정수를 각 2진수, 8진수, 16진수로 바꿀 수 있다.
- str() 내장함수를 통해 인자를 문자열로 변환한다.
- str.count('검색어')를 통해서 해당 검색어의 갯수를 리턴한다.
