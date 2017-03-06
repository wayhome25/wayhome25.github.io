---
layout: post
title: django 06. 두번째 장고앱 10 - POST 처리
category: Django
tags: [python, 파이썬, Django, form]
comments: true
---
# django 06. 두번째 장고앱 10 - POST 처리
> [파이썬 웹 프로그래밍 - Django로 웹 서비스 개발하기 ](https://www.inflearn.com/course/django-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EA%B0%95%EC%A2%8C/)      


- POST 폼을 처리할 vote 페이지를 작성한다.  
- form의 action 값은 vote 페이지로 설정되어 있다.

```html
{% raw %}
<form action="{% url 'polls:vote' question.id %}" method="POST">
{% endraw %}
```

- views.py 의 vote 함수가 POST 처리 할 수 있도록 수정한다.
- `question.choice_set.get(pk = request.POST['choice'])` 를 통해서 POST form에서 선택된 라디오 버튼의 `value` 값을 가져올 수 있다.
- 예외 처리를 통해서 올바르지 않은 라디오 버튼을 선택시 error_message를 전달한다.
- 예외 처리에서 문제가 없으면 .save()를 통해 업데이트 한다.
- vote 페이지가 POST를 처리하고 나면 `return redirect('polls:results', question_id = question.id)`를 통해 result 페이지로 이동시킨다.


```python
def vote(request, question_id): #POST를 처리할 수 있도록 작성한다.
    question = get_object_or_404(Question, pk = question_id)
    try:
        # POST form에서 'choice' name 값을 갖는 input의 value 값을 가져온다.
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id = question.id)
```
