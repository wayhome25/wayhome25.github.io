---
layout: post
title: level 1. 핸드폰번호 가리기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1. 핸드폰번호 가리기
> [출처](http://tryhelloworld.co.kr/challenge_codes/133)

## 문제
```
별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다.
전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요
예를들어 s가 "01033334444"면 "*******4444"를 리턴하고, "027778888"인 경우는 "*****8888"을 리턴하면 됩니다.
```


## 풀이 (python)

```python
#풀이 1 - slice 활용
def hide_numbers(s):
    return (len(s)-4)*'*'+s[-4:] # slice 시간복잡도 O(N)

# 풀이 2
def hide_numbers(s):
    return s.replace(s[:-4], '*'*(len(s)-4))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
```


## 다른사람 풀이

```python
def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    return "*"*(len(s)-4) + s[-4:]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));
```

## 배운점

- 문제를 풀면 바로 풀이를 보지 말고, 더 효율적으로 접근하는 방법에 대해서 한번 더 고민해보자.
