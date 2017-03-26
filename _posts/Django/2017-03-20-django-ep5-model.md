---
layout: post
title: Django 기본 05 - 모델(Model), 모델필드, 필드옵션
category: Django
tags: [python, Django, 모델, 필드옵션]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# 장고 모델

- 뷰(view) 함수에서 데이터베이스에 어떤 작업을 요청할 때는 SQL 구문이 필요하다.

## SQL(Structured Query Language)
- Query: 정보수집에 대한 요청에 쓰이는 컴퓨터 언어
- SQL : 관계형 데이터베이스 관리 시스템(Relational Database Management System)의 데이터를 관리하기 위해 설계된 특수목적의 프로그래밍 언어
- RDBMS의 종류 : MySQL, MariaDB, PostgreSQL
- 장고 모델은 관계형 데이터베이스 (RDBMS)만을 지원
- 장고 모델을 통해 SQL을 생성/실행 (ORM)

## Django Model
- 장고 내장 ORM
- ORM의 역할 : SQL을 직접 작성하지 않아도 장고 모델을 통해 데이터베이스로 접근한다. (조회/추가/수정/삭제)
- `(중요)` SQL을 몰라도 된다는 것은 아니다. 최소한 내가 작성한 코드가 어떤 SQL을 만들어내는지는 검증할 수 있어야 한다.
- 보통 하나의 장고 프로젝트에서 하나의 DB를 사용한다.
- 파이썬 클래스 와 데이터베이스 테이블을 매핑
  - Model : DB 테이블과 매핑
  - Model Instance : DB 테이블의 1 Row

---

# 장고 커스텀 모델 정의
- 위치 : 특정앱/models.py
- 데이터베이스 테이블 구조/타입을 먼저 설계를 한 다음에 모델을 정의한다.
- 모델 클래스명은 단수형을 사용한다. (Posts가 아니라 Post)

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100) # 길이 제한이 있는 문자열
    content = models.TextField()             # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동저장
    # DB에서는 길이제한 유무에 따라서 문자열 필드타입이 다른다.
    # 길이 제한이 없는 문자열을 많이 쓰면 성능이 좋지 않다.
```

## 모델 등록절차
1. models.py 에서 모델클래스 정의 (상기코드 참고)
2. shell에서 migrations, migrate 실행
3. admin.py에 모델클래스 등록

```shell
# 2. shell에서 migrations, migrate 실행
$ python3 manage.py makemigrations
$ python3 manage.py migrate
# 위 명령을 통해서 앱폴더 아래에 migration 폴더가 생성되고 DB에 테이블을 생성한다.
```

```python
# 3. admin.py에 모델클래스 등록
# 앱폴더/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

## 지원하는 모델필드 타입
- [가이드 문서](https://docs.djangoproject.com/es/1.10/ref/models/fields/#field-types)
- 주요 Field Types : AutoField, BooleanField, CharField, DateTimeField, FileField, ImageField,TextField
- 주요 Relation ship Types : ForeignKey, ManyToManyField, OneToOneField

## 주요 Field Option
- `필드옵션` : 필드마다 고유 옵션이 존재, 공통 적용 옵션도 있음
- null (DB 옵션) : DB 필드에 NULL 허용 여부 (디폴트 : False)
- unique (DB 옵션) : 유일성 여부 (디폴트 : False)
- blank : 입력값 유효성 (validation) 검사 시에 empty 값 허용 여부 (디폴트 : False)
- default : 디폴트 값 지정. 값이 지정되지 않았을 때 사용
- verbose_name : 필드 레이블. 지정되지 않으면 필드명이 쓰여짐
- validators : 입력값 유효성 검사를 수행할 `함수`를 다수 지정
  - 각 필드마다 고유한 validators 들이 이미 등록되어있기도 함
  - 예 : 이메일만 받기, 최대길이 제한, 최소길이 제한, 최대값 제한, 최소값 제한 등
- choices (form widget 용) : select box 소스로 사용
- help_text (form widget 용) : 필드 입력 도움말  
- auto_now_add : Bool, True 인 경우, 레코드 생성시 현재 시간으로 자동 저장

## 커스텀 모델 예시
- max_length, verbose_name 등 주요 필드 옵션을 적용하였다.

```python
# 앱폴더/models.py
import re
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    title = models.CharField(max_length=100, help_text='최대 100자 내로 입력가능합니다.'
    choices = (
              ('제목1', '제목 1 레이블'),
              ('제목2', '제목 2 레이블'),
              ('제목3', '제목 3 레이블'),
    ))
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
        validators = [lnglat_validator], # 함수를 넘겨서 유효성 검사 실행
        help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
