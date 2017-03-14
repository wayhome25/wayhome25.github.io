---
layout: post
title: django 06. 두번째 장고앱 16 - 정적파일, 템플릿 확장, 어드민 템플릿 변경
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)

> static 파일관리와 템플릿 확장에 대해서 알아본다.

## 참고문서

- [가이드문서](https://docs.djangoproject.com/en/1.10/howto/static-files/)

# 정적파일

## css 파일 만들기

- polls/static/polls/style.css

```
a {
    color: red;
    text-decoration: none;
}

body {
    background: white url("images/background.gif") no-repeat right bottom;
}
```
## css 파일 적용

```html
{% raw %}
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
{% endraw %}
```

## settings.py 수정

```python
# collectstatic 명령 수행시 모든 static 파일을 static 폴더에 모아준다.
# 나중에 서버에 배포할때 정적 파일을 특정 디렉토리 아래에 묶어 놓을 수 있다.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

## collectstatic 명령 수행 및 변경사항 확인

```
$ python manage.py collectstatic
```

---------

# 어드민 템플릿 변경

## settings.py 수정

```python
INSTALLED_APPS = [
    'polls',  # 어드민 앞에 입력한다.
    'django.contrib.admin',
    # ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    }
]
```

## 장고 기본 디렉토리 확인

```bash
>>> import django
>>> print(django.__path__)
```

## polls/templates/admin/base_site.html 생성

- 원본 파일은 django/contrib/admin/templates 에 저장되어 있음

```html
{% raw %}
{% extends "admin/base.html" %}

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">투표 관리자</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
{% endraw %}
```

-----

# 템플릿 확장하기 (extends)

- templates/polls/base.html 생성

```
{% raw %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Django Polls Example</title>

  <!-- Bootstrap -->
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body>
  <div class="container">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <span class="navbar-brand">Polls Example</span>
        </div>
        <ul class="nav navbar-nav">
          <li><a href = "{% url 'polls:index' %}">투표</a></li>
          <li class="navbar-right"><a href = "{% url 'admin:index' %}">관리자</a></li>
        </ul>
      </div>
    </nav>
    <div>
      {% block content %}
      {% endblock %}
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js></script>
  </body>
  </html>
  {% endraw %}

```

## 나머지 페이지들 수정

```html
{% raw %}

{% extends 'polls/base.html' %}

{% block content %}
    <!--
        ohter html here
    -->
{% endblock content %}
{% endraw %}
```
