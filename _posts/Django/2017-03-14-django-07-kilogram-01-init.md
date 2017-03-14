---
layout: post
title: django 07. 세번째 장고앱 01 - 기본 설정 및 프로젝트 초기화
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)

> 세번째 장고앱 '킬로그램'을 시작하기 위한 기본 설정 및 프로젝트 초기화를 진행한다.

# 기획
- 앱이름: 킬로그램
- 유사 OOO그램: 이미지 업로드 앱

# 사용자 시나리오
- 회원 가입 및 로그인 기능
- 소셜 로그인도 가능(?)
- 비회원 열람 불가 - 공개된 인기 이미지
- 회원 전용 페이지 - 내 이미지와 친구들 이미지 보기
- 하트 주기
- 댓글 달기

# 핵심 기능
- `인증`
- `이미지 업로드`

# 페이지들
- 메인페이지: 인기 이미지들 보여주기
- 마이페이지: 로그인한 사용자에게 내 이미지들 보여주기
- 친구찾기 및 친구추가 페이지:

-----

# 기본 설정 및 프로젝트 초기화

## start project and app
- 프로젝트명을 mysite로 만들고 나서 app3로 변경한다.
- 처음부터 app3로 만들지 않는 이유는, 프로젝트 폴더 내에 대표 폴더가 같은 폴더명 mysite로 생성이 되는데 그게 편하기 때문이다.

```
/*프로젝트 생성*/
$ django-admin startproject mysite
/*폴더명 변경*/
$ mv mysite app3
/*앱 생성*/
$ python manage.py startapp kilogram
```

## settings.py 수정
- INSTALLED_APPS에 kilogram 앱을 추가하는데, 위치는 admin 위에 추가해야한다.
- LANGUAGE_CODE, TIME_ZONE을 수정한다.
- STATIC_ROOT를 통해 Static file 경로를 추가한다.

```
INSTALLED_APPS = [
    'kilogram',


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

- shell에서 migrate 진행

```shell
$ python manage.py migrate
```

## super user 생성

```shell
$ python manage.py createsuperuser
```

## model

아직까지는 특별히 생성 또는 수정할 model이 없다.

## kilogram/urls.py 생성

- `include` 방식으로 kilogram (앱폴더) 내에 `urls.py` 를 따로 작성한다.
  - **이 방법이 더 좋다.**
- 앱 폴더, 프로젝트 폴더 내부 각각에 `urls.py`를 갖는다.
- `app_name` 네임스페이스를 지정하여 url name 중복 문제를 해결한다.
- FBV(function based view) 보다 CBV(Class based view)에서 이미 정의되어 있는 `generic view`를 활용하는 것이 편리하다.

```python
from django.conf.urls import url
from . import views

app_name = 'kilogram'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    # /kilogram 으로 접속시 (include 됨)
    # CBV의 generic view를 이용하여 url을 처리하겠다는 말
]
```

## mysite/urls.py 수정

- 파이썬 기본 문법인 `as`를 적용해서 `views를 구별` 가능하도록 한다.
- `include` 할 urls.py 의 경로와 url 패턴을 지정한다.

```python
from django.conf.urls import url, include
from django.contrib import admin
from kilogram import views as kilogram_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kilogram_views.IndexView.as_view(), name = "root"),
    url(r'^kilogram/', include('kilogram.urls')),
]
```

## kilogram/views.py 수정

- 간단히 템플릿을 적용하기 위해서 generic view인 `TemplateView`를 사용했습니다.
  - 아무 기능 없이 템플릿을 그대로 표시해준다.

```python
from django.views.generic.base import TemplateView

class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'kilogram/index.html'
```

## 기본 템플릿 작성
- `템플릿 경로`(앱 폴더 내) : kilogram/templates/kilogram/

### base.html (kilogram/base.html)

```html
{% raw %}
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Kilogram</title>

  <!-- Bootstrap -->
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

  {% load static %}
  <link rel="stylesheet" type="text/css" href="{% static 'kilogram/style.css' %}" />

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body>
  <nav class="navbar navbar-default navbar-static-top">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="{% url 'kilogram:index' %}"> <span class="glyphicon glyphicon-camera"> </span> Kilogram </a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#"> <span class="glyphicon glyphicon-user"></span> Login</a></li>
        <li><a href="#">Logout</a></li>
        <li><a href="{% url 'admin:index' %}">Admin</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
  <div class="container">
    <div>
      {% block content %}
      {% endblock %}
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>
</html>
{% endraw %}
```

### index.html (kilogram/index.html)
- base.html 템플릿을 확장하여 작성

```html
{% raw %}
{% extends 'kilogram/base.html' %}
{% block content %}

<h1>Kilogram Main Page</h1>

{% endblock %}
{% endraw %}
```
