---
layout: post
title: django 07. 세번째 장고앱 03. 회원가입
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)    
> 세번째 장고앱 '킬로그램'에 회원가입 기능을 구현한다.

# auth - 회원 가입 구현하기

## model
역시 모델의 수정은 필요 없다. (내장된 모델 사용)

## mysite/urls.py 수정

- 장고의 auth.urls에는 회원 가입 url이 따로 없기 때문에 구현해 주어야 한다.
  - 회원가입의 경우, view, template 경로가 따로 준비되어 있지 않다. (로그인, 로그아웃과 다름)
- 추후에 settings.py에 관련 속성 값들도 몇가지 추가를 해 줄 예정.

```python
urlpatterns = [
  url(r'^accounts/signup$', kilogram_views.CreateUserView.as_view(), name = 'signup'),
  url(r'^accounts/login/done$', kilogram_views.RegisteredView.as_view(), name = 'create_user_done'),
]
```

## 내장폼 CreateUserForm을 활용해서 CreateUserView (CBV) 만들기

- View 는 generic view 중 폼을 이용해 오브젝트를 생성하는 CreateView를 사용한다.
- reverse_lazy는 reverse와 같은 기능인데 generic view에서 주로 사용한다.    
  타이밍 로딩 문제로 generic view에서는 reverse는 사용할 수 없고 reverse_lazy를 사용해야한다.

- views.py 수정


```python
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
# from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)
from .forms import CreateUserForm # 장고의 기본 회원가입 폼을 커스터마이징 한 폼
from django.core.urlresolvers import reverse_lazy # generic view에서는 reverse_lazy를 사용한다.

# CBV (Class Based View 작성!)
class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
    template_name = 'registration/signup.html' # 템플릿은?
    form_class =  CreateUserForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
    # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
    success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
    template_name = 'registration/signup_done.html' # 템플릿은?
```

## login.html 에 내용 추가

- 아래 내용 추가

```
{% raw %}
<br>
<p>아이디가 없으신가요? <a href="{% url 'signup'%}">회원가입</a></p>
{% endraw %}
```

## template 생성

- CreateUserView와 RegisteredView에서 사용할 template을 작성

### registration/signup.html

```html
{% raw %}
{% extends 'kilogram/base.html' %}
{% block content %}

<form method="post" action="{% url 'signup' %}">
{% csrf_token %}
{{ form.as_p }}
<button type="submit">회원가입</button>
</form>

{% endblock %}
{% endraw %}
```



### registration/signup_done.html

```html
{% raw %}
{% extends 'kilogram/base.html' %}
{% block content %}

<h2>회원가입이 완료되었습니다. </h2>
<br>
<a href="{% url 'login'%}">로그인하기</a>

{% endblock %}
{% endraw %}
```


## 회원가입 폼 클래스(CreateUserForm) 만들기 - 내장 폼 커스터마이징

- 회원가입 폼을 만드는 방법은 여러가지가 있을 수 있는데, 그 중 가장 간단한 장고에서 제공하는 UserCreationForm(django.contrib.auth.forms.UserCreationForm)을 사용한다.
- 다만 요즘 대부분의 사이트에서 필수적으로 받는 이메일도 입력받기 위해서 추가적으로 구현을 한다.


- forms.py 생성

```python
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
```


## 참고 링크
- [Source code for django.contrib.auth.forms](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/)
- <https://docs.djangoproject.com/en/1.10/ref/urlresolvers/>
- <https://docs.djangoproject.com/en/1.10/topics/auth/default/>
