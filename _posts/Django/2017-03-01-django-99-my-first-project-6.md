---
layout: post
title: django 04. 장고 개인 프로젝트 6 - 회원가입, 로그인 폼 꾸미기
category: Django
tags: [python, 파이썬, Django, 인증]
comments: true
---
> 개인 프로젝트에 회워가입, 로그인 페이지를 커스터마이징 하는 과정을 기록하였습니다.

## 원하는 상태
- 회원가입, 로그인 폼을 css를 통해서 커스터마이징한다.
- User model form 필드의 기본 글자 수 제한을 변경한다.


## 결과물
- <http://siwabada.pythonanywhere.com/>

# 회원가입 폼 커스터마이즈

## forms.py 수정

- 회원가입에서 사용되는 UserForm을 수정한다.
- `widgets` 를 통해서 각 폼 필드의 `형식`과 class명을 포함한 `어트리뷰트`를 추가할 수 있다.
- `labels` 를 통해서 각 폼 필드의 `label`을 지정할 수 있다.
- `__init__` 메소드를 통해서 부모모델 User의 기본 설정을 (maxlength 등) 변경할 수 있다.

```python
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': '닉네임',
            'email': '이메일',
            'password': '패스워드'
        }
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15
```

## views.py

```python
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('index')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'memo_app/adduser.html', {'form': form})
```

## adduser.html 템플릿 수정

```html
{% raw %}
{% if user.is_authenticated %}
<script type="text/javascript">
  alert('잘못된 접근입니다. \n회원가입을 위해서는 로그아웃이 필요합니다.')
  window.location.href = '/';
</script>
{% else %}
<form method="POST" action="" class="sign-up-form">
  {%csrf_token%}
  <h2 class="sub-title"> 회원가입 </h2>
  {% for field in form %}
      <div class="form-group">
        {{ field.label }}
        {{field}}
      </div>
  {% endfor %}
  <button type="submit" class="save btn btn-success">회원가입</button>
  <a href="{% url 'index' %}">
    <button type="button" class="btn btn-danger">취소</button>
  </a>
</form>
{% endraw %}
```

# 로그인 폼 커스터마이즈

## urls.py 수정
- django 내장 인증기능 `auth_views.login` 을 사용하면, 기본 템플릿의 경로는 `templates/registration/login.html` 이다
- 별도의 템플릿을 사용하고자 하는 경우 아래와 같은 별도 설정이 필요하다.

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
  url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}),
]

```

## login.html 템플릿 수정
- 템플릿 수정을 통해서 원하는 class, id 등의 어트리뷰트 설정이 가능하다.

```html
{% raw %}
<form method="post" action="{% url 'login' %}" class="sign-in-form">
  {%csrf_token%}
  <h2 class="sub-title"> 로그인 </h2>
  {% if form.errors %}
  <p>Your username and password didn't match. Please try again.</p>
  {% endif %}
  {% if next %}
      {% if user.is_authenticated %}
      <p>Your account doesn't have access to this page. To proceed,
      please login with an account that has access.</p>
      {% else %}
      <p>Please login to see this page.</p>
      {% endif %}
  {% endif %}
  <div class="form-group">
    <label for="{{ form.username.id_for_label }}">닉네임</label>
    <input class="form-control" id="{{ form.username.id_for_label }}" maxlength="15" name="{{ form.username.html_name }}" type="text" />
  </div>
  <div class="form-group">
    <label for="{{ form.password.id_for_label }}">패스워드</label>
    <input class="form-control" id="{{ form.password.id_for_label }}" maxlength="120" name="{{ form.password.html_name }}" type="password" />
  </div>
  <input type="submit" class="save btn btn-success" value="로그인">
  <a href="{% url 'index' %}">
    <button type="button" class="btn btn-danger">취소</button>
  </a>
  <input type="hidden" name="next" value="{{ next }}" />
</form>
{% endraw %}
```
