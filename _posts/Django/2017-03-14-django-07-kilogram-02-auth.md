---
layout: post
title: django 07. 세번째 장고앱 02 - 로그인, 로그아웃, form 커스터마이징
category: Django
tags: [python, 파이썬, Django]
comments: true
---
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)

> 세번째 장고앱 '킬로그램'에 로그인, 로그아웃 기능을 구현한다.


## static 파일 추가 - css

- `static 파일경로` : kilogram/static/kilogram/style.css
- (참고) template 파일경로 : kilogram/templates/kilogram/index.html
- style.css

```css
a {
    color: green;
    text-decoration: none;
}
```

- base.html 템플릿에는 `load static` 구문이 있는데 `load staticfiles` 로 고칠 수 있다. [관련 링크](http://stackoverflow.com/questions/24238496/what-is-the-difference-between-load-staticfiles-and-load-static)
- 이 경우 `python manage.py collectstatic` 명령을 서버 실행 전에 수행해야 한다.
- 상기 명령을 통해서 최상위 폴더 내 static 폴더에 모든 static 파일이 모인다. settings.py 설정 내용 : `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
- 이는 배포할때 중요한 커멘드로, 정적파일은 로컬이 아닌 클라우드 같은 다른 strage에 저장되는 경우가 많다. 그럴 경우에 `collectstatic` 명령어가 사용된다. (다음 배포관련 부분에서 자세히 다룰 예정)

## 로그인 구현순서
- MVT 순서로 구현해 본다.
- Model : django.contrib.auth.models.User 내장 클래스 사용
- View : 내장 로그인 View 사용
- Template : 간단하게 작성

## model

- 장고의 `django.contrib.auth.models.User` 라는 클래스를 그대로 사용한다. (Full framework)
- 특별한 코딩은 필요하지 않다.

## auth 관련 url 추가하기

- 장고에 기본으로 내장된 인증 기능을 include하여 활용한다.
- settings/urls.py 수정

```python
urlpatterns = [
  url(r'^accounts/', include('django.contrib.auth.urls')),
]
```

- **auth.urls를 include 할 경우 아래와 같은 url들이 포함된다.** [관련문서](https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views)

```shell
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
```


## view 만들기

login 관련 기능에는 별도로 view를 작성할 필요 없이 `템플릿만` 작성하면 된다.


## template 만들기

- 로그인과 로그아웃에 사용할 템플릿을 만든다.
- 경로와 이름이 이미 정해져 있는데 로그인은 만들지 않으면 에러가 발생하고, 로그 아웃은 관리자용 페이지를 사용한다.(둘 다 모두 직접 만들어 주는 것이 좋다.)


### base.html 수정

- `로그인 및 로그아웃 링크를 추가` 한다.
- 로그인한 상태와 로그인하지 않은 상태에서 보여줄 링크도 변경한다
- `if user.is_active` : 유저가 로그인 상태일때 (django 템플릿 문법)

```html
{% raw %}
<ul class="nav navbar-nav navbar-right">
  {% if user.is_active %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-heart"></span> {{user.username}}</a></li>
  <li><a href="{% url 'logout' %}">Logout</a></li>
  {% else %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-user"></span> Login</a></li>
  <li><a href="{% url 'admin:index' %}">Admin</a></li>
  {% endif %}
</ul>
{% endraw %}
```

## shell에서 로그인용 사용자 생성해 보기

- 완료 후 admin 툴을 이용해서 확인한다.
- 템플릿 상에서도 로그인이 잘 되는지 확인한다.
- [관련문서](https://docs.djangoproject.com/en/1.10/topics/auth/default/#creating-users)

```
$ python manage.py shell
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('chiken1', 'chiken1@out.org', 'pass5678')
>>> user = User.objects.create_user(username = 'test1', email = 'na@na.com', password = '1234')
>>> User.objects.all() # 전체 User 리스트 확인
```

### login.html 템플릿 작성
- 로그인 페이지 템플릿을 작성한다.
- `파일 경로` : registration/login.html (내장된 인증모델의 로그인 템플릿의 경로는 해당 경로와 파일명으로 지정되어 있다.)
- [관련문서](https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views)

```html
{% raw %}
  {% extends 'kilogram/base.html' %}
  {% block content %}

  <!-- 로그인 되어있는 경우 -->
  {% if user.is_active %}
  <h2> Welcome, {{user.username}} </h2>
  <a href="{% url 'logout' %}">로그아웃</a>

  <!-- 로그인 되어있지 않은 경우 -->
  {% else %}
  {% if form.errors %}
    <!-- 에러발생시 -->
  <p>ID나 비밀번호가 일치하지 않습니다.</p>
  {% endif %}
    <!-- 로그인 폼 -->
  <form method="post" action="{% url 'login' %}">
  {% csrf_token %}
  <input type="hidden" name="next" value="" />
  {{ form.as_p }}
  <button type="submit">로그인</button>
  </form>

  {% endif %}
  {% endblock %}
{% endraw %}
```

### (참고) login.html 템플릿에서 로그인 폼 커스터마이징

- registration/login.html에서 사용하는 내장된 로그인 폼 (위 코드에서 form.as_p 로 사용한)을 커스터마이징 할 수 있다.
- [참고문서](https://docs.djangoproject.com/en/1.10/topics/forms/#rendering-fields-manually)


```html
{% raw %}
<form method="POST" action="{% url 'login' %}" class="sign-in-form">
  {% csrf_token %}
  <h2 class="sub-title"> 로그인 </h2>
  <!-- <input type="hidden" name="next" value="">
  {{form.as_p}} >> 기본으로 내장된 로그인 폼을 아래와 같이 커스터마이징 한다-->
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
  <input type="hidden" name="next" value="">
</form>
{% endraw %}
```

## settings.py 수정

- 로그인후 리다이렉트 페이지는 기본적으로 /accounts/profile 로 지정되어 있는데 이를 변경한다.
- settings.py의 가장 아래에 아래 내용을 추가한다.

```python
# Auth settings
LOGIN_REDIRECT_URL = '/kilogram/'
```



## 로그아웃용 template 만들기

- 파일경로 : registration/logged_out.html (내장된 인증모델의 로그아웃 템플릿의 경로는 해당 경로와 파일명으로 지정되어 있다.)
- 템플릿 이름이 다르면 안된다. 파일이름은 장고 소스의 auth.views.logout()을 보면 확인할 수 있다. [참고](https://github.com/django/django/blob/master/django/contrib/auth/views.py)
- settings.py 에서 `INSTALLED_APPS` 내용 중 app 파일이 admin 파일보다 위에 와야한다. 그렇지 않으면 템플릿 파일 override가 동작하지 않는다.

```html
{% raw %}

{% extends 'kilogram/base.html' %}
{% block content %}

<h2> 잘 가요, 안녕. </h2>
<p><a href="{%url 'login'%}">다시 로그인하기</a></p>

{% endblock %}
{% endraw %}
```

## 로그아웃 후 바로 홈으로 보내기
- 내장된 인증 관련 views를 활용하여 별도의 로그인 템플릿 지정 및 로그아웃 후 바로 홈으로 리다이렉트가 가능하다.
- urls.py

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),
url(r'^login/$', auth_views.login,  {'template_name':'memo_app/login.html'}),
]
```

## 참고 링크
- <https://docs.djangoproject.com/en/1.10/ref/urlresolvers/>
- <https://docs.djangoproject.com/en/1.10/topics/auth/default/>
