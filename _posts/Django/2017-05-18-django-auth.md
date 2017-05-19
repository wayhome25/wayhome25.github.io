---
layout: post
title: 사용자 인증 (django.contrib.auth)
category: Django
tags: [python, Django, 인증]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.

# django.contrib.auth 앱을 통한 회원가입/로그인/로그아웃

## 인증 관련 기본설정
- [global settings](https://github.com/django/django/blob/1.10.6/django/conf/global_settings.py)에 정의된 인증관련 기본 설정
- 위치 : django/django/conf/global_settings.py

```python
from django.conf import settings # << 해당 위치의 global settings 내용
# local settings.py에서 오버라이딩 가능

# 기본 로그인 페이지 URL 지정
# login_required 장식자 등에 의해서 사용
LOGIN_URL = '/accounts/login/'

# 로그인 완료 후 next 인자가 지정되면 해당 URL 페이지로 이동
# next 인자가 없으면 아래 URL로 이동
LOGIN_REDIRECT_URL = '/accounts/profile/'

# 로그아웃 후에 next 인자기 지정되면 해당 URL 페이지로 이동
# next 인자가 없으면 LOGOUT_REDIRECT_URL로 이동
# LOGOUT_REDIRECT_URL이 None(디폴트)이면, 'registration/logged_out.html' 템플릿 렌더링
LOGOUT_REDIRECT_URL = None

# 인증에 사용할 커스텀 User 모델 지정 : '앱이름.모델명'
AUTH_USER_MODEL = 'auth.User'
```

## 인증 관련 주요 모델필드
- 위치 : django/django/contrib/auth/models.py

```python
class AbstractBaseUser(models.Model):
    password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	...

class PermissionsMixin(models.Model):
    is_superuser = models.BooleanField(default=False)
	...

class AbstractUser(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=150, unique=True)
	first_name = models.CharField(max_length=30, blank=True)  
	last_name = models.CharField(max_length=30, blank=True)
	email = models.EmailField(blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False) # 로그인 허용 여부
	date_joined = models.DateTimeField(default=timezone.now)

class User(AbstractUser): # 우리가 사용하는 User 모델
	...

class AnonymousUser: # 로그아웃 유저를 표현하는 클래스 (모델아님)
	...

```

## AbstractUser 클래스 주요 속성, 멤버함수
- .is_authenticated : 로그인여부 (속성)
- .is_anonymous : 로그아웃 여부 (속성)
- .set_password(raw_password) : 지정 암호를 암호화해서 password 필드에 저장 (save함수 호출 안함)
- .check_password(raw_password) : 암호비교
- .set_unusable_password() : 로그인 불가 암호로 세팅 (암호를 통한 로그인X, 외부인증 OAuth에 의한 유저일 경우)
- .has_unusable_password() : 로그인 불가 암호 설정여부


---

# User 모델 클래스 획득 방법 (중요)

### 직접 User 모델 import (비추)
- global settings 오버라이딩을 통해서 인증 User 모델을 다른 모델로 변경할 수 있음

```python
from django.contrib.auth.models import User

User.objects.all()
```

### `get_user_model` helper 함수를 통해 모델 클래스 참고 (추천)

```python
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.all()
```

### `settings.AUTH_USER_MODEL` 을 통한 모델클래스 참조 (추천)

```python
from django.conf import settings # 추천!
from django.conf.auth.models import User # 비추
from django.db import models

class Post(models.Model):
	author = models.ForeignKey(User) 		# 비추
	author = models.ForeignKey('auth.User') # 비추
	author = models.ForeignKey(settings.AUTH_USER_MODEL) # 추천!
```


## 뷰 에서 현재 로그인 유저 획득하는 방법  
1. FBV : request.user
2. CBV : self.request.user
- 로그인 상태 :settings.AUTH_USER_MODEL 클래스 인스턴스  
- 로그아웃 상태 :django.contrib.auth.models.AnonymousUser 클래스 (모델 인스턴스가 아님, 다른 모델과 관계 불가능)
- context_processor를 통해서 user가 모든 view에 context로 기본 제공 됨
