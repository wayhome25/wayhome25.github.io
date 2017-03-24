---
layout: post
title: level 1. 가운데 글자 가져오기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 가운데 글자 가져오기
> [출처](http://tryhelloworld.co.kr/challenge_codes/83)

## 문제
getMiddle메소드는 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요. 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.

## 풀이 1 (python)  
```python
def string_middle(str):
    if len(str) % 2:
        return str[len(str) // 2]
    else:
        return str[(len(str) // 2) -1 : len(str) // 2 + 1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))
```
## 풀이 2 (python) - 3항 연산자 활용
```python
def string_middle(str):
    t = len(str) // 2
    return str[t] if len(str) % 2 else str[t -1 : t + 1]
```


## 배운점
- 슬라이싱 [처음 : 끝] 에서 `끝`에 해당하는 인덱스 값은 포함되지 않는다.   
  (처음 <= 원하는 값 < 끝)
- python의 3항 연산자: a if test else b (test 가 참이면 a 거짓이면 b 반환)
