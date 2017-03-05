---
layout: post
title: django 06. 두번째 장고앱 7 - 404 핸들링
category: Django
tags: [python, 파이썬, Django, template]
comments: true
---
# django 06. 두번째 장고앱 7 - 404 핸들링
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## 템플릿 파일 작성 - detail.html
- 위치 : app2/polls/templates/polls/detail.html
- detail.html 코드내용

```html
{% raw %}
{{ question }}
{% endraw %}
```

## views.py 와 templates 의 detail.html 파일 연결

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question

# url을 views 의 메소드들과 연결해주는 것 >> function based view
def detail(request, question_id):
    q = Question.objects.get(pk = question_id)
    return render(request, 'polls/detail.html', {'question' : q})
```

## 404 페이지 표시 - try-except 예외처리 사용
- 에러가 날 경우에는 `예외처리`를 통해서 404 페이지를 표시하는 것이 좋다.
- django.http의 `Http404` 함수를 import 한다.


```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question

def detail(request, question_id):
    # 예외처리
    try:
        q = Question.objects.get(pk = question_id) # 에러가 발생할지 모르는 코드
    except Question.DoesNotExist: #DoesNotExist 에러가 발행하면
        raise Http404("Question %s does not exist" % question_id)

    return render(request, 'polls/detail.html', {'question' : q})
```

## 404 페이지 표시 - shortcuts 사용
- 예외처리를 통한 404 페이지 표시는 `아주 많이 사용되는` 기능이다.
- 따라서 장고에서는 `get_object_or_404` 등의  통해 간단하게 기능을 구현할 수 있다.
- `get_list_or_404` 함수도 있다. [관련문서](https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/)

```python
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Question

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question' : q})
```
