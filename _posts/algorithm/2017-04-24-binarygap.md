---
layout: post
title: codility - BinaryGap (시간복잡도 평가 추가)
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/
tags: [알고리즘, 프로그래밍]
comments: true
---

> [문제출처](https://codility.com/programmers/lessons/1-iterations/)

## 문제

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)

**that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.**

Assume that:

N is an integer within the range [1..2,147,483,647].

Complexity:

**expected worst-case time complexity is O(log(N));

expected worst-case space complexity is O(1).**

## 풀이과정
- 함수의 인자로 받은 N을 2진수로 바꾼다
- 2진수 N의 각 자릿수 중에 1에 해당하는 자릿수의 인덱스 값을 찾아 빈 배열에 담는다.
- 배열에 담긴 요소를 인접한 요소와 뺀 결과를 새로운 빈 배열에 담는다.
- 그중에서 최댓값을 리턴한다.

## 풀이코드

```python
def solution(N):
    N = bin(N)[2:] # 함수의 인자로 받은 N을 2진수로 바꾼다, format(N, 'b') 도 가능
    arr = []

    for idx, value in enumerate(N):
        if value == '1':
            arr.append(idx) # 2진수 N의 각 자릿수 중에 1에 해당하는 자릿수의 인덱스 값을 찾아 빈 배열에 담는다.

    arr2 = []    

    for i in range(len(arr)-1):
        arr2.append(arr[i+1] - arr[i] - 1) # 배열에 담긴 요소를 인접한 요소와 뺀 결과를 새로운 빈 배열에 담는다.

    return max(arr2) # 그 중에서 최댓값을 리턴한다.
```

### Big-O
- (1) ~ (9)를 더하면 `5N + 4` Big-O 로 표현하면 O(N)

```python
def solution(N):
    N = bin(N)[2:] # (1) Big-O : constant 1
    arr = [] # (2) Big-O: constant 1

    for idx, value in enumerate(N): # (3) Big-O: N
        if value == '1': # (4) Big-O: N
            arr.append(idx) # (5) Big-O: N

    arr2 = [] # (6) Big-O: constant 1    

    for i in range(len(arr)-1): # (7) Big-O : N
        arr2.append(arr[i+1] - arr[i] - 1) # (8) Big-O: N

    return max(arr2) # (9) Big-O: constant 1
```

## 다른 사람 코드
- Big-O : O(N)

```python
#1
def solution(N):
  return len(max(bin(N)[2:].strip('0').strip('1').split('1'))) # Big-O : N

#2
def solution(N):
  return len(max(format(N, 'b').strip('0').split('1'))) # Big-O : N  
```

---

### .strip() / .split()
- str.strip() 메소드를 활용하여 문자열 양 끝에서 원하는 연속된 문자열을 삭제할 수 있다.

```python
# 2진수 '100100010000' 의 경우,

'100100010000'.strip('0')
# '10010001'
# 좌, 우 끝의 모든 연속된 0을 삭제

'100100010000'.strip('0').strip('1')
# '001000'
# 좌,우 끝의 모든 연속된 1을 삭제

'100100010000'.strip('0').strip('1').split('1')
# ['00', '000']
# 1을 기준으로 문자열을 나눠 배열에 담는다
```

## 시간 복잡도 측정 (time complexity)
- [참고자료-추천](http://www.hanbit.co.kr/network/category/category_view.html?cms_code=CMS5648300711), [참고자료](http://www.mydiyworld.net/?p=440),
- Big O  표기법은 컴퓨터 공학에서 알고리즘의 복잡도 또는 성능을 표현하기 위해 사용된다.  **Big O는 특히 최악의 경우를 표현하며**, 특정 알고리즘을 수행하는데 특정 시간안에 수행된다는 것을 보장한다는 의미를 가진다.
- Bio 표기법 종류 (상세 내용은 자료 참고)
  - O(1), O(N), O(N^2), O(2^N), O(log N), O(N log N)
  - 이진 탐색 같은 알고리즘은 O(log N)의 성능을 가지며 대용량의 데이터를 처리하는데 아주 효율적이다.
- 알고리즘의 계산복잡도를 결정하는 요소는 크게 네 가지로 구분할 수 있다.
  -	단순 반복문(루프)
  -	재귀호출
  -	테스트 문(IF, WHILE, 또는 UNTIL)
  -	함수의 호출
- **반복문의 계산복잡도는** 반복되는 횟수를 통해 쉽게 구할 수 있고, 입력값의 수에 대해 항상 일정하고, **입력되는 값에 좌우되지 않는다**.
  (각 명령이 끝날 때마다 실행 횟수를 적고 더한 후, 상수는 생략하고 최고차항만 고려한다.)
- 반면에 재귀호출이나 테스트 문의 경우에는 새로운 문제를 야기시키는데, 입력되는 값이 따라 계산 복잡도가 바뀌는 것이다. 일반적으로 세 가지 경우를 생각한다. Best Case, Average Case, Worst Case가 그것이다.
