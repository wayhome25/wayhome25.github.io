---
layout: post
title: level 2. JadenCase 문자열 만들기
category: 알고리즘 문제풀이
permalink: /algorithm/:year/:month/:day/:title/

tags: [알고리즘, 프로그래밍]
comments: true
---
# level 2. JadenCase 문자열 만들기
> [출처](http://tryhelloworld.co.kr/challenge_codes/124)

## 문제
Jaden_Case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 "3people unFollowed me for the last week"라면 "3people Unfollowed Me For The Last Week"를 리턴하면 됩니다.

## 풀이 (python)
```python
def Jaden_Case(s):
    s = s.lower()
	list_s = s.split()
	list_s = [i.replace(i[0], i[0].upper(), 1) for i in list_s]
	return ' '.join(list_s)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
```

## 다른사람 풀이
```python
def Jaden_Case(s):
    return s.title()
```
## 배운점
- String.split() 을 통해서 문자열을 리스트로 바꾼다.
- ' '.join(List) 를 통해서 리스트를 문자열로 바꾼다.
- String.replace(old, new, 숫자) 를 통해서 문자열 안의 값을 바꿀 수 있다. 숫자 조건을 입력하면 그 숫자 만큼만 변경한다.
- String.title() 을 통해서 문자열 각단어의 첫 글자를 대문자로 바꾼다.
