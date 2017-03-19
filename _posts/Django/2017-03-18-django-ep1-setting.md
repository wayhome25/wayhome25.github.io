---
layout: post
title: Django 기본 01 - 기본세팅, 휴대폰으로 접속하기
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [AskDjango](https://nomade.kr/vod/django) 수업을 듣고 중요한 내용을 정리하였습니다.


## One Project, Multi App 구조
- 장고 프로젝트 : **장고 프로젝트 rule** 에 따라, 파일/디렉토리 구성이 된 디렉토리
- 장고 앱 : **장고 앱 rule** 에 따라, 파일/디렉토리 구성이 된 디렉토리
- 하나의 장고 프로젝트에 다수의 장고 앱이 존재할 수 있다.

```shell
# 프로젝트 생성방법 1 - 최상위 디렉토리 명은 변경 가능하다. 프로젝트 폴더명은 변경하지 않는게 좋다. (변경시 설정 변경 필요)
$ django-admin startproject mysite
$ mv mysite django_project

# 프로젝트 생성방법 2 - django-admin 명령어를 사용할 수 없는 경우
$ python3 -m django startproject mysite

# 앱 생성방법 - 여러개 생성 가능
$ python3 manage.py startapp blog

$ python3 manage.py startapp shop
```

# App/URLConf/ View/Template

## urls.py
- 앱 디렉토리 생성 (상기 코드 참조)
- 앱을 프로젝트에 등록 (mysite/settings.py) : admin 위에 입력하는 것이 좋음

```python
INSTALLED_APPS = [
'blog',
# 생략
]
```

- 앱 폴더 내에 urls.py 파일 생성 후 프로젝트 urls.py와 연결

```python
# 프로젝트 폴더 urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]
# 앱 폴더 urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
]
```
- 개발 서버 돌리기 (계속 켜놓는게 편하다)

```shell
$ python3 manage.py runserver
```
## views.py

```python
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')
```

## template
- 경로 : blog/templates/blog/post_list.html
- 서버 실행후 작성한 template 디렉토리를 서버가 알게하는 방법
  - 서버 강제종료 (ctrl+c) 후 재실행

---

# 휴대폰 망을 통해 장고서버 접속하기

## ngrok
- [ngrok 사이트](https://ngrok.com/)
- Demo without deploying
- Simplify mobile device testing
- 사설 네트워크 안의 개발서버를 포트포워딩 등의 설정 없이도, 외부 네트워크에서 접속 가능하도록 한다.

<center>
 <figure>
 <img src="/assets/post-img/django/ngrok.png" alt="views">
 <figcaption>ngrok 구동방식</figcaption>
 </figure>
 </center>

## 설치 및 실행
### 설치
- ngrok를 [다운](https://ngrok.com/download), 압축을 풀어 ngrok 실행파일을 manage.py 가 존재하는 장고 프로젝트 경로로 복사

```shell
$ mv ~/Downloads/ngrok .
```

### 실행
- 장고 개발서버를 8000 포트로 (디폴트) 구동
- ngrok 실행 후 표시되는 http 주소로 휴대폰 브라우저 접속

```shell
# 서버구동
$ python3 manage.py runserver 8000
# ngrok 실행
$ ./ngrok http 8000
```
<center>
 <figure>
 <img src="/assets/post-img/django/ngrok_terminal.png" alt="views">
 <figcaption>ngrok 실행 - 해당 주소로 휴대폰으로 접속</figcaption>
 </figure>
 </center>

## settings.py 수정
- settings.py 의 ALLOWED_HOSTS 에 상기 주소를 입력하여 접속을 허용해야한다.
- `*` 을 입력하면 모든 도메인에 대해서 접속을 허용한다.

```python
# 서버는 여려개의 도메인을 가질 수 있는데, 그 중에 허용할 도메인을 입력
# ALLOWED_HOSTS = ['f1ee182d.ngrok.io']
ALLOWED_HOSTS = ['*'] # 모든 도메인에 대해서 허용
```

## (참고) 템플릿 모바일뷰 대응하기
- viewport meta : 배율 x 1.0 고정으로, 유저의 배율 조정을 막는다.

```html
<meta name="viewport" content="width=device-width,initial-scale=1.0,
                               minimum-scale=1.0,maximum-scale=1.0,
                               user-scalable=no" />
```
