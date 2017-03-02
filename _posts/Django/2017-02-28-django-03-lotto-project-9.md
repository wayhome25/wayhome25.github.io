---
layout: post
title: django 03. 첫번째 장고앱 9 - 앱 다듬기
category: Django
tags: [python, 파이썬, Django, 템플릿]
comments: true
---
# django 03. 첫번째 장고앱 9 - 앱 다듬기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## urls.py 추가 (위치 : 프로젝트 폴더 - mysite)
- detail 페이지를 추가한다.
- 정규표현식 사용, url에 입력된 해당 숫자를 lottokey 변수에 argument perameter 로 담는다.


```python
{% raw %}
urlpatterns = [
    ...
    ...
    #lottokey라는 변수에 숫자로 된 url 부분이 전달된다.
    #url에서 view로 전달할 때 해당 perameter를 함께 전달한다.  
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name = 'detail'),
]
{% endraw %}
```

## views.py 수정 (위치 : 앱 폴더 - mylotto)

```python
{% raw %}
def detail(request, lottokey): # perameter 'lottokey'를 함께 전달
    #primary key가 lottokey 파라미터와 일치하는 오브젝트를 가져온다.
    #primary key는 클래스의 오브젝트 생성시 자동으로 생성, .py 를 통해 가져올 수 있다.
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, 'lotto/detail.html', {'lotto' : lotto})
{% endraw %}
```

## detail.html 탬플릿 작성

- post 페이지로 이동하는 버튼을 작성한다.
- detail 페이지 탬플릿을 작성한다.

```html
{% raw %}
  <!DOCTYPE html>
  {% load staticfiles %}
  <html lang="ko">
  <head>
    <link rel="stylesheet" href="{% static 'css/lotto.css'%}">
  </head>

  <body>
    <div class="page-header">
    <h1>My Lotto Page</h1>
    </div>
    <div class="container lotto">
      <h2>{{lotto.text}}</h2>
      <p> by {{lotto.name}}</p>
      <p> {{lotto.update_date}}</p>
      <p> {{lotto.lottos|linebreaksbr}}</p>
    </div>
  </body>
{% endraw %}
```



## default.html 탬플릿 수정
- post 템플릿으로 연결하는 버튼을  추가한다.

```html
{% raw %}
<a href="{% url 'new_lotto'%}">
  <span class="glyphicon glyphicon-plus btn btn-default"></span>
</a>
{% endraw %}
```

- 각 제목에 detail 링크를 추가한다.


```html
{% raw %}
<div class="page-header">
<h1>My Lotto Page
  <a href="{% url 'new_lotto' %}"><span class="glyphicon glyphicon-plus btn btn-default"></span></a></h1>
</div>

<h2><a href="{% url 'lotto_detail' lottokey=lotto.pk  %}">{{lotto.text}}</a></h2>
{% endraw %}
```
