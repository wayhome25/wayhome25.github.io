---
layout: post
title: Django 기본 02 - 파이썬 정규표현식, URLConf
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# 정규표현식 (Regular Expression)

- 대부분의 개발 언어에서 지원
- 문자열 검색, 치환을 간편하게 처리
- 파이선3 는 `re`라는 모듈을 통해서 지원 - [라이브러리](https://docs.python.org/3/library/re.html)  

## 정규표현식 예시
- `^(시작)`, `$(끝)`을 사용하여 해당 패턴에 완전히 일치하는 것만 찾을 수 있다.
- `r(raw)` 로 시작하여 이스케이프 문자를 한번 더 쓰지 않아도 된다. 자동 이스케이핑

### 예시

```python
r"[0-9]{1,3}" or r"\d{1,3}" # 최대 3자리 숫자
r"010[1-9]\d{6,7}" #10자리 혹은 11자리 휴대폰번호
r"[ㄱ-힣]{2,3}" # 한글이름 2글자 혹은 3글자
r"이[ㄱ-힣]{1,2}" # 성이 "이"인 이름
```

### 1글자 패턴 예시

```python
r"[0,1,2,3,4,5,6,7,8,9]" or r"[0-9]" or r"\d" # 숫자 1글자
r"[a-z]" # 소문자 1글자
r"[A-Z]" # 대문자 1글자
r"[a-zA-Z]" # 대소문자 1글자
r"[ㄱ-힣]" # 한글 1글자
```

### 반복횟수 지정

```python
r"\d?" # 숫자 0회 또는 1회 (있거나 없거나)
r"\d*" # 숫자 0회 이상
r"\d+" # 숫자 1회 이상
r"\d{m}" # 숫자 m 글자
r"\d{m,n}" # 숫자 m글자 이상 n글자 이하 (m~n)
```

## (참고) ipython 설치 및 실행
- python을 터미널에서 사용할때 편리한 프로그램

```shell
$ pip3 install "ipython[notebook]" # 설치
$ ipython # 실행
$ python3 -m  IPython # 위 명령어로 동작하지 않을 경우
```

## 정규표현식 참고자료
- [regexr](http://regexr.com/) : 연습하기 좋은 사이트
- [tryhelloworld](http://tryhelloworld.co.kr/courses/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D) : 간단한 정규표현식 강의


----

# URLConf
- settings.py에 최상위 URLConf 모듈을 지정
- 특정 URL과 뷰 매핑 list
- Django 서버로 Http 요청이 들어올 때마다, URLConf 매핑 List 를 처음부터 끝까지 순차적으로 훝으며 검색
- 매칭되는 URL Rule 을 찾지못했을 경우, 404 Page Not Found 응답을 발생

```python
# settings.py
ROOT_URLCONF = 'mysite.urls' # 프로젝트/urls.py 파일
```

## URLConf 정규표현식 매핑

### 예시1

```python
# urls.py
url(r'^sum/(?P<x>\d+)/$', views.mysum)

# views.py
def mysum(request, x):
  return HttpResponse(int(x))
```

- `(?P)` : 이 영역의 문자열에 정규표현식을 적용해서
- `\d+` : \d+ 패턴에 부합된다면
- `<x>` : x 라는 변수명으로 인자를 view.sum 으로 넘기겠다.
- 인자로 넘겨받은 값들은 모두 문자열 타입


### 예시2

```python
# 인자 2개
url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum)

# views.py
def mysum(request, x, y):
return HttpResponse(int(x) + int(y))

# 인자 3개
url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum)
# views.py
def mysum(request, x, y, z):
    return HttpResponse(int(x) + int(y) + int(z))

# 하나의 뷰에 3개의 url 연결
url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum)
url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum)
url(r'^sum/(?P<x>\d+)/$', views.mysum)
# views.py
def mysum(request, x, y=0, z=0):
  return HttpResponse(int(x) + int(y) + int(z))
```

### 예시3

```python
# 인자가 여러개인 경우
url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum)

# views.py
def mysum(request, numbers):
    return HttpResponse(sum(map(int,numbers.split('/'))))

# 나이, 이름 인자 받기
url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)$', views.hello)

# views.py
def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요'.format(name,age))
```
