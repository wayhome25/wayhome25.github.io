---
layout: post
title: django 06. 두번째 장고앱 11 - 결과 페이지 만들기
category: Django
tags: [python, 파이썬, Django]
comments: true
---

> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      

## views.py의 result 함수를 수정한다.

```python
def results(request, question_id): #question_id를 파라미터로 받는다.
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question' : question})
```

## results.html 템플릿을 만든다.

```html
{% raw %}
<h1>{{question.question_text}}</h1>

<ul>
  {% for choice in question.choice_set.all %}
    <li>{{choice.choice_text}} : {{choice.votes}} 표</li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">투표 화면으로 돌아가기</a>
{% endraw %}
```
