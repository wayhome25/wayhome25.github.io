---
layout: post
title: level 1. 같은 숫자는 싫어
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 1.같은 숫자는 싫어
> [출처](http://tryhelloworld.co.kr/challenge_codes/86)

## 문제
no_continuous함수는 스트링 s를 매개변수로 입력받습니다.

s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.
예를들어 다음과 같이 동작하면 됩니다.

s가 '133303'이라면 ['1', '3', '0', '3']를 리턴
s가 '47330'이라면 [4, 7, 3, 0]을 리턴

## 풀이 (python)
### 1
```python
def no_continuous(s):
    result = []
    for i, v in enumerate(s):
        if i == 0:
            result.append(v)
        elif s[i-1] == v:
            continue
        else:
            result.append(v)
    return result
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
```

### 2
list comprehension을 활용하여 코드 길이를 줄였다.

```python
def no_continuous(s):
    # 함수를 완성하세요
	return [v for i, v in enumerate(s) if i==0 or s[i-1] != s[i]]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
```


## 배운점
- `enumerate()` : 순서가 있는 자료형 (리스트, 튜플, 문자열)을 입력으로 받아 인텍스 값을 포함하는 enumerate 객체를 리턴한다.
