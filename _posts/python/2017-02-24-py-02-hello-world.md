---
layout: post
title: 파이썬 파트2. 변수와 계산
category: python
tags: [python, 파이썬]
comments: true
---
# 파트2. 파이썬 변수와 계산
> [try hello world 파이썬 입문 강의 ](http://tryhelloworld.co.kr/courses/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%AC%B8)      

## tip - 파이썬 한글입력 에러 문제

### IDLE
- [active state](http://www.activestate.com/activetcl/downloads) 접속
- `8.5.*` 최신버전 설치 (최신버전은 8.6이지만 파이썬이 사용하는 패키지는 8.5버전이라 8.5로 설치해야 한다.)
- IDLE 다시 실행 후 한글 입력되는 부분 확인

### 터미널
- .py 파일 실행시 python이 아닌 `python3 파일명.py` 로 입력하여 실행


## 주석
```python
# 파이썬 주석은 이렇게 작성합니다.

"""
여러줄 주석은
이렇게
작성해요
"""
```

## 변수 - 작성기본
```python
name = 'siwa'
hobby = '달리기'
```

## 변수 - 문자, 숫자
### 문자 변수
```python
name = '몽키'
# 텍스트 두개를 더하면 문자열이 이어붙여짐
nick_name = '초보' + '몽키' # 초보몽키
```
### 숫자 변수
```python
my_age = 2
my_age + 1 # 3 - 더하기
my_age * 3 # 6 - 곱하기
my_age / 2 # 1 - 나누기
my_age ** 10 # 1024 - 거듭제곱
my_age % 2 # 0 - 나머지
```
