---
layout: post
title: django 06. 두번째 장고앱 9 - 간단한 폼 직접 만들기
category: Django
tags: [python, 파이썬, Django, form]
comments: true
---
# django 06. 두번째 장고앱 9 - 간단한 폼 직접 만들기
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)       

## detail.html 템플릿에 form 을 추가
- 지난번 실습에서는 form 클래스(form.py)를 사용해서 form을 작성했으나, 이번에는 2개의 모델을 갖고 (Question, Choice) custom form을 작성한다.
- form 안에는 보안을 위해서 `csrf_token`을 무조건 넣어준다.
- input 의 name 값은 post의 dictionary 처럼 사용 할 수 있다.
- `forloop.counter`를 통해서 반복하면서 하나씩 증가하는 임의의 숫자를 추가할 수 있다. (1부터 시작)

### views.py 내의 DetailView 클래스

```python
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```
### detail.html 템플릿 코드

```html
{% raw %}
<h2>{{question.question_text}}</h2>

{%if error_message %} <p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="POST">
  {% csrf_token %}
  <!-- 해당 question의 선택지들을 하나씩 보여준다 .all()이 아닌것 주의 -->
  {% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{choice.id}}">
    <label for="choice{{ forloop.counter }}">{{choice.choice_text}}</label><br>
  {% endfor %}
  <input type="submit" value="투표">
</form>
{% endraw %}
```

### 랜더링된 detail.html 코드

```html
{% raw %}

<h2>최고의 고기는?</h2>

<form action="/polls/1/vote/" method="POST">
  <input type='hidden' name='csrfmiddlewaretoken' value='XGkLxShVgsOnJBte8eObFGWctzk9hcgq0qKVj0LMHDQVWAYOnxbYcAzkezRCjXZw' />
  <!-- 해당 question의 선택지들을 하나씩 보여준다 -->

    <input type="radio" name="choice" id="choice1" value="1">
    <label for="choice1">돼지</label><br>

    <input type="radio" name="choice" id="choice2" value="2">
    <label for="choice2">치킨</label><br>

    <input type="radio" name="choice" id="choice3" value="3">
    <label for="choice3">소</label><br>

    <input type="radio" name="choice" id="choice4" value="6">
    <label for="choice4">닭</label><br>

    <input type="radio" name="choice" id="choice5" value="7">
    <label for="choice5">소</label><br>

  <input type="submit" value="투표">
</form>
{% endraw %}
```
