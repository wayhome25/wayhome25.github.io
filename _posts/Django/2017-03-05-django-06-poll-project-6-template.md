---
layout: post
title: django 06. 두번째 장고앱 6 - template 연동
category: Django
tags: [python, 파이썬, Django, template]
comments: true
---
# django 06. 두번째 장고앱 6 - template 연동
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## templates 폴더 작성
- 폴더위치 (앱폴더 내부) : app2/polls/`templates/polls/index.html`
- index.html 작성

```html
{% raw %}
{% if latest_question_list %}
  <ul>
    {% for question in latest_question_list %}
    <li><a href="/polls/{{question.id}}">{{question.question_text}}</a></li>
    {% endfor %}
  </ul>
{% else %}
  <p>No polls are available.</p>
{% endif %}
{% endraw %}
```

## views.py 와 templates 의 index.html 파일 연결
- `order_by`를 통해서 오름차순, 내림차순으로 모델클래스를 가져올 수 있다.
- dic 형식으로 models 클래스의 데이터를 index.html로 보내줄 수 있다.

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

def index(request):
    # 모델클래스 Question을 가져온다. (pub_date 내림차순으로)
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    return render(request, 'polls/index.html',{'latest_question_list' : latest_question_list})

```
