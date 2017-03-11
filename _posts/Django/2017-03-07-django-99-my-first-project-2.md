---
layout: post
title: django 04. 장고 개인 프로젝트 2 - 인증 (회원가입, 로그인)
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
# django 04. 장고 개인 프로젝트 (메모 앱) - 인증 (회원가입, 로그인)
> 개인 프로젝트에 인증 기능을 추가하는 과정을 기록하였습니다.

## 결과물
- <http://siwabada.pythonanywhere.com/>
- [Using the Django authentication system](https://docs.djangoproject.com/en/1.10/topics/auth/default/)
- [ModelForm](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#modelform)
- [How to log a user in](https://docs.djangoproject.com/en/1.10/topics/auth/default/#how-to-log-a-user-in)
- [Authentication data in templates](https://docs.djangoproject.com/en/1.10/topics/auth/default/#authentication-data-in-templates)
- [Taking User Input to create Users in Django](http://stackoverflow.com/questions/11287485/taking-user-input-to-create-users-in-django)
- [Authentication Views](https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views)
- [로그인, 로그아웃 하기](http://blog.hannal.com/2015/06/start_with_django_webframework_08/)

-------

# 회원가입

## ModelForm 작성
- 회원가입시 데이터를 입력 받을 폼을 작성한다.
- ModelForm 은 자동적으로 당신이 제공한 model 소속의 폼을 작성한다. 그리고 필드에 기초해서 입력값을 확인한다.
- forms.py

```python
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
```

## url 패턴추가
- urls.py

```python
urlpatterns = [
    url(r'^join/$', views.signup, name='join'),
]
```

## view 작성
- views.py 에 signup 메소드 추가
- POST request 인 경우, UserForm으로 받은 POST 값을 가지고 신규 유저를 등록
- 일반 접속인 경우, UserForm 을 반환
- views.py

```python
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'memo_app/adduser.html', {'form': form})
```

## template 작성

```html
{% raw %}
<h2>회원가입</h2>
<form method="post" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="회원가입" />
</form>
{% endraw %}
```

<center>
 <figure>
 <img src="/assets/post-img/django/signup.png" alt="views">
 <figcaption>adduser.html 탬플릿 구현화면</figcaption>
 </figure>
 </center>

---------

# 로그인 구현 첫번째 방법 - ModelForm 사용

## ModelForm 작성
- 로그인시 데이터를 입력 받을 폼을 작성한다.
- ModelForm 은 자동적으로 당신이 제공한 model 소속의 폼을 작성한다. 그리고 필드에 기초해서 입력값을 확인한다.
- forms.py

```python
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password'] # 로그인 시에는 유저이름과 비밀번호만 입력 받는다.
```

## url 패턴추가
- urls.py

```python
urlpatterns = [
  url(r'^login/$', views.signin, name='login'),
]
```

## view 작성
- views.py 에 signin 메소드 추가 (메소드 명이 함수명 ex. login() 등과 겹치지 않도록 주의)
- POST request 인 경우, LoginForm으로 받은 POST 값을 가지고 인증 및 로그인
- 일반 접속인 경우, LoginForm을 반환
- views.py

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'memo_app/login.html', {'form': form})
```

## template 작성
- login.html

```html
{% raw %}
<h2>로그인</h2>
<form method="post" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="로그인" />
</form>
{% endraw %}
```

<center>
 <figure>
 <img src="/assets/post-img/django/signin.png" alt="views">
 <figcaption>login.html 탬플릿 구현화면</figcaption>
 </figure>
 </center>

----

# 로그인 후 username을 탬플릿에서 표시

## {{ user }}
- [Authentication data in templates](https://docs.djangoproject.com/en/1.10/topics/auth/default/#authentication-data-in-templates)

- default.html 템플릿
```html
{% raw %}
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}. Thanks for logging in.</p>
{% else %}
    <p>Welcome, new user. Please log in.</p>
{% endif %}
{% endraw %}
```

-----

# 로그인 구현 두번째 방법 - Authentication Views 사용
> 장고는 login, logout, password management 를 위한 몇가지 views를 제공하고 있다.

## Authentication Views 도입 - url include
- urls.py

```python
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
]
```

- 위의 include를 통해서 아래의 url 패턴을 사용할 수 있다.

```python
{% raw %}
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/done/$ [name='password_reset_complete']
{% endraw %}
```


## 상기의 url이 본인이 작성한 view를 사용하게 하는 방법

- auth_views 사용

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^change-password/$', auth_views.password_change),
]
```

- auth_views는 view의 상태를 변경할 수 있는 옵션 인자를 받는다. 예를 들어, 만약 template name을 변경하고 싶은 경우 인자 template name을 제공할 수 있다.
- 그밖에 제공 가능한 인자는 [가이드문서 ](https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views) 에서 확인

```python
urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}), #로그아웃 후 홈으로 이동
    url(r'^login/$', auth_views.login),
    url('^', include('django.contrib.auth.urls')),
]
```

## 로그인 후 홈으로 이동하도록 하는 방법
- django.contrib.auth.views.login은 로그인이 성공하면 settings.LOGIN_REDIRECT_URL (which defaults to /accounts/profile/) 으로 리다이렉트 하도록 설정되어 있다.
- 변경을 위해서는 settings.py 에 LOGIN_REDIRECT_URL 항목 추가가 필요하다.

- settings.py

```python
# 로그인 이후 경로 수정
LOGIN_REDIRECT_URL = "/"
```

## 글쓰기 PostForm 과 로그인한 usrname을 연결하는 방법 1
- 글 작성후 POST로 데이터 전송시, 해당 모델 클래스의 name 컬럼에 현재 usrname 을 저장한다.
- `memo.name = request.user.get_username()`
- views.py

```python
def post(request):
    if request.method == "POST":
        #저장
        form = PostForm(request.POST)
        if form.is_valid():
            memo = form.save(commit = False)
            memo.name = request.user.get_username()
            memo.generate()
            return redirect('index')
    else:
        #입력
        form = PostForm()
        return render(request, 'memo_app/form.html',{'form': form})
```

## 글쓰기 PostForm 과 로그인한 usrname을 연결하는 방법 2 - ForeignKey 사용
- models.py 수정
- Memos 모델 클래스의 컬럼 name_id 를 User 모델 클래스와 연결한다.
```python
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Memos(models.Model):
    name_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
    return '%s by %s' % (self.title, self.name_id)
```

- views.py 수정
- `memo.name_id = User.objects.get(username = request.user.get_username())` 를 통해서 현재 로그인된 username을 갖는 User의 오브젝트를 name_id 컬럼에 할당한다.
```python
def post(request):
    if request.method == "POST":
        #저장
        form = PostForm(request.POST)
        if form.is_valid():
            memo = form.save(commit = False)
            memo.name_id = User.objects.get(username = request.user.get_username())
            memo.generate()
            return redirect('index')
```
