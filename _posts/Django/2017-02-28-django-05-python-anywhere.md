---
layout: post
title: django 05. python anywhere를 이용한 쉬운 배포
category: Django
tags: [python, 파이썬, Django, 배포, python anywhere]
comments: true
---
# django 05. python anywhere 를 이용한 쉬운 배포
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       
https://www.pythonanywhere.com/

## 설치전 요구사항
- 로컬에 git 또는 sourceTree 설치하기
- github 계정 생성
- 로컬 프로젝트 github 에 업로드
- 참고 강좌
    - https://opentutorials.org/course/1492
    - https://backlogtool.com/git-guide/kr/

## pythonanywhere 회원가입
이메일만으로 쉽게 가입 가능

## bash 실행
```
$ git clone https://github.com/honux77/lotto-web
$ tree lotto-web
```

## virtualenv 설정
```
$ virtualenv --python=python3.5 lottoenv
$ source lottoenv/bin/activate
$ pip install django==1.10 whitenoise
```

## 서버 설정
```
$ cd lotto-web
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py createsuperuser
```

## web - virtualenv 설정
```
/home/<your-username>/<your-project-folder>/
```


## web - WSGI 설정
```
import os
import sys

path = '/home/<your-username>/<your-project-folder>/'  
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
```

## secret key 생성
```
$ python genkey.py
```
- 코드 내용

```python
"""
Pseudo-random django secret key generator.
- Does print SECRET key to terminal which can be seen as unsafe.
"""

import string
import random

# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

print(SECRET_KEY)
```

## settings.py 수정
```
DEBUG=False
ALLOWED_HOST=[honux.pythonanywhere.com]
SECRET_KEY= '....'
```
