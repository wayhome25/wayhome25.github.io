---
layout: post
title: django 06. 두번째 장고앱 8 - 하드코딩 URL 제거, namespace, app_name
category: Django
tags: [python, 파이썬, Django, template]
comments: true
---
# django 06. 두번째 장고앱 8 - 하드코딩 URL 제거
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## 하드코딩된 URL을 제거한다
- 기존의 하드코딩된 index.html의 URL 링크

```html
{% raw %}
{% for question in latest_question_list %}
<li><a href="/polls/{{question.id}}">{{question.question_text}}</a></li>
{% endfor %}
{% endraw %}
```
- 하드코딩 대신에 url 마다 갖고 있는 `name` 값(urls.py)을 활용한다.
- 하드코딩 url 보다 url의 name 값을 사용하는 것이 유지보수를 위해서 더 좋다.
- html 내에서  `url 'url 네임값' 전달할 파라미터` 형식으로 작성 가능하다.

```html
{% raw %}
{% for question in latest_question_list %}
<li><a href="{% url 'detail' question.id%}">{{question.question_text}}</a></li>
{% endfor %}
{% endraw %}
```
## 네임스페이스
- url의 name 값을 사용하다 보면 이름이 중복되는 문제가 발생할 수 있다.
- 중복을 방지하기 위해서 `app_name` 이라는 url 네임스페이스를 사용할 수 있다.
- 네임스페이스 예시

```python
# myapp/urls.py
app_name = 'polls' #url 네임 스페이스

# mysite/urls.py
url(r'^video/', include('video.urls', namespace='video'))
```

- index.html 의 링크 name 값에도 `polls:detail` 처럼 네임 스페이스를 함께 적어야 한다. (`중요 : 띄어쓰기 없음`)

```html
{% raw %}
{% for question in latest_question_list %}
<li><a href="{% url 'polls:detail' question.id%}">{{question.question_text}}</a></li>
{% endfor %}
{% endraw %}
```
