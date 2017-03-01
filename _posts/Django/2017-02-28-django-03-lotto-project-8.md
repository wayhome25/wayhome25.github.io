---
layout: post
title: django 03. 첫번째 장고앱 8 - form 만들기, post 처리
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 03. 첫번째 장고앱 8 - form 만들기, post 처리
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## form 만들기
- [장고 가이드 문서](https://docs.djangoproject.com/en/1.10/topics/forms/#building-a-form-in-django)
- 데이터를 입력 받는 form을 작성한다.
- 작성경로 : lotto/mylotto/forms.py (app 폴더 내부)
- `forms.py` 코드

```python
from django import forms
from .models import GuessNumbers
# 모델클래스 GuessNumbers로 부터 데이터를 입력 받을 폼을 작성한다.

class PostForm(forms.ModelForm): #forms의 ModelForm 클래스를 상속 받는다.

    class Meta:
        model = GuessNumbers #GuessNumbers와 연결
        fields = ('name', 'text', 'num_lotto', ) # 그 중에 입력 받을 것
```

### urls.py 수정
- 프로젝트 폴더 내의 (mysite) `urls.py` 파일에서 form 페이지 경로를 지정한다.   
  (url : /lotto/new/)

```python
from mylotto import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lotto/$', views.index, name = 'lotto'),
    url(r'^$', views.index, name = 'index'),
    url(r'^lotto/new/$', views.post, name = 'new_lotto'),
]
```

### views.py 수정
- lotto/new/ url과 연결할 `views 오브젝트의 post 메소드`를 작성한다.   
  (일반적으로 form은 메소드 이름으로 post를 갖는다)

```python
from .forms import PostForm

def post(request):
    form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
    return render(request, 'lotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달
```

### form.html 템플릿 작성

```html
{% raw %}
<!DOCTYPE html>
{% load staticfiles %}
<html lang="ko">
 <head>
  <title>My Little Lotto</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
  <link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/lotto.css' %}">
 </head>
 <body>
  <div class="page-header">
   <h1>My Little New Lotto</h1>
  </div>
  <div class="container lotto">
   <form method="POST" class="post-form">
       {%csrf_token%}  <!-- 보안이슈로 입력 -->
       {{form.as_p}}
     <button type="submit" class="save btn btn-default">Save</button>
   </form>
  </div>
 </body>
</html>
{% endraw %}
```
```html
{% raw %}
- {{ form.as_table }} will render them as table cells wrapped in <tr> tags
- {{ form.as_p }} will render them wrapped in <p> tags
- {{ form.as_ul }} will render them wrapped in <li> tags
{% endraw %}
```

## post 처리
- get으로 접속했을 때 화면과, post로 접속했을 때 화면을 분기한다.
- redirect를 위해서는 `from django.shortcuts import redirect` 모듈이 필요하다.
- redirect를 위한 경로는 url 절대경로가 아닌, urls.py 의 url name을 입력하면 된다.


### views.py 수정
- [model formsets 가이드 문서](https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/#model-formsets)

```python
from django.shortcuts import render, redirect
from .forms import PostForm

def post(request):
    if request.method == "POST":
         # create a form instance and populate it with data from the request:
        form = PostForm(request.POST) #PostForm으로 부터 받은 데이터를 처리하기 위한 인스턴스 생성
        if form.is_valid(): #폼 검증 메소드
            lotto = form.save(commit = False) #lotto 오브젝트를 form으로 부터 가져오지만, 실제로 DB반영은 하지 않는다.
            lotto.generate()
            return redirect('index') #url의 name을 경로대신 입력한다.
    else:
        form = PostForm() #forms.py의 PostForm 클래스의 인스턴스
        return render(request, 'lotto/form.html', {'form' : form})  # 템플릿 파일 경로 지정, 데이터 전달

```
