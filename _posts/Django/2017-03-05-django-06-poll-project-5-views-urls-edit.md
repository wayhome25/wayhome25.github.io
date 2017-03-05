---
layout: post
title: django 06. 두번째 장고앱 5 - views.py 및 urls.py 수정 2
category: Django
tags: [python, 파이썬, Django]
comments: true
---
# django 06. 두번째 장고앱 5 - views.py 및 urls.py 수정 2
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       



## urls.py 수정
- 프로젝트 폴더의 urls.py 가 아닌, include 시킨 앱 폴더 내의 urls.py 를 수정한다.

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 숫자로 이루어진 question_id를 매개변수로 저장해서 views.py에 넘긴다
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

## views.py 수정

- function based view : url을 views의 메소드와 연결하는 것
- 다음 시간에 class based view에 대해서 알아본다.

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello, siwa')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id): #question_id를 파라미터로 받는다.
    return HttpResponse("You're looking at the results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
```

<center>
<figure>
<img src="/assets/post-img/django/views.png" alt="views">
<figcaption>url-views 연결 화면</figcaption>
</figure>
</center>
