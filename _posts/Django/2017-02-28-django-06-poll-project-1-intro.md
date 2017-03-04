---
layout: post
title: django 06. 두번째 장고앱 1 - 셋업 및 urls.py와 views.py 수정
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 06. 두번째 장고앱 1 - 셋업 및 urls.py와 views.py 수정
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       


## 사전준비 - 프로젝트 및 앱 생성
> [사전준비 상세내용](https://wayhome25.github.io/django/2017/02/28/django-03-lotto-project-1/)

1. 가상환경 설치 (virtualenv)
2. 가상환경 실행
3. 설치된 패키지 확인 및 장고 설치 (pip)
4. 프로젝트 생성 ($ django-admin startproject 프로젝트 이름)
5. settings.py 수정 (TIME_ZONE, LANGUAGE_CODE, INSTALLED_APPS)
6. app 생성 ($ django manage.py startapp 앱 이름)
7. 서버실행 - 특정 포트번호로 실행 가능 (python manage.py runserver 8080)

## urls.py와 views.py 테스트 등록
> 첫번째 실습과 다른 방식으로 urls.py 를 설정한다 - Including another URLconf

- 프로젝트 폴더 (myapp) 내의 urls.py 내용을 앱폴더 (polls) 에 복사

```python
from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
- 프로젝트 폴더 (myapp) 내의 urls.py 내용 수정 - Including another URLconf

```python
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    #polls 로 시작하는 url은 polls의 urls 로 처리해라
]
```
